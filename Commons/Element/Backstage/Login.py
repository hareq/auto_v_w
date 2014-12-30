# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import sys
from selenium import webdriver
import time,re
import Read_datebase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Backstage:

    def logout(self,driver,url):
      url = url+"default/logout"
      driver.get(url)

    def login(self,url,user,password,driver):
      driver.get(url)
      #print driver.title
      driver.find_element_by_name("user_name").click()
      driver.find_element_by_name("user_name").clear()
      driver.find_element_by_name("user_name").send_keys(user)
      driver.find_element_by_name("password").click()
      driver.find_element_by_name("password").clear()
      driver.find_element_by_name("password").send_keys(password)
      driver.find_element_by_name("submit").click()


