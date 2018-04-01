from selenium.webdriver.common.by import By

EDIT_BUTTON = (By.XPATH, "//td[@class='text-right']//a[.='Edit']")
DELETE_BUTTON = (By.XPATH, "//td[@class='text-right']//a[.='Delete']")
NEW_ADDRESS_BUTTON = (By.XPATH, "//div[@id='content']//a[.='New Address']")
ALERT_MESSAGE = (By.XPATH, "//div[@id='account-address']/div[1]")
