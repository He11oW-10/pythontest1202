import pyodbc
from flask import Flask
app = Flask(__name__)

server = ''
database = ''
username = ''
password = ''
driver= '{ODBC Driver 17 for SQL Server}'

@app.route("/")
def hello():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("select Stu_city from Students ")
    row = cursor.fetchone()
    temp=""
    while row:
        temp=temp+str(row[0])
        row = cursor.fetchone()
    return temp

