import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException, ElementClickInterceptedException
from Helpers import bridge_amount


class Browser:
    def __init__(self, profile_path, profile_number, metamask):
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={profile_path}")
        options.add_argument(f'--profile-directory={profile_number}')
        self.metamask = metamask
        self.webdriver = webdriver.Chrome(chrome_options=options)

    def login(self):
        self.metamask.login(self.webdriver)

    def add_networks(self):
        self.metamask.add_networks(self.webdriver)

    def allow_test_network(self):
        self.metamask.allow_test_network(self.webdriver)

    def change_current_networks(self):
        self.metamask.change_current_networks(self.webdriver)

    def connect_mm(self, game_url):
        try:
            self.webdriver.get(game_url)
            time.sleep(5)
            self.switch_network()
        except IndexError:
            print("Network already connected")

    def bridge_to_scroll(self):
        enter_amount = self.webdriver.find_element(By.XPATH,
                                                   '//*[@id=":r0:"]')
        enter_amount.send_keys(bridge_amount)
        time.sleep(3)
        send_button = self.webdriver.find_element(By.XPATH,
                                                  '//*[@id=":r2:"]')
        if send_button.is_enabled():
            send_button.click()

        time.sleep(3)
        self.confirm_transaction()
        time.sleep(1113)

    def confirm_transaction(self):
        self.webdriver.switch_to.window(self.webdriver.window_handles[1])
        time.sleep(10)
        # click Confirm
        Confirm = self.webdriver.find_element(By.XPATH,
                                              '//*[@id="app-content"]/div/div[2]/div/div[3]/div[3]/footer/button[2]')
        Confirm.click()
        time.sleep(1)

    def approve(self):
        self.webdriver.switch_to.window(self.webdriver.window_handles[1])
        print("Second window title = " + self.webdriver.title)
        time.sleep(10)
        # click Next
        Approve = self.webdriver.find_element(By.XPATH,
                                              '//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
        Approve.click()
        time.sleep(1)
        Approve.click()

    def switch_network(self):
        self.webdriver.switch_to.window(self.webdriver.window_handles[1])
        time.sleep(3)
        # click Network
        Network = self.webdriver.find_element(By.XPATH,
                                              '//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
        Network.click()
