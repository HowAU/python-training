from model.group import Group


def test_delete_first_group(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.group.count() ==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)#новый список групп должен быть на 1 больше, чем старый
    old_groups[0:1] = [] #при такой записи пустой позиции первого элемента - читай удаления
    # получаются разные указатели на 1 элемент в старом и новом списках. Сравнение в иттоге будет неверным
    # для корректности сровнения добавлется элемент __eq__, который сравнивает логическое наполнение,а не указатели
    assert old_groups == new_groups
