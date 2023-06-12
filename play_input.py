SEARCH_URL = 'https://partscatalog.deere.com/jdrc/search/type/parts/term/'
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
