import pyodbc
import datetime
import csv
import sys
#import zipfile
import os

#읽을파일 경로
#rpath = 'D:/dw/bi_prod/BI_TOSBI000_20190410_095000.CSV'
rpath = 'C:/Users/Samsung/Desktop/BI_TOSBI014_20190410_095000.CSV'

'''
BI_TOSBI000_20190404_143810.CSV
BI_TOSBI000_20190404_143800.CSV
BI_TOSBI000_20190404_143840.CSV
BI_TOSBI000_20190404_143830.CSV     제외
BI_TOSBI000_20190404_143820.CSV
'''

#입력테이블명
tblname = 'XXX_TOSBI014'

#sys.exit()

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=123.123.123.123;DATABASE=database;UID=userid;PWD=password')
cursor = cnxn.cursor()

with open (rpath, 'r', encoding='UTF8') as f:

    reader = csv.reader(f)
    columns = next(reader)
    columns = ['col1', 'col2 ', 'col3', 'col4', 'col5']

    columns.append('CRT_USER_ID')
    columns.append('DATA_CRT_DTM')

    #print(columns)

    sql = 'insert into ' + tblname + '({0}) values ({1})'
    sql = sql.format(','.join(columns), ','.join('?' * len(columns)))
	
    #print(sql)

    k = 0

    for data in reader:

        k += 1
        data.append('ISP')
        data.append(str(datetime.datetime.now()))

        cursor.execute(sql, data)
    cursor.commit()

msg = "%s row(s)" % (str(k))
print(msg)

msg = 'insert complete.'
print(msg)
