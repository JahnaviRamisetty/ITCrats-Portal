import pytest

from pageobjects.portal_login import Login
from utilites.readproperties import ReadConfig
from utilites.customlogger import Loggen

class Testlogin:
    url=ReadConfig.getApplicationURL()
    user=ReadConfig.getusername()
    pswd=ReadConfig.getpassword()
    Logger=Loggen.loggen()

    #@pytest.fixture(scope="function")
    def test_logintopage(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.username(self.user)
        self.lp.password(self.pswd)
        self.lp.click_login()
        self.lp.click_dashboard()



