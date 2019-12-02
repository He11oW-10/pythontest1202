import pyodbc

server = 'tcp:servertest1202.database.windows.net,1433'
database = 'datatest1202'
username = 'v-yilzho'
password = 'Z23_y0@O7'
driver= '{ODBC Driver 17 for SQL Server}'

if __name__== "__main__":
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  cursor.execute("select Stu_city from Students ")
  row = cursor.fetchone()
  while row:
    print(str(row[0]))
    row = cursor.fetchone()
    

