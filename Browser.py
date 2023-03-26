import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException


class Browser:
    def __init__(self, profile_path, metamask):
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={profile_path}")
        options.add_argument('--profile-directory=Profile 1')
        self.metamask = metamask
        self.webdriver = webdriver.Chrome(chrome_options=options)

    def open_game(self):
        self.metamask.login(self.webdriver)

    def connect_mm(self, game_url):
        self.webdriver.get(game_url)
        time.sleep(3)
        # connect MM and add networks
        try:
            # find button ConnectWallet
            time.sleep(3)
            self.webdriver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div[1]/div[2]/dl/div[2]/div[1]/dd/ul/li/div[2]/a').click()
            # finde MM
            time.sleep(3)
            Metamask_Button_Shadow = self.webdriver.find_element(By.CSS_SELECTOR,
                                                                 'body > onboard-v2')
            shadow_host = self.webdriver.find_element(By.CSS_SELECTOR,
                                               'body > onboard-v2')
            shadow_root = self.webdriver.execute_script('return arguments[0].shadowRoot', shadow_host)
            shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'section > div > div > div > div > div > div > '
                                                                       'div > div.scroll-container.svelte-1n0mo1q > '
                                                                       'div.svelte-1n0mo1q > div > div > button')
            shadow_content.click()
            print(shadow_content.text)
            self.webdriver.switch_to.window(self.webdriver.window_handles[1])
            print("Second window title = " + self.webdriver.title)
            time.sleep(3)
            # click Next
            Next = self.webdriver.find_element(By.CSS_SELECTOR,
                                               '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')
            Next.click()
            time.sleep(3)
            # click Connect
            Connect = self.webdriver.find_element(By.XPATH, '//*[@id="app-content"]/div/'
                                                            'div[2]/div/div[2]/div[2]/div['
                                                            '2]/footer/button[2]')
            Connect.click()
            time.sleep(3)

        except IndexError:
            print('Second window dont exist')
