from model.group import Group


def test_delete_first_group(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.group.count() ==0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
