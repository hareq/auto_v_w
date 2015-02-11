__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
from Config import common_config
from Commons.lib import Read_datebase
from Commons.Common import Browser
#Read_datebase = Read_datebase()
Browser = Browser.browser()


class browser:
    def browser_start(self):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        return Browser.browser(table.cell(2,Read_datebase.find_colum(file,'public','browser')).value)

    def browser_close(self,driver):
        driver.close()

