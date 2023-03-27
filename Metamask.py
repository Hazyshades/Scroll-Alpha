import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException
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

        # change Eng lang

        web_driver.get(f"chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/general")
        time.sleep(5)
        web_driver.find_element(By.XPATH, "//*[contains(text(), 'English')]").click()

        web_driver.get(f"chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/advanced")
        time.sleep(2)

        allow_test_networks = web_driver.find_element(By.XPATH,
                                                      '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/label/div[1]/div[1]/div[2]')

        label_off = web_driver.find_element(By.XPATH,
                                            '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/label/div[2]/span[1]')

        print(label_off.text)

        if label_off.text == 'OFF':
            allow_test_networks.click()
            time.sleep(3)

        current_network = web_driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span')
        current_network.click()
        time.sleep(3)

        Goerli_network = web_driver.find_element(By.XPATH, "//*[contains(text(), 'Goerli')]")
        Goerli_network.click()
        time.sleep(3)

    def add_networks(self, web_driver):
        try:
            net_name = 'Scroll Alpha Testnet'
            rpc = 'https://alpha-rpc.scroll.io/l2'
            chain_id = 534353
            symbol = 'ETH'
            explorer = 'https://blockscout.scroll.io'

            web_driver.get(
                f"chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
            time.sleep(3)
            web_driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div['
                                              '2]/div/div[2]/div[1]/label/input').send_keys(net_name)
            web_driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div['
                                    '2]/div[2]/label/input').send_keys(rpc)
            web_driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div['
                                    '2]/div[3]/label/input').send_keys(chain_id)
            web_driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div['
                                    '2]/div[4]/label/input').send_keys(symbol)
            web_driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div['
                                    '2]/div[5]/label/input').send_keys(explorer)
            time.sleep(3)

            web_driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div['
                                    '3]/button[2]').click()
        except ElementClickInterceptedException:
            print('Network already added')
