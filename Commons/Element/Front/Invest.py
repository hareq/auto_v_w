# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import os,sys
from selenium import webdriver
import time
from Commons.lib import Read_datebase

class Invest:

    def invest(self,url,money,driver):
      money = int(money)
      url=url+'project/list'
      driver.get(url)
      driver.find_element_by_class_name("btn-primary").click()
      driver.find_element_by_name("money").send_keys(str(money))
      driver.find_element_by_class_name("btn-primary").click()
      alert = driver.switch_to_alert()
      alert.accept()

