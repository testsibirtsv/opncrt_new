"""
Contain tests to edit address book records.
"""

import pytest
from models.addressbook import AddressBook


def test_edit_address_by_index(conf, index=2):
    record = AddressBook(first_name="edited_firstname",
                         last_name="edited_lastname",
                         company="edited_company",
                         address_1="edited_address1",
                         address_2="edited_address2",
                         city="edited_city",
                         post_code="e_postcode",
                         country="Ukraine",
                         region_state="Ternopil's'ka Oblast'")
    while conf.address_book.records_count() < index + 1:
        conf.address_book.create(record)
    with pytest.allure.step("Select an address book entry to edit by index %d." % index):
        conf.address_book.edit_record_by_index(record, index)
    with pytest.allure.step("Take information from edited address record from Add Address form."):
        info_from_edited_address = conf.address_book.get_content_info_from_form(record)
    with pytest.allure.step("Take information about edited address on Address Book page."):
        updated_info_from_address_list = conf.address_book.get_content_info_by_index(index)
    with pytest.allure.step("Retrieving info about successfully updated address."):
        assert conf.address_book.get_alert_message() == 'Your address has been successfully updated'
    with pytest.allure.step("Compare info about edited address."):
        assert info_from_edited_address == updated_info_from_address_list
