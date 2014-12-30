class Backstage_start:

    def url_start(self,driver):
        file = 'E:\gautotest\datebase.xls'
        data = Read_datebase.open_excel(file)
        table = data.sheet_by_name('public')
        mylogin = Reception()
        mylogin.url(table.cell(2,Read_datebase.find_colum(file,'public','url_admin')).value,driver)