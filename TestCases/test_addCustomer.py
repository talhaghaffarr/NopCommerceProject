import pytest
import time

from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomerPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationsURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepage_title(self, setup):
        self.log.info("********* Test_003_AddCustomer ********")
        self.log.info("********* Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("********* Login Successful ********")
        self.log.info("********* Starting Add Customer Test ********")

        self.addCust = AddCustomerPage(self.driver)
        self.addCust.clickonCustomerMenu()
        self.addCust.clickonCustomerMenuItem()
        self.addCust.clickAddNew()

        self.log.info("********* Entering new  Customer Details ********")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        # self.addCust.setCustomerRoles("Guests")
        self.addCust.setFirstName("Talha")
        self.addCust.setLastName("Ghaffar")
        self.addCust.setGender("Female")
        self.addCust.enterDOB("1/1/1990")
        self.addCust.setCompanyName("AdvanceQA")
        self.addCust.setNewsletter()
        self.addCust.setCustomerRoles("Vendors")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminComment("Hello, This is a new customer")
        self.addCust.clickOnSave()

        self.log.info("********* Saving new  Customer Details ********")
        self.log.info("******** Add customer validation started ********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.log.info("********* Add Customer Test Passed ********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_addCustomer.png")
            self.log.error("********* Add Customer Test Failed ********")
            assert False

        self.driver.close()
        self.log.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
