from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New name")
    group.id = old_groups[index].id #применяем для сохранения идентефикатора группы для последующего изменения
                      #app.group.modify_first_group(group)
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)#новый список групп должен быть на 1 больше, чем старый
    old_groups[index] = group
    app.group.delete_first_group()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test2"))
#    app.group.modify_first_group(Group(header="New header"))
