from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="") #Открытия БД под названием адресбук

try:
    list = db.get_group_list()
    for item in list:
        print(item)
    print(len(list))
finally:
    pass
   # cursor = connection.cursor() #указывает на данные, хранящиеся где-то в БД и возвращаемые след.запросом
   # cursor.execute("select*from group_list")
   # for row in cursor.fetchall(): # fetchall возвращает все данные что переданы
    #    print(row)
