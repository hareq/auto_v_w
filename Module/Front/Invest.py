__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
from Config import common_config
from Commons.lib import Read_datebase
from Commons.Element.Front import Invest

mylogin = Invest.Invest()

class invest_start:

    def invest_start(self,driver,row):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('invest')
        money=table.cell(row,Read_datebase.find_colum(file,'invest','money')).value
        table = data.sheet_by_name('public')
        mylogin.invest(table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value,money,driver)

