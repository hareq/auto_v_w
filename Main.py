# -*- coding: UTF-8 -*-
#!/usr/local/bin/python

from Commons.lib import Read_datebase
from Module.Common import Browser
from Module.Front import Module_Front_Url,Invest,Module_Front_Login
from Module.Backstage import Module_Backstage_Url,Module_Backstage_Login,Module_Financing
import threading
from time import ctime,sleep
import Config.common_config

######################
#    对象定义    #
######################
browser = Browser.browser()
module_front_Url = Module_Front_Url.front_url()
module_Backstage_Url = Module_Backstage_Url.Backstage_url()
module_backstage_login = Module_Backstage_Login.module_backstage_login()
module_financing = Module_Financing.financing()
Invest = Invest.invest_start()
Login = Module_Front_Login.module_front_login()
common_config = Config.common_config


######################
#    初始化部分    #
######################
#打开浏览器
def main():
    file = common_config.datebase_path
    driver = browser.browser_start()

    #
    # ######################
    # #    前台操作部分    #
    # ######################
    # #打开vmdai前台首页
    # module_front_Url.url_start(driver,'')
    # #用户登录-投标
    # for row in range(2,Read_datebase.rownum(file,'invest')):
    #      Login.login_start(driver,row)
    #      Invest.invest_start(driver,row)
    #      Login.logout_start(driver)
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


threads = []
t1 = threading.Thread(target=main,args=())
threads.append(t1)
#t2 = threading.Thread(target=main,args=())
#threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "all over %s" %ctime()