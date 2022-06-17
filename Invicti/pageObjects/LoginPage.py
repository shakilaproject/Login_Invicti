from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    sign_logiin_xpath = '//*[@id="LoginLink"]/font'
    username_textbox_id = "uid"
    password_textbox_name = "passw"
    login_bt_name = 'btnSubmit'
    drp_downbtn_name = 'listAccounts'
    sign_logoff_xpath = '//*[@id="LoginLink"]/font'

    def __init__(self,driver):
        self.driver=driver

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.sign_logiin_xpath).click()


    def setUserName(self, username):
        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.password_textbox_name).clear()
        self.driver.find_element(By.ID,self.password_textbox_name).send_keys(password)

    def setlogin(self):
        self.driver.find_element(By.NAME, self.login_bt_name).click()

    def setdrpdwn(self):
        self.driver.find_element(By.ID,self.drp_downbtn_name).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.sign_logoff_xpath).click()