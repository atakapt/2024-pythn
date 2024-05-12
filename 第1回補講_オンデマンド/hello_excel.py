import openpyxl as excel

# 新規ワークブックを作る
book = excel.Workbook()

# アクティブなワークシートを得る
sheet = book.active

# A1のセルに値を設定する
sheet["A1"] = "こんばんは"

# ファイルを保存
book.save("hello.xlsx")