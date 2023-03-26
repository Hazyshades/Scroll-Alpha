import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class MetaMask:
    def __init__(self, extension_id, password):
        self.extension_id = extension_id
        self.password = password

    def login(self, web_driver):
        web_driver.get(f"chrome-extension://{self.extension_id}/popup.html")
        time.sleep(1)
        passT = web_driver.find_element(By.XPATH, "//*[@id='password']")
        passT.send_keys(self.password)
        time.sleep(3)
        clickT = web_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/button")
        clickT.click()
        time.sleep(3)

        try:
            web_driver.find_element(By.XPATH, '//*[@id="popover-content"]/div/div/section/div[3]/button').click()
            time.sleep(3)
        except NoSuchElementException:
            print("Button Got It doesn't exist")
