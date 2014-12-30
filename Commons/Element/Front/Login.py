# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import os,sys
from selenium import webdriver
import time
import Read_datebase

class Login:
	#driver = None
	# def __init__(self,driver):
	# 	self.driver = driver

    def url(self,url,driver):
      driver.get(url)

    def login(self,url,user,password,driver):
      url = url+"user/login"
      driver.get(url)
      driver.find_element_by_id("username").send_keys(user)
      driver.find_element_by_id("password").send_keys(password)
      driver.find_element_by_class_name("btn-primary").click()

    def logout(self,driver,url):
      url = url+"user/logout"
      driver.get(url)
