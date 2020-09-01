import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationsURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()

    log = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.log.info("********* Test_001_Login ********")
        self.log.info("********* Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        if page_title == "Your store. Login":
            assert True
            self.driver.close()
            self.log.info("********* Home Page Title Test Passed ********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homepage_title.png")
            self.driver.close()
            self.log.info("********* Home Page Title Test Failed ********")
            self.log.error("********* Home Page Title Test Failed ********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.log.info("********* Verifying Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        page_title = self.driver.title
        if page_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.log.info("********* Login Test Passed ********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.log.info("********* Login Test Failed ********")
            self.log.error("********* Login Test Failed ********")
            assert False
