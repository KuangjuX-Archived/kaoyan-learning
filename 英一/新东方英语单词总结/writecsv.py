import csv
from operator import delitem
import xlrd

files = ["WordList{}-中英文.xls".format(i) for i in range(1, 51)]
csv_file = "WordList.csv"


with open(csv_file, "w", encoding='UTF-8') as f:
    csv_writer = csv.writer(f)
    for index, file in enumerate(files):
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        csv_writer.writerow(["WordList {}".format(index + 1)])
        print("WordList {}".format(index + 1))
        for i in range(table.nrows):
            row = table.row_values(i)[0]
            explaintions = table.row_values(i)[1].replace(",", "，")
            csv_writer.writerow([row, explaintions])