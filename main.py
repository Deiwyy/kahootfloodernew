from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

sets = {
    'url': 'https://www.kahoot.it',
    'getreadyurl': 'https://kahoot.it/getready',
    'gameblockurl': 'https://kahoot.it/gameblock',
    'game-pin-field-xpath': '//*[@id="game-input"]',
    'join-button-xpath': '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    'nickname-field-xpath': '//*[@id="nickname"]',
    'start-button-xpath': '//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button',
    'quiz-xpath': '//*[@id="root"]/div[1]/div/div/main/div[2]/div/div',
    'true-false-xpath': '//*[@id="root"]/div[1]/div/div/main/div[2]/div/div',
    'q-type-xpath': '//*[@id="root"]/div[1]/div/div/main/div[1]/div/div[2]/div/div/span'
}

class Bot:
    def __init__(self, idd, name):
        self.idd = idd
        self.name = name
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path='.\\chromedriver.exe')
        self.driver.get(sets['url'])

    def quit(self):
        self.driver.quit()
        exit(0)

    def load_element(self, path, by, ex=True):
        try:
            element = WebDriverWait(self.driver, 5000).until(EC.presence_of_element_located((by, path)))
            return element
        except Exception as e:
            if ex:
                print(f'couldnt find {path} {e}')
                self.quit()
            return False

    def start(self):
        pin_field = self.load_element(sets['game-pin-field-xpath'], By.XPATH)
        pin_field.clear()
        pin_field.send_keys(self.idd)
        pin_field.send_keys(Keys.RETURN)

        name_field = self.load_element(sets['nickname-field-xpath'], By.XPATH)
        name_field.clear()
        name_field.send_keys(self.name)
        name_field.send_keys(Keys.RETURN)

        while True:
            while not self.driver.current_url == sets['gameblockurl']:
                time.sleep(0.2)
                if self.driver.current_url == 'https://kahoot.it/ranking':
                    self.quit()
            qType = self.load_element(sets['q-type-xpath'], By.XPATH)
            buttons = []
            if qType.text.lower() == 'quiz':
                buttons = self.load_element(sets['quiz-xpath'], By.XPATH, ex=False)
                buttons = buttons.find_elements(By.XPATH, '//button')
                print(buttons)
            else:
                buttons = self.load_element(sets['true-false-xpath'], By.XPATH, ex=False)
                buttons = buttons.find_elements(By.XPATH, '//button')
            if buttons: random.choice(buttons).click()


def main(amount, basename, idd):
    for i in range(amount):
        b = Bot(idd, basename+str(i+1))
        b.start

if __name__ == '__main__':
    idd = sys.argv[1]
    name = sys.argv[2]
    am = sys.argv[3]
    main(am, name, idd)