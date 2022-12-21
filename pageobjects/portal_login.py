from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base_driver import Basedriver

class Login(Basedriver):

    username_id="user"
    password_id="pass"
    login_id="wp-submit"
    login="//input[@id='wp-submit']"
    dashboard="//a[@class='fas fa-tachometer-alt']"

    def __init__(self,driver):
        self.driver=driver

    def username(self,user_name):
        self.driver.find_element(By.ID,self.username_id).send_keys(user_name)

    def password(self,passwrd):
        self.driver.find_element(By.ID,self.password_id).send_keys(passwrd)

    def click_login(self):
        self.wait_until_element_is_clickabale(By.XPATH,self.login).click()

    def click_dashboard(self):
        self.wait_until_element_is_clickabale(By.XPATH,self.dashboard).click()






