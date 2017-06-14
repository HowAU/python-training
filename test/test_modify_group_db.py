from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    change_group = random.choice(old_groups)
    group = Group(name="New name", id=change_group.id)
    old_groups.remove(change_group)
    app.group.modify_group_by_id(group.id, change_group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

