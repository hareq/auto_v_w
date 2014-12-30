__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
import Read_datebase,Reception
from Reception import Reception
from Backstage import Backstage


class public:
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

    def browser_start(self):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        return self.browser(table.cell(2,Read_datebase.find_colum(file,'public','browser')).value)

    def browser_close(self):
        self.driver.close()

    def start_url(self,driver,url):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        return self.browser(table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value)