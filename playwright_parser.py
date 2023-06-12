import time

import pandas as pd
from playwright.sync_api import sync_playwright


HOST = 'https://partscatalog.deere.com/jdrc/search'
SEARCH_URL = 'https://partscatalog.deere.com/jdrc/search/type/parts/term/'
USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 ' \
            'Safari/537.36 '
ACCEPT = '*/*'
HEADERS = {
    'User-Agent': USERAGENT,
    'Accept': ACCEPT
}
FILE = 'files/parts.csv'

# block pages by resource type. e.g. image, stylesheet
BLOCK_RESOURCE_TYPES = [
    'beacon',
    'csp_report',
    'font',
    'image',
    'imageset',
    'media',
    'object',
    'texttrack',
]

# block 3rd party resources like tracking:
BLOCK_RESOURCE_NAMES = [
    'adzerk',
    'analytics',
    'cdn.api.twitter',
    'doubleclick',
    'exelator',
    'facebook',
    'fontawesome',
    'google',
    'google-analytics',
    'googletagmanager',
]


def intercept_route(route):
    """Intercept all requests and abort blocked ones"""
    if route.request.resource_type in BLOCK_RESOURCE_TYPES:
        return route.abort()
    if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
        return route.abort()
    return route.continue_()


def get_urls():
    """Create urls for all parts in articles.txt"""
    with open('files/articles.txt', encoding='utf-8') as file:
        articles_list = [i.strip() for i in file.readlines()]

    urls_list = [SEARCH_URL + article for article in articles_list]
    return urls_list


def handle_search_results(parts_list, response):
    if "/v1//search/parts" in response.url:
        parts_data = response.json()['searchResults']
        for item in parts_data:
            try:
                parts_list.append({
                    'name': item['model'],
                    'description': item['equipmentName']
                })
            except KeyError:
                parts_list.append({
                    'name': item['model'],
                    'description': item['partDescription']
                })
            except Exception as e:
                print(e)
                parts_list.append({
                    'name': '-',
                    'description': '-'
                })


def main():
    """Open browser automatically with Playwright and get json data from response"""
    urls = get_urls()
    with sync_playwright() as p:
        parts = []
        for i, url in enumerate(urls):
            try:
                def handle_response(response):
                    handle_search_results(parts, response)

                browser = p.chromium.launch()
                page = browser.new_page()
                page.on("response", handle_response)
                page.route("**/*", intercept_route)
                page.goto(url)
                page.wait_for_selector('div[_ngcontent-serverapp-c50]')

                page.context.close()
                browser.close()
            except Exception as e:
                print(e)
                pd.DataFrame(parts).to_csv(FILE, index=False, sep=';', encoding='utf-8-sig')

            print(f'Parse {i + 1}/{len(urls)} parts')
        pd.DataFrame(parts).to_csv(FILE, index=False, sep=';', encoding='utf-8-sig')


if __name__ == '__main__':
    print('Start parsing...')
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'{total_time:.4f} seconds')
