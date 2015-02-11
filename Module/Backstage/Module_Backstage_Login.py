__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
from Config import common_config
from Commons.lib import Read_datebase
from Commons.Element.Backstage import Element_Backstage_Login


element_backstage_login = Element_Backstage_Login.module_backstage_login()
class module_backstage_login:

    def login_start(self,driver,row):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('financing')
        user=table.cell(row,Read_datebase.find_colum(file,'financing','Login_user')).value
        password=table.cell(row,Read_datebase.find_colum(file,'financing','Login_password')).value
        table = data.sheet_by_name('public')
        element_backstage_login.login(table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value,user,password,driver)

    def logout_start(self,driver):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        element_backstage_login.logout(driver,table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value)

