from selenium.webdriver.common.by import By

FIRSTNAME_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[1]/div/div")
LASTNAME_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[2]/div/div")
ADDRESS1_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[4]/div/div")
CITY_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[6]/div/div")
POSTCODE_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[7]/div/div")
REGION_ERROR = (By.XPATH, "//form[@class='form-horizontal']/fieldset/div[9]/div/div")

FIRSTNAME_FIELD = (By.ID, "input-firstname")
LASTNAME_FIELD = (By.ID, "input-lastname")
COMPANY_FIELD = (By.ID, "input-company")
ADDRESS1_FIELD = (By.ID, "input-address-1")
ADDRESS2_FIELD = (By.ID, "input-address-2")
CITY_FIELD = (By.ID, "input-city")
POSTCODE_FIELD = (By.ID, "input-postcode")
COUNTRY_OPTION = (By.ID, "input-country")
REGION_OPTION = (By.ID, "input-zone")

CONTINUE_BUTTON = (By.XPATH, "//form[@class='form-horizontal']/div/div[2]/input")
