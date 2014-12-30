__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
import Read_datebase,Reception
from Reception import Reception
from Backstage import Backstage

class Reception_start:

    def invest_start(self,driver,row):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        mylogin = Reception()
        table = data.sheet_by_name('invest')
        money=table.cell(row,Read_datebase.find_colum(file,'invest','money')).value
        table = data.sheet_by_name('public')
        mylogin.invest(table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value,money,driver)

