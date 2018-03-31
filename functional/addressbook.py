"""
Contains AddressBookAssistant class that provides help with
interacting with the Address Book page elements.
"""

import re
from typing import List, Tuple
from selenium.webdriver.support.ui import Select
from models.addressbook import AddressBook


class AddressBookAssistant:
    """Used to work with the Address Book page."""

    def __init__(self, conf):
        self.conf = conf

    def create(self, address: AddressBook):
        """
        Open Address Book page, then open and fill Add Address form
        and submit creation.

        :param address: object with parameters for fields in Add Address form.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        self.open_form_page()
        self.fill_address_form(address)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def open_form_page(self):
        """
        Open Add Address form on Address Book page.
        """
        driver = self.conf.driver
        driver.find_element_by_link_text("New Address").click()

    def fill_address_form(self, address: AddressBook):
        """
        Fill fields with data in Add Address form.

        :param address: object with parameters for fields.
        """
        self.change_text_field_data("input-firstname", address.first_name)
        self.change_text_field_data("input-lastname", address.last_name)
        self.change_text_field_data("input-company", address.company)
        self.change_text_field_data("input-address-1", address.address_1)
        self.change_text_field_data("input-address-2", address.address_2)
        self.change_text_field_data("input-city", address.city)
        self.change_text_field_data("input-postcode", address.post_code)
        self.change_drop_list_data("input-country", address.country)
        self.change_drop_list_data("input-zone", address.region_state)

    def change_drop_list_data(self, ddlist_option: str, value: AddressBook):
        """
        Select option in dropdown list in Add Address form.

        :param ddlist_option: option's id in dropdown list.
        :param value: option's text in dropdown list.
        """
        if value is not None:
            driver = self.conf.driver
            data_select = Select(driver.find_element_by_id(ddlist_option))
            data_select.select_by_visible_text(value)

    def change_text_field_data(self, field_name: str, value: AddressBook):
        """
        Set text into Add Address form field.

        :param field_name: field's id in Add Address form.
        :param value: field's text in Add Address form.
        """
        driver = self.conf.driver
        if value is not None:
            driver.find_element_by_id(field_name).click()
            driver.find_element_by_id(field_name).clear()
            driver.find_element_by_id(field_name).send_keys(value)

    def open_address_book_page(self):
        """
        Open Address Book page.

        :return: None if we still on Address Book page.
        """
        driver = self.conf.driver
        if driver.current_url.endswith("account/address"):
            return
        driver.find_element_by_link_text("Address Book").click()

    def delete_record_by_index(self, index: int):
        """
        Delete Address Book entry from Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on Address Book page.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Delete']")[index].click()

    def edit_record_by_index(self, updated_values: AddressBook, index: int):
        """
        Open Address Book page, then open already existing address entry,
        fill Add Address form with new data and submit changes.

        :param updated_values: object with parameters for fields in Add Address form.
        :param index: position of address in list on Address Book page.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        self.open_edit_page_by_position(index)
        self.fill_address_form(updated_values)
        driver.find_element_by_xpath("//form[@class='form-horizontal']/div/div[2]/input").click()

    def open_edit_page_by_position(self, position: int):
        """
        Edit address book entry from the Address Book page
        by it's positional index.

        :param position: positional index of address entry
        in list of addresses on the Address Book page.
        """
        driver = self.conf.driver
        driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Edit']")[position].click()

    def get_content_info_from_list(self) -> List[AddressBook]:
        """
        Get text of each individual address record in table on the Address Book page,
        filter and convert it into object, append them to list and return it.

        :return: list of objects.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        address_list = []
        for line in driver.find_elements_by_xpath('//*[@id="content"]//table/tbody//td[1]'):
            content = re.sub(r'\s', '', line.text)
            address_list.append(AddressBook(content=content))
        return address_list

    def get_content_info_from_form(self, address_obj: AddressBook) -> AddressBook:
        """
        Get text from object, filter and convert it into another object.

        :param address_obj: object that we used to create/edit Add Address form.
        :return: object with filtered text.
        """
        self.open_address_book_page()
        info_from_object = []
        for attr in address_obj.__dict__.items():
            if attr[1] is not None:
                info_from_object.append(attr[1])
        content = re.sub(r'\s', '', "".join(info_from_object))
        return AddressBook(content=content)

    def records_count(self) -> int:
        """
        Count the number of address records on the Address Book page.

        :return: number of records.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        return len(driver.find_elements_by_xpath(
            "//div[@class='table-responsive']//a[.='Edit']"))

    def get_content_info_by_index(self, index: int) -> AddressBook:
        """
        Get text from address record  by index in table on the Address Book page,
        filter and convert it into object.

        :return: object.
        """
        driver = self.conf.driver
        self.open_address_book_page()
        info = driver.find_elements_by_xpath(
            '//*[@id="content"]//table/tbody//td[1]')[index].text
        content = re.sub(r'\s', '', info)
        return AddressBook(content=content)

    def get_alert_message(self) -> str:
        """
        Receive a message from the address book after adding,
        editing or deleting a record.

        :return: text message.
        """
        driver = self.conf.driver
        return driver.find_element_by_xpath("//div[@id='account-address']/div[1]").text

    def get_form_error_messages(self) -> Tuple[str, str, str, str, str, str]:
        driver = self.conf.driver
        errors = driver.find_elements_by_css_selector(".text-danger")
        messages = []
        for error in errors:
            messages.append(error.text)
        firstname_error = messages[0]
        lastname_error = messages[1]
        address1_error = messages[2]
        city_error = messages[3]
        postcode_error = messages[4]
        region_error = messages[5]
        return (firstname_error, lastname_error,
                address1_error, city_error,
                postcode_error, region_error)
