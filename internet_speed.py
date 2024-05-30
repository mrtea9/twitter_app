from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        internet_speed_url = 'https://www.speedtest.net/'
        self.driver.get(internet_speed_url)
        go_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        download = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = download.text
        upload = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = upload.text
        print(self.down, self.up)

    def tweet_at_provider(self):
        twitter_url = 'https://twitter.com/login'
        self.driver.get(twitter_url)
        sign_in = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[2]/span[1]')
        time.sleep(5)

