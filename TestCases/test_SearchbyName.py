from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomerPage
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time
import pytest

class Test_005_SearchCustomerbyName:
    baseURL = ReadConfig.getApplicationsURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerbyName(self, setup):
        self.log.info("********* Test_005_SearchCustomerbyName ********")
        self.log.info("********* Verifying Login ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.log.info("********* Login Successful ********")
        self.log.info("********* Starting Search Customer Test ********")

        self.addCust = AddCustomerPage(self.driver)
        self.addCust.clickonCustomerMenu()
        self.addCust.clickonCustomerMenuItem()

        self.log.info("********* Searching Customer by Name ********")

        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setFirstName("Arthur")
        self.searchCust.setLastName("Holmes")
        self.searchCust.clicksearch()
        time.sleep(3)
        status = self.searchCust.SearchbyName("Arthur Holmes")
        assert True == status
        self.log.info("********* Test_005_SearchCustomer By Name Finished ********")
        self.driver.close();
