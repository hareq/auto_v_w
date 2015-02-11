__author__ = 'guyanhua'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from Commons.lib import Read_datebase
from Module.Common import Browser
from Module.Front import Module_Front_Url,Invest,Module_Front_Login
from Module.Backstage import Module_Backstage_Url,Module_Backstage_Login,Module_Financing
import threading
from time import ctime,sleep
import Config.common_config
browser = Browser.browser()
module_front_Url = Module_Front_Url.front_url()
module_Backstage_Url = Module_Backstage_Url.Backstage_url()
module_backstage_login = Module_Backstage_Login.module_backstage_login()
module_financing = Module_Financing.financing()
Invest = Invest.invest_start()
Login = Module_Front_Login.module_front_login()
common_config = Config.common_config
class Test_F_Login(unittest.TestCase):

    def test_f_login_urla(self,driver):
        module_Backstage_Url.url_start(driver,'')

    def test_f_login_urlb(self):
        driver = self.driver
        driver.get(self.base_url + "/lender/add_tengfei")
        driver.find_element_by_id("focusedInput").clear()
        driver.find_element_by_id("focusedInput").send_keys(u"身份证;营业执照")

    def test_f_login(self):
        driver = self.driver
        driver.get(self.base_url + "/lender/add_tengfei")
        driver.find_element_by_id("focusedInput").clear()
        driver.find_element_by_id("focusedInput").send_keys(u"身份证;营业执照")

    def test_f_logout(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

if __name__ == "__main__":
    unittest.main()
