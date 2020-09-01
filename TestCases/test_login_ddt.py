import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationsURL()
    path = "./TestData/LoginData.xlsx"

    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.log.info("********* Test_001_ddt_Login ********")
        self.log.info("********* Verifying Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        lst_status = []
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            page_title = self.driver.title
            if page_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.lp.clickLogout()
                    self.log.info("********* Passed ********")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.log.info("********* Failed ********")
                    lst_status.append("Fail")
            elif page_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.log.info("********* Failed ********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.log.info("********* Passed ********")

        if "Fail" not in lst_status:
            self.log.info("Login DDT Test Passed")
            self.driver.close()
            assert True
        else:
            self.log.info("*********** Login DDT Test Failed ***********")
            self.driver.close()
            assert False

        self.log.info("*********** End of DDT Test ************")
        self.log.info("*********** Test_002_DDT_Login Completed ************")
