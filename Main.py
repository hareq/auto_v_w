# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

import Read_datebase
import Reception_start
import Backstage_start
import Reception
import Backstage
from commons import Public

public = Public.public()
Reception_start = Reception_start.Reception_start()
Backstage_start = Backstage_start.Backstage_start()
Reception = Reception.Reception()
Backstage = Backstage.Backstage()

######################
#    初始化部分    #
######################
#打开浏览器
file = 'E:\gautotest\datebase.xls'
driver = public.browser_start()


# ######################
# #    前台操作部分    #
# ######################
# #打开vmdai前台首页
# Reception_start.url_start(driver)
# #用户登录-投标
# for row in range(2,Read_datebase.rownum(file,'invest')):
#     Reception_start.login_start(driver,row)
#     Reception_start.invest_start(driver,row)
#     Reception_start.logout_start(driver)
# #退出登录
# #Reception.Signout(driver)
# #投标


######################
#    后台操作部分    #
######################
#打开vmdai后台首页
Backstage_start.url_start(driver)
#发标用户登录-发标
for row in range(2,Read_datebase.rownum(file,'financing')):
    Backstage_start.login_start(driver,row)
    Backstage_start.financing_start(driver,row)
    Backstage_start.logout_start(driver)




