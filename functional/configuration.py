"""
Contains Configuration class.
"""

from selenium.webdriver.firefox.webdriver import WebDriver
from functional.session import SessionAssistant
from functional.addressbook import AddressBookAssistant
from functional.personaldetails import UserDetailsAssistant


class Configuration:
    """Contains references and auxiliary methods."""

    def __init__(self):
        self.driver = WebDriver()
        self.session = SessionAssistant(self)
        self.address_book = AddressBookAssistant(self)
        self.personal_details = UserDetailsAssistant(self)

    def open_login_page(self):
        """
        Open login page.
        """
        driver = self.driver
        driver.get("http://localhost/opencart/index.php?route=account/login")

    def exit_fixture(self):
        """
        Quit WebDriver.
        """
        self.driver.quit()
