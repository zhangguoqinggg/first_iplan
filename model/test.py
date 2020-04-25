import pyodbc

print("%" * 80)
connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=117.50.82.37,1433;DATABASE=YZDQUOTE;UID=iplan;PWD=1234qwerasdfzxcv!')

curs = connection.execute('select GETDATE()')
print("%"*80)
print(curs.fetchone())