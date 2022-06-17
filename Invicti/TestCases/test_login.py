import pytest
#import time
#from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseurl = "http://demo.testfire.net/"
    username = "admin"
    password = "admin"


    def test_home_page_title(self,setup):
        self.driver= setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Altoro Mutual":

            assert True
            print("Home Page is verified")
        else:
            assert False


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.clickLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.setlogin()
        self.lp.setdrpdwn()
        self.lp.clickLogout()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Altoro Mutual":
            assert True
        else:
            assert False
#from selenium import webdriver
#from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
#import time

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("http://demo.testfire.net/")
#driver.maximize_window()
#time.sleep(2)

#sign_loginin = driver.find_element(By.XPATH,'//*[@id="LoginLink"]/font')
#sign_loginin.click()
#time.sleep(3)

#username_textbox = driver.find_element(By.ID,'uid')
#username_textbox.send_keys("admin")

#password_textbox = driver.find_element(By.NAME,'passw')
#password_textbox.send_keys("admin")
#time.sleep(2)

#login_btn = driver.find_element(By.NAME,'btnSubmit')
#login_btn.click()
#time.sleep(2)

#drp_downbtn = driver.find_element(By.NAME,'listAccounts')
#drp_downbtn.click()
#time.sleep(2)

#sign_logoff = driver.find_element(By.XPATH,'//*[@id="LoginLink"]/font')
#sign_logoff.click()
#time.sleep(3)
