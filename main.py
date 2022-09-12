from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

sets = {
    'url': 'https://www.kahoot.it',
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
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path='.\\chromedriver.exe')
        self.driver.get(sets['url'])

    def load_element(self, path, by, ex=True):
        try:
            element = WebDriverWait(self.driver, 5000).until(EC.presence_of_element_located((by, path)))
            return element
        except Exception as e:
            if ex:
                print(f'couldnt find {path} {e}')
                self.driver.quit()
                exit(1)
            return False

    def start(self):
        self.pin_field = self.load_element(sets['game-pin-field-xpath'], By.XPATH)
        self.pin_field.clear()
        self.pin_field.send_keys(self.idd)
        self.pin_field.send_keys(Keys.RETURN)

        self.name_field = self.load_element(sets['nickname-field-xpath'], By.XPATH)
        self.name_field.clear()
        self.name_field.send_keys(self.name)
        self.name_field.send_keys(Keys.RETURN)
        input()

b = Bot('6754', 'saghsdf')
b.start()