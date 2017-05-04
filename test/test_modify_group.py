from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    app.group.modify_first_group(Group(name="New name"))
    app.group.delete_first_group()


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test2"))
    app.group.modify_first_group(Group(header="New header"))
