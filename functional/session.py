"""
Contain SessionAssistant hat provide help with Login and Logout.
"""


class SessionAssistant:
    """Include methods for Login and Logout."""

    def __init__(self, conf):
        self.conf = conf

    def login(self, email: str, password: str):
        """
        Login user into Account page.

        :param email: user's email.
        :param password: user's password.
        """
        driver = self.conf.driver
        self.conf.open_login_page()
        self.inputted_data("input-email", email)
        self.inputted_data("input-password", password)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def inputted_data(self, field: str, data: str):
        """
        Set data into textfield on Login page.

        :param field: field's id.
        :param data: data to enter into the text field.
        """
        driver = self.conf.driver
        driver.find_element_by_id(field).click()
        driver.find_element_by_id(field).clear()
        driver.find_element_by_id(field).send_keys(data)

    def logout(self):
        """
        Logout from user's account.
        """
        driver = self.conf.driver
        driver.find_element_by_xpath("//ul[@class='list-inline']//a[.=' My Account ']").click()
        driver.find_element_by_xpath("//ul[@class='list-inline']//a[.='Logout']").click()
