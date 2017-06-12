import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="") #Открытия БД под названием адресбук

try:
    cursor = connection.cursor() #указывает на данные, хранящиеся где-то в БД и возвращаемые след.запросом
    cursor.execute("select*from group_list")
    for row in cursor.fetchall(): # fetchall возвращает все данные что переданы
        print(row)
finally:
    connection.close()