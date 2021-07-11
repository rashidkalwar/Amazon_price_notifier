from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirfoxOptions
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.opera import options as OperaOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

"""
gettting a webdriver, checking multiple web browsers in user's system to see which one can we use, 
also making webdriver headless so it is not visible to user and running in background.
"""

driver = None

# Trying with Google Chrome
if not driver:
    try:
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    except: pass

# Trying with Firfox
if not driver:
    try:
        options = FirfoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    except: pass

# Trying with Microsoft Edge
if not driver:
    try:
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('headless')
        edge_options.add_argument('disable-gpu')
        driver = Edge(executable_path=(EdgeChromiumDriverManager().install()), options=edge_options)
    except: pass

# Trying with Opera
if not driver:
    try:
        options = OperaOptions
        options.add_argument("--headless")
        driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
    except: pass

# Trying using Google Chromium
if not driver:
    try:
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)
    except : pass

# Trying using Safari
if not driver:
    try:
        driver = webdriver.Safari()
    except: pass
