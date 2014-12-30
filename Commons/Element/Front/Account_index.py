# -*- coding: UTF-8 -*-
#!/usr/local/bin/python
__author__ = 'guyanhua'
class index:
    url = 'account/index'
#details--账户余额 1
#activity--活动金额 2
#available_balance--可用余额 3
#bid_money--投标中的金额 4
    def head_css(self):
        details = 'html body div.main.projectlist div.acc_nav div.wrap div.acc_tit div.dressing_list dl dt span.alt'
        activity = 'html body div.main.projectlist div.acc_nav div.wrap div.acc_tit div.dressing_list dl dt span.alt'
        available_balance = 'html body div.main.projectlist div.acc_nav div.wrap div.acc_tit div.dressing_list dl dd span.alt'
        bid_money = 'html body div.main.projectlist div.acc_nav div.wrap div.acc_tit div.dressing_list dl dd span.alt'
        return details,activity,available_balance,bid_money
    def head_xpath(self):
        details = '/html/body/div[1]/div[3]/div/div[1]/div[2]/dl/dt/span[2]'
        activity = '/html/body/div[1]/div[3]/div/div[1]/div[2]/dl/dt/span[6]'
        available_balance = '/html/body/div[1]/div[3]/div/div[1]/div[2]/dl/dd/span[2]'
        bid_money = '/html/body/div[1]/div[3]/div/div[1]/div[2]/dl/dd/span[4]'
        return details,activity,available_balance,bid_money

    def lend(self):
        fes = ''

class backlend:
    url = 'account/backlend'

