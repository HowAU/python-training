from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New name")
    group.id = old_groups[0].id #применяем для сохранения идентефикатора группы для последующего изменения
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)#новый список групп должен быть на 1 больше, чем старый
    old_groups[0] = group
    app.group.delete_first_group()


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test2"))
#    app.group.modify_first_group(Group(header="New header"))
