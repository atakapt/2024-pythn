import openpyxl as excel

# ワークブック（Excel）を読み込む
book = excel.load_workbook("hello.xlsx")

# アクティブなワークシートを得る
sheet = book.active

# セルA1の値を得る
cell = sheet["A1"]

# セルの値を表示する
print(cell.value)