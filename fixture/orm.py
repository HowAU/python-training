from pony.orm import*
from datetime import datetime


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'#указываем название таблицы
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name') #указываем тип поля. Опционально - т.к. может быть и не стрококй, а пустой величиной
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'#указываем название таблицы
        id = PrimaryKey(int, column='group_id')#название столбца, где расположено значение можно не указывать если его наименование совпадает с наименованием значения, но все же лучше указывать
        firstname = Optional(str, column='firstname') #указываем тип поля. Опционально - т.к. может быть и не стрококй, а пустой величиной
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        deprecated = Optional(datetime, column='deprecated')

        #привязка к БД
    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping() #занимается сопоставлением описанных классов с таблицами и полями в этих таблицах в частности

    @db_session
    def get_group_list(self):
        return(list(select(g for g in ORMFixture.ORMGroup)))