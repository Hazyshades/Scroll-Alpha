from Browser import Browser
from Metamask import MetaMask


def main():
    site_url = 'https://scroll.io/alpha'
    profile_path = r"C:\Users\leo\AppData\Local\Google\Chrome\User Data"
    extension_id = "nkbihfbeogaeaoehlefnkodbefgpgknn"
    metamask_password = "Slayer233189"
    metamask = MetaMask(extension_id, metamask_password)
    browser = Browser(profile_path, metamask)
 #   try:
    browser.open_game()
    browser.connect_mm(site_url)
  #  browser.swap()
     #   browser.work()
  #  finally:
     #   browser.quit()


if __name__ == "__main__":
    main()

