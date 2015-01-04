# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import sys
from selenium import webdriver
import time,re
from Commons.lib import Read_datebase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class financing:

    def financing(self,url,uername,purpose,pro_type,bank,moneyf,dayormauthtype,dayormauth,rate,end_time,service_fee,deposit,activity,estate_name,build_size,limit,p_price,c_price,driver):
      url = url+"lender"
      moneyf = int(moneyf)
      dayormauth = int(dayormauth)
      rate = int(rate)
      end_time = int(end_time)
      service_fee = int(service_fee)
      build_size = int(build_size)
      driver.get(url)
      driver.find_element_by_css_selector("p").click()
      driver.find_element_by_id("user_name").clear()
      driver.find_element_by_id("user_name").send_keys(uername)
      driver.find_element_by_id("find_user_info").click()
      if pro_type =="t":
          Select(driver.find_element_by_name("category")).select_by_visible_text(u"腾飞系列")
      if pro_type =="z":
          Select(driver.find_element_by_name("category")).select_by_visible_text(u"钻石系列")
      driver.find_element_by_id("focusedInput").clear()
      driver.find_element_by_id("focusedInput").send_keys(bank)
      driver.find_element_by_name("money").clear()
      driver.find_element_by_name("money").send_keys(moneyf)
      if purpose =="公司经营周转":
          Select(driver.find_element_by_id("selectError3")).select_by_visible_text(u"公司经营周转")
      if purpose =="网站经营周转":
          Select(driver.find_element_by_id("selectError3")).select_by_visible_text(u"网店经营周转")
      if purpose =="个人消费周转":
          Select(driver.find_element_by_id("selectError3")).select_by_visible_text(u"个人消费周转")
      if purpose =="个人消费供应链融资":
          Select(driver.find_element_by_id("selectError3")).select_by_visible_text(u"个人消费供应链融资")
      if purpose =="网络借款体验":
          Select(driver.find_element_by_id("selectError3")).select_by_visible_text(u"网络借款体验")
      if activity == 'yes':
          driver.find_element_by_name("activity_id[]").click()
           #Select(driver.find_element_by_name("activity_id")).select_by_visible_text(u"2014年11月投标即送")
      if activity == 'no':
          1 == 1
           #Select(driver.find_element_by_name("activity_id")).select_by_visible_text(u"非活动标")
      if deposit == "是":
          driver.find_element_by_xpath("(//div[@id='uniform-day_click']/span)[1]").click()
      if deposit == "否":
          driver.find_element_by_xpath("(//div[@id='uniform-day_click']/span)[2]").click()
      driver.find_element_by_css_selector("#uniform-day_click > span").click()
      driver.find_element_by_id(dayormauthtype).click()
      driver.find_element_by_name("term_num").clear()
      driver.find_element_by_name("term_num").send_keys(dayormauth)
      driver.find_element_by_name("money_rate").clear()
      driver.find_element_by_name("money_rate").send_keys(rate)
      driver.find_element_by_name("use_year").clear()
      limit = int(limit)
      driver.find_element_by_name("use_year").send_keys(limit)
      driver.find_element_by_name("evaluate_price").clear()
      p_price = int(p_price)
      driver.find_element_by_name("evaluate_price").send_keys(p_price)
      driver.find_element_by_name("reference_price").clear()
      c_price = int(c_price)
      driver.find_element_by_name("reference_price").send_keys(c_price)
      driver.find_element_by_name("end_time").clear()
      driver.find_element_by_name("end_time").send_keys(end_time)
      driver.find_element_by_name("service_fee").clear()
      driver.find_element_by_name("service_fee").send_keys(service_fee)
      driver.find_element_by_name("estate_name").clear()
      driver.find_element_by_name("estate_name").send_keys(estate_name)
      driver.find_element_by_name("build_size").clear()
      driver.find_element_by_name("build_size").send_keys(build_size)
      driver.find_element_by_css_selector("input.btn.btn-primary").click()
      #self.driver.close()


