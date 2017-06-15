


from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(id="54"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

   # cursor = connection.cursor() #указывает на данные, хранящиеся где-то в БД и возвращаемые след.запросом
   # cursor.execute("select*from group_list")
   # for row in cursor.fetchall(): # fetchall возвращает все данные что переданы
    #    print(row)
