import logging
from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.example.com/'


def phantomjs_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    browser = webdriver.PhantomJS()
    logging.info('Initialized phantomjs browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


if __name__ == '__main__':
    phantomjs_example()
