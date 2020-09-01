import time
from selenium.webdriver.support.ui import Select


class AddCustomerPage:
    lnkCustomers_mainmenu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomer_menu_item_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    btn_gender_male_id = "Gender_Male"
    btn_gender_female_id = "Gender_Female"
    txt_dateofbirth_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    btn_istaxexempt_xpath = "//input[@id='IsTaxExempt']"
    txt_newsletter_xpath = "//div[9]//div[2]//div[1]//div[1]//div[1]"
    lst_item_yourstorename_xpath = "//li[contains(text(),'Your store name')]"
    lst_item_teststore2_xpath = "//li[contains(text(),'Your store name')]"
    txt_CustomerRoles_xpath= "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    lst_item_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lst_item_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lst_item_guests_xpath = "//li[contains(text(),'Guests')]"
    lst_item_registered_xpath = "//li[contains(text(),'Registered')]"
    lst_item_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_down_managerofvendors_xpath = "//select[@name='VendorId']"
    drp_down_novendor_xpath = "//option[contains(text(),'Not a vendor')]"
    drp_down_vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    drp_down_vendor2_xpath = "//option[contains(text(),'Vendor 2')]"
    txt_admincomment_xpath = "//textarea[@name='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_mainmenu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_item_xpath).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.btn_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.btn_gender_female_id).click()
        else:
            self.driver.find_element_by_id(self.btn_gender_male_id).click()

    def enterDOB(self,dob):
        self.driver.find_element_by_xpath(self.txt_dateofbirth_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element_by_xpath(self.txt_company_name_xpath).send_keys(companyname)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_administrator_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_registered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_vendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lst_item_guests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_down_managerofvendors_xpath))
        drp.select_by_visible_text(value)

    def setNewsletter(self):
        self.driver.find_element_by_xpath(self.txt_newsletter_xpath).click()
        # drp = Select(self.driver.find_element_by_xpath(self.txt_newsletter_xpath))
        # drp.select_by_visible_text(value)
        self.driver.find_element_by_xpath(self.lst_item_teststore2_xpath).click()

    def setAdminComment(self,comment):
        self.driver.find_element_by_xpath(self.txt_admincomment_xpath).send_keys(comment)
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()