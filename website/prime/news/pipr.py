import pandas as pd
import xlwings as xl


def report(df):
    # Dump Pandas DataFrame to Excel sheet
    s = xl.Book("e:/proect/website/prime/news/templates/news/myreport.xlsx")
    s1 = s.sheets(1)
    s1.range('A2').value = 'ОТЧЕТ'
    'one', 'two', 'three', 'four'
    df1=df[['one','three']]
    sd =len(df)
    s1.range('B2').value = sd
    df2 = df[['two','four']]
    s1.range('B4:C8').options(index=False,header=False).value = df1
    s1.range('H4:J9').value = df2

    s.save("e:/proect/website/prime/news/templates/news/myreport1.xlsx")
    return 1
