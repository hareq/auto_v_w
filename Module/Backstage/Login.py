__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
import Read_datebase,Reception
from Reception import Reception
from Backstage import Backstage

class Backstage_start:

    def login_start(self,driver,row):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        mylogin = Backstage()
        table = data.sheet_by_name('financing')
        user=table.cell(row,Read_datebase.find_colum(file,'financing','Login_user')).value
        password=table.cell(row,Read_datebase.find_colum(file,'financing','Login_password')).value
        table = data.sheet_by_name('public')
        mylogin.login(table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value,user,password,driver)

    def logout_start(self,driver):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        mylogin = Backstage()
        table = data.sheet_by_name('public')
        mylogin.logout(driver,table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value)

