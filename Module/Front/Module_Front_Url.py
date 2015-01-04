from Commons.Common import Commons_Url
from Commons.lib import Read_datebase
url = Commons_Url.url()

class front_url:
    def url_start(self,driver,otherurl):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        urlall = table.cell(2,Read_datebase.find_colum(file,'public','url_vmdai')).value + '/'+otherurl
        url.url(urlall,driver)