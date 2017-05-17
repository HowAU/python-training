from model.group import Group
from random import randrange

def test_delete_some_group(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.group.count() ==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)#новый список групп должен быть на 1 больше, чем старый
    old_groups[index:index+1] = [] #при такой записи пустой позиции первого элемента - читай удаления
    # получаются разные указатели на 1 элемент в старом и новом списках. Сравнение в иттоге будет неверным
    # для корректности сровнения добавлется элемент __eq__, который сравнивает логическое наполнение,а не указатели
    assert old_groups == new_groups