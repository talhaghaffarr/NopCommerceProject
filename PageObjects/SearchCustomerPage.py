from selenium.webdriver.support.ui import Select


class SearchCustomer:
    txtSearchEmail_id = "SearchEmail"
    txtSearchFirstName_id = "SearchFirstName"
    txtSearchLastName_id = "SearchLastName"
    drpSearchMonth_id = "SearchMonthOfBirth"
    drpSearchDay_id = "SearchDayOfBirth"
    # txtSearchCompany_id = "SearchCompany"
    # txtSearchIpAddress_id = "SearchIpAddress"
    btnSearch_id = "search-customers"
    tblElements_xpath = "//table[@role='grid']"
    tbl_xpath = "//table[@id='customers-grid']"
    tblRow_xpath = "//table[@id='customers-grid']//tbody//tr"
    tblColumn_xpath = "//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtSearchEmail_id).clear()
        self.driver.find_element_by_id(self.txtSearchEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element_by_id(self.txtSearchFirstName_id).clear()
        self.driver.find_element_by_id(self.txtSearchFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_id(self.txtSearchLastName_id).clear()
        self.driver.find_element_by_id(self.txtSearchLastName_id).send_keys(lastname)

    # def setDOB(self, month, day):
    #     drp = Select(self.driver.find_element_by_xpath(self.drpSearchMonth_id))
    #     drp.select_by_visible_text(month)
    #     drp2 = Select(self.driver.find_element_by_xpath(self.drpSearchDay_id))
    #     drp2.select_by_visible_text(day)

    def getNoofRows(self):
        return len(self.driver.find_elements_by_xpath(self.tblRow_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tblColumn_xpath))

    def SearchbyEmail(self,email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            emailed = table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(r)+"]/td[2]").text
            if emailed == email:
                flag = True
                break
        return flag

    def SearchbyName(self, name):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            Searchname = table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr[" + str(r) + "]/td[3]").text
            if Searchname == name:
                flag = True
                break
        return flag

    def clicksearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()