from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum


class EyeGamePage:

    url = "https://www.igame.com/eye-test/"

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("Iframe"))

    def click_chosenone(self):
        self.driver.find_element_by_css_selector('.thechosenone').click()

    def get_current_time(self):
        self.driver.find_element_by_css_selector('.clock').text

    def get_to_level(self, num_of_clicks):
        for i in range(num_of_clicks):
            self.click_chosenone()


    def get_reached_level(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.character-title').text







