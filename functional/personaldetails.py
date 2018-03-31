"""Temp info."""
from models.personaldetails import PersonalDetails


class UserDetailsAssistant:

    def __init__(self, conf):
        self.conf = conf

    def open_user_edit_form(self):
        """
        Open Edit Account form.
        """
        driver = self.conf.driver
        driver.find_element_by_xpath("//div[@id='content']//a[.='Edit Account']").click()

    def change_data_in_text_fields(self, form_field: str, data: str):
        """
        Enter the data in the textfield.

        :param form_field: textfield's id.
        :param data: data entered in the textfield.
        """
        driver = self.conf.driver
        if data is not None:
            driver.find_element_by_id(form_field).click()
            driver.find_element_by_id(form_field).clear()
            driver.find_element_by_id(form_field).send_keys(data)

    def edit(self, user_data: PersonalDetails):
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        """
        driver = self.conf.driver
        self.open_user_edit_form()
        self.change_data_in_text_fields("input-firstname", user_data.firstname)
        self.change_data_in_text_fields("input-lastname", user_data.lastname)
        self.change_data_in_text_fields("input-email", user_data.email)
        self.change_data_in_text_fields("input-telephone", user_data.telephone)
        driver.find_element_by_xpath("//form[@class='form-horizontal']/div/div[2]/input").click()

