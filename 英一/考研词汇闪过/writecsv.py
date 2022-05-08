import csv
from operator import delitem
import xlrd

# files = ["WordList{}-中英文.xls".format(i) for i in range(1, 51)]
files = ["高频词.xls"]
csv_file = "高频词.csv"


with open(csv_file, "w", encoding='UTF-8') as f:
    csv_writer = csv.writer(f)
    for index, file in enumerate(files):
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        for i in range(table.nrows):
            row = table.row_values(i)[0]
            if len(row) > 0 and row[0:8] != 'WordList':
                print(row)
                explaintions = table.row_values(i)[1].replace(",", "，")
                csv_writer.writerow([row, explaintions])