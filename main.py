from Browser import Browser
from Metamask import MetaMask


def main():
    site_url = 'https://scroll.io/alpha/bridge'
    profile_path = r"C:\Users\leo\AppData\Local\Google\Chrome\User Data"
    profile_number = r'Profile 1'
    extension_id = "nkbihfbeogaeaoehlefnkodbefgpgknn"
    network_name_goerli = 'Goerli'
    metamask_password = "***"
    metamask = MetaMask(extension_id, metamask_password, network_name_goerli)
    browser = Browser(profile_path, profile_number, metamask)

    browser.login()

    browser.add_networks()

    browser.allow_test_network()

    browser.change_current_networks()

    browser.connect_mm(site_url)

    browser.bridge_to_scroll()


if __name__ == "__main__":
    main()
