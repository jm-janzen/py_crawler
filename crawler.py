import time  # For sleep
import argparse  # For command line args

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # For default wait interval
from selenium.common import exceptions as SeleniumExceptions  # For help on first run
from xvfbwrapper import Xvfb as VirtualDisplay  # For headless browsing

def init_driver():
    """
    Returns webdriver in $PATH and specifies default wait
    period of 5 seconds for an event to occur
    """
    try:
        driver = webdriver.Firefox()
        driver.wait = WebDriverWait(driver, 5)
    except SeleniumExceptions.WebDriverException as e:

        # Print Exception Type, Message, and exit
        print(type(e).__name__, e)
        exit(1)

    return driver

def navigate(driver, url):
    """ Using given webdriver, navigate to given URL """
    try:
        driver.get(url)
    except SeleniumExceptions.WebDriverException as e:
        print(type(e).__name__, e)

def get_elements(driver, attribute):
    """ Returns a list of names of all instances of the given attribute """
    return driver.find_elements_by_xpath("//*[@" + attribute + "]")

def parse_arguments():
    """
    Returns the attribute to look for, or prints a useful usage message
    and exits.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("url"
        , help="A url to query for the given attribute (leading schema optional)")
    parser.add_argument("attribute"
        , help="A type of attribute to look for (eg: `id' or `class')")

    args = parser.parse_args()

    return parse_url(args.url), args.attribute

def parse_url(url):
    if not url.startswith("http://"):
        url = "http://" + url

    return url


def main():

    url, attribute = parse_arguments()

    # Use X Virtual Frame Buffer (headless display),
    # used as context manager for driver.
    with VirtualDisplay():
        driver = init_driver()

        navigate(driver, url)

        # Retrieve and print results
        attr_list = get_elements(driver, attribute)
        for attr in attr_list:
            print(attr.get_attribute(attribute))

        # Close browser
        driver.quit()

main()
