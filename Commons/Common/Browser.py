__author__ = 'guyanhua'

import sys
from selenium import webdriver

class browser:
    def browser(self,browser):
       if browser=='Chrome':
          driver=webdriver.Chrome()
          return driver
       if browser=='Ie':
          driver=webdriver.Ie()
          return driver
       if browser=='Firefox':
          driver=webdriver.Firefox()
          return driver
       if browser=='Opera':
          driver=webdriver.Opera()
          return driver

