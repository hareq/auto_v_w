__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
import Read_datebase,Reception
from Reception import Reception
from Backstage import Backstage

class Reception_start:

    def url_start(self,driver):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        mylogin = Reception()
        mylogin.url(table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value,driver)

    def url_start_other(self,driver,url):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        mylogin = Reception()
        urlall = table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value + '/'+url
        mylogin.url(urlall,driver)


