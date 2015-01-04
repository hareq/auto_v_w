# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

from Commons.lib import Read_datebase
from Module.Common import Browser
from Module.Front import Module_Front_Url
from Module.Backstage import Module_Backstage_Url,Module_Backstage_Login,Module_Financing

######################
#    对象定义    #
######################
browser = Browser.browser()
module_front_Url = Module_Front_Url.front_url()
module_Backstage_Url = Module_Backstage_Url.Backstage_url()
module_backstage_login = Module_Backstage_Login.module_backstage_login()
module_financing = Module_Financing.financing()
######################
#    初始化部分    #
######################
#打开浏览器
file = 'E:\gautotest\datebase.xls'
driver = browser.browser_start()


# ######################
# #    前台操作部分    #
# ######################
# #打开vmdai前台首页
#module_front_Url.url_start(driver,'')
# #用户登录-投标
# for row in range(2,Read_datebase.rownum(file,'invest')):
#      Reception_start.login_start(driver,row)
#      Reception_start.invest_start(driver,row)
#      Reception_start.logout_start(driver)
# #退出登录
# #Reception.Signout(driver)
# #投标


######################
#    后台操作部分    #
######################
#打开vmdai后台首页
module_Backstage_Url.url_start(driver,'')
# #发标用户登录-发标
for row in range(2,Read_datebase.rownum(file,'financing')):
    module_backstage_login.login_start(driver,row)
    module_financing.financing(driver,row)
    module_backstage_login.logout_start(driver)




