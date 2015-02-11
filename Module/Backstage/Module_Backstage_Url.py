from Commons.Common import Commons_Url
from Commons.lib import Read_datebase
from Config import common_config
url = Commons_Url.url()

class Backstage_url:

    def url_start(self,driver,otherurl):
        file = common_config.datebase_path
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        urlall = table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value + '/'+otherurl
        url.url(urlall,driver)
