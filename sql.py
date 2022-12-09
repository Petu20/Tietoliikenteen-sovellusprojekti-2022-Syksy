import mysql.connector
from mysql.connector import Error
import csv
from login import * 

host='172.20.241.9'
database='measurements'
user='dbaccess_ro'
password='vsdjkvwselkvwe234wv234vsdfas'

mydb = mysql.connector.connect(host=host,
                                database=database,
                                user=user,
                                password=password,)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM rawdata WHERE groupid ='74'")

myresult = mycursor.fetchall()

for x in myresult:
        print("GroupID = ", x[2]),
        print("x = ", x[5]),
        print("y  = ", x[6]),
        print("z  = ", x[7])

