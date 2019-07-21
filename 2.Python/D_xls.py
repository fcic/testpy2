#pip3 install xlwt
import xlwt

def write(path,content):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    sheet.write(0,0,content)
    book.save(path)

write('fcic.xls','fcic123')