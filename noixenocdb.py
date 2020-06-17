import mysql.connector
from mysql.connector import Error
from bs4 import BeautifulSoup
import csv
# import unicodecsv as csv

# with myFile:
def to_utf8(lst):
    return [unicode(elem).encode('utf-8') for elem in lst]

def conexion():

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='menorca_nuevaweb',
                                            user='root',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select * from blog")
            records = cursor.fetchall()
            
            myFile = open('prueba.csv','w',encoding='utf-8')
            i = 1
            for row in records:
                # print("blg_id = ", row[0], )
                # print("blg_titulo = ", row[1])

                arreglo = []

                textolimpio = BeautifulSoup(row[7], 'html.parser').text

                textolimpio = textolimpio.replace('\n',' ')#.replace('\r',' ')
                
                textarray = [i,textolimpio]
                arreglo.append(textarray)

                writer = csv.writer(myFile)
                writer.writerows(arreglo)
                i=i+1
                # print("blg_cuerpo = ", clean)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




conexion()
# con.execute("select * from blog")
# records = con.fetchall()
# print("Total number of rows in Laptop is: ", con.rowcount)

# print("\nPrinting each laptop record")
# for row in records:
#     print("Id = ", row[0], )
#     print("Name = ", row[1])
#     print("Price  = ", row[2])
#     print("Purchase date  = ", row[3], "\n")