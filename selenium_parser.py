import json
import time
import random
from typing import List

import pandas as pd
from selenium.webdriver import Keys
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selen_input import (
    SEARCH_URL,
    HEADERS,
    ARTICLES_FILE,
    FILE
)
from timer import timeit


class JohnDeereParser:

    def __init__(self):
        self.url = SEARCH_URL
        self.articles_file = ARTICLES_FILE
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(f'user-agent={HEADERS["User-Agent"]}')
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.options
        )
        self.driver.maximize_window()

    @timeit
    def parse_data(self) -> List[dict]:
        """Parse data with Selenium and return it for next saving to csv"""
        parts_data = []
        articles = self.get_articles()

        # Open first article (this way we don't have to choose search settings)
        self.driver.get(self.url + articles[0])
        self.check_search_results_list()

        result = self.get_search_results()
        parts_data.extend(self.handle_data(result))
        print(f'Parsed: 1/{len(articles)} parts')

        count = 2

        # Repeat for all articles
        for article in articles[1:]:
            try:
                search_input = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="applicationContainer"]/div[1]/div[2]/div[1]/div[2]/app-search/div/div['
                    '1]/app-search-input/div/div[3]/div/p-autocomplete/span/input'
                )
                search_input.clear()
                time.sleep(1)

                search_input.send_keys(article)
                time.sleep(1)

                search_input.send_keys(Keys.RETURN)

                self.check_search_results_list()
                time.sleep(2)

                result = self.get_search_results()
                parts_data.extend(self.handle_data(result))
            except Exception as e:
                print(e)

            time.sleep(random.randrange(1, 3))

            # Randomly sleep every 10 iteration
            if count % 10 == 0:
                time.sleep(random.randrange(2, 5))
            print(f'Parsed: {count}/{len(articles)} parts')
            count += 1

        self.driver.close()

        return parts_data

    def get_articles(self) -> List[str]:
        """Read and return articles from file"""
        with open(self.articles_file, encoding='utf-8') as f:
            articles_list = [i.strip() for i in f.readlines()]

        return articles_list

    def check_search_results_list(self) -> None:
        """Check wile div with data loading"""
        try:
            WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="applicationContainer"]/div[1]/div[2]/div[1]/div[2]/app-search/div/div['
                           '2]/app-search-results/div/div[3]')
            ))
        except Exception as e:
            print(e)

    def get_search_results(self) -> List[dict]:
        """Fetch and return json data from response"""
        request_list = [request for request in self.driver.requests if f'v1//search/parts' in request.url]
        req = request_list[-1]

        body = decode(
            req.response.body,
            req.response.headers.get('Content-Encoding', 'identity')
        )
        str_data = body.decode('utf-8', 'ignore')
        search_result = json.loads(str_data)['searchResults']
        return search_result

    @staticmethod
    def handle_data(data_list) -> List[dict]:
        """Transforms the received data into the required form"""
        parts = []
        for item in data_list:
            try:
                parts.append({
                    'name': item['model'],
                    'description': item['equipmentName']
                })
            except KeyError:
                parts.append({
                    'name': item['model'],
                    'description': item['partDescription']
                })
            except Exception as e:
                print(e)
                parts.append({
                    'name': '-',
                    'description': '-'
                })
        return parts


if __name__ == '__main__':
    print('Start parsing...')
    parser = JohnDeereParser()
    data = parser.parse_data()
    pd.DataFrame(data).to_csv(FILE, index=False, sep=';', encoding='utf-8-sig')
    print('Data saved to file!')
