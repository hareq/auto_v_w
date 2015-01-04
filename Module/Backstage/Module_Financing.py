__author__ = 'guyanhua'

import sys
from selenium import webdriver
import time
from Commons.lib import Read_datebase
from Commons.Element.Backstage import Element_Financing

element_financing = Element_Financing.financing()

class financing:
    def financing(self,driver,row):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('financing')
        uername = table.cell(row,Read_datebase.find_colum(file,'financing','username')).value
        bank = table.cell(row,Read_datebase.find_colum(file,'financing','bank')).value
        moneyf = table.cell(row,Read_datebase.find_colum(file,'financing','moneyf')).value
        dayormauthtype = table.cell(row,Read_datebase.find_colum(file,'financing','dayormauthtype')).value
        dayormauth = table.cell(row,Read_datebase.find_colum(file,'financing','dayormauth')).value
        rate = table.cell(row,Read_datebase.find_colum(file,'financing','rate')).value
        end_time = table.cell(row,Read_datebase.find_colum(file,'financing','end_time')).value
        service_fee = table.cell(row,Read_datebase.find_colum(file,'financing','service_fee')).value
        estate_name = table.cell(row,Read_datebase.find_colum(file,'financing','estate_name')).value
        build_size = table.cell(row,Read_datebase.find_colum(file,'financing','build_size')).value
        purpose = table.cell(row,Read_datebase.find_colum(file,'financing','purpose')).value
        pro_type = table.cell(row,Read_datebase.find_colum(file,'financing','pro_type')).value
        deposit = table.cell(row,Read_datebase.find_colum(file,'financing','deposit')).value
        activity = table.cell(row,Read_datebase.find_colum(file,'financing','activity')).value
        limit = table.cell(row,Read_datebase.find_colum(file,'financing','limit')).value
        p_price = table.cell(row,Read_datebase.find_colum(file,'financing','p_price')).value
        c_price = table.cell(row,Read_datebase.find_colum(file,'financing','c_price')).value
        table = data.sheet_by_name('public')
        url=table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value
        element_financing.financing(url,uername,purpose,pro_type,bank,moneyf,dayormauthtype,dayormauth,rate,end_time,service_fee,deposit,activity,estate_name,build_size,limit,p_price,c_price,driver)
