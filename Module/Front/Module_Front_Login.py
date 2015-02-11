__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
from Commons.lib import Read_datebase
from Commons.Element.Front import Login
from Config import common_config
mylogin = Login.Login()

class module_front_login:

    def login_start(self,driver,row):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('invest')
        user=table.cell(row,Read_datebase.find_colum(file,'invest','user')).value
        password=table.cell(row,Read_datebase.find_colum(file,'invest','password')).value
        table = data.sheet_by_name('public')
        mylogin.login(table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value,user,password,driver)

    def logout_start(self,driver):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        mylogin.logout(driver,table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value)


