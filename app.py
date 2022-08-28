import logging
import os

from flask import Flask
from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.example.com/'

app = Flask(__name__)


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


@app.route('/test', methods=['GET'])
def test():
    phantomjs_example()
    return 'fine'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
