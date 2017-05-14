# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):   #убираем метод Self и добавляем метод app для ссылки на фикстуру аппликешен
    old_groups=app.group.get_group_list()
    group = Group(name="Gruppa", header="sdfbv", footer="asfasf")
    app.group.create(group)
    assert len(old_groups)+ 1 == app.group.count()#новый список групп должен быть на 1 больше, чем старый
    #т.к. создали новую группу. Короче говоря - просто считаем кол-во групп в начале и  конце и сравниваем
    new_groups = app.group.get_group_list()
    old_groups.append(group) # Добавляет указанный элемент в конец списка
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) #Инструкция assert позволяет производить проверки истинности утверждений, что может
    # быть использовано в отладочных целях.


#def test_empty_group(app):
#    old_groups=app.group.get_group_list()
#    group = Group(name="Gruppas", header="sdggd", footer="qwr")
#    app.group.create(group)
#    new_groups=app.group.get_group_list()
#    assert len(old_groups)+ 1 == len(new_groups)#новый список групп должен быть на 1 больше, чем старый
#    old_groups.append(group) # Добавляет указанный элемент в конец списка
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)