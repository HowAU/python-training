import mysql.connector
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="") #Открытия БД под названием адресбук

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
   # cursor = connection.cursor() #указывает на данные, хранящиеся где-то в БД и возвращаемые след.запросом
   # cursor.execute("select*from group_list")
   # for row in cursor.fetchall(): # fetchall возвращает все данные что переданы
    #    print(row)
finally:
    db.destroy()