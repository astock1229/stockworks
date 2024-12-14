AUTHOR = 'Anthony Stock'
SITENAME = 'StockWorks'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),)

# Theme Settings
THEME = 'themes/Flex'
SITETITLE = 'StockWorks'
SITESUBTITLE = 'Exploring Code, ML, and AI'
SITEDESCRIPTION = 'A technical blog about software development, machine learning, and artificial intelligence'
SITELOGO = None  # Add a path to your logo if you have one
FAVICON = None   # Add a path to your favicon if you have one
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'

# Flex Theme Settings
MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

# Social Links
SOCIAL = (
    ('github', 'https://github.com/astock1229'),
)

# Other Settings
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Add custom CSS
CUSTOM_CSS = 'theme/css/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/css/custom.css'}
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
