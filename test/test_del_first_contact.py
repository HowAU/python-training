from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.contact.count() ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list() #получаем список существующих групп
    index = randrange(len(old_contacts))
    print(index)
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()  # получаем список новых групп
    assert len(old_contacts) - 1 == app.contact.count() #сравниваем длины списков
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

