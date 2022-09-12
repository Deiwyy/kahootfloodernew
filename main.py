import selenium
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import time

sets = {
    'url': 'kahoot.it',
    'game-pin-field-xpath': '//*[@id="game-input"]',
    'join-button-xpath': '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    'nickname-field-xpath': '//*[@id="nickname"]',
    'start-button-xpath': '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    'buttons-xpath': '//*[@id="root"]/div[1]/div/div/main/div[2]/div/div',
    'true-false-xpath': '//*[@id="root"]/div[1]/div/div/main/div[2]/div/div',

}




class Bot:
    def __init__(self, idd, name):
        self.idd = idd
        self.name = name
        options = Options()
        options.add_argument("excludeSwitches")
        options.add_argument("enable-logging")
        self.driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=options)

    def start(self):
        self.driver.get(sets['url'])
        time.sleep(3)
        self.driver.close()
        self.driver.exit()

b = Bot(None, None)
b.start()