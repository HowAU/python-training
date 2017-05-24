# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen): #генерация случайных данных для теста
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10 #данные которые применяем в случайной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #случайным образом выбирает символы из заданной строки

testdata = [Group(name="", header="", footer="")] + [
     Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 20))
     for i in range(random.randrange(5))
]


@pytest.mark.parametrize("group", testdata, ids =[repr(x) for x in testdata] )  #обратить внимание - подробнее что это
def test_add_group(app, group):   #убираем метод Self и добавляем метод app для ссылки на фикстуру аппликешен
    old_groups=app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+ 1 == app.group.count()#новый список групп должен быть на 1 больше, чем старый   //(хеширование)
    #т.к. создали новую группу. Короче говоря - просто считаем кол-во групп в начале и  конце и сравниваем
    new_groups = app.group.get_group_list()
    old_groups.append(group) # Добавляет указанный элемент в конец списка
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) #Инструкция assert позволяет производить проверки истинности утверждений, что может
    # быть использовано в отладочных целях.


#testdata =  [ один из варантов создания списка групп
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]    #настоящая форма записи означает что каждое из значений принимает по 2 варианта и как следствие всего буден 8 комбинаций
#     for header in ["", random_string("header", 10)]
#     for footer in ["", random_string("footer", 10)]
#]
