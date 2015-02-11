# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import os,sys
from selenium import webdriver
import time
from Commons.lib import Read_datebase
import traceback


class Invest:

    def invest(self,url,money,driver):
      money = int(money)
      url=url+'project/list'
      #url=url+'project/list/category/1/type/0/status/1'
      #url=url+'project/list/category/2/type/0/status/1'

      driver.get(url)
      driver.find_element_by_class_name("btn-primary").click()
      driver.find_element_by_name("money").send_keys(str(money))
      driver.find_element_by_id("loancontract").click()
      try:
          driver.find_element_by_id("pledgecontract").click()
      except:
          1 ==1
      driver.find_element_by_class_name("btn-primary").click()
      alert = driver.switch_to_alert()
      alert.accept()

