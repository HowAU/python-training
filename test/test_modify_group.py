from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    #index = randrange(len(old_groups))
    group = random.choice(old_groups)
    #old_groups.remove(group)
    change_group = Group(name="New name")
   # change_group.id = old_groups[group].id #применяем для сохранения идентефикатора контакта для последующего изменения.
   # group.id = old_groups #применяем для сохранения идентефикатора группы для последующего изменения
    app.group.modify_group_by_id(group.id, change_group)
    new_groups = db.get_group_list()
    #assert len(old_groups) == app.group.count()#новый список групп должен быть на 1 больше, чем старый
    old_groups.append(change_group)
    #app.group.delete_first_group()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test2"))
#    app.group.modify_first_group(Group(header="New header"))
