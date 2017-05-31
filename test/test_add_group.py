# -*- coding: utf-8 -*-
from model.group import Group
#import pytest
#from data.groups import testdata


#@pytest.mark.parametrize("group", testdata, ids =[repr(x) for x in testdata] )  #обратить внимание - подробнее что это
def test_add_group(app, json_groups):   #убираем метод Self и добавляем метод app для ссылки на фикстуру аппликешен
    group = json_groups
    old_groups = app.group.get_group_list()
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
