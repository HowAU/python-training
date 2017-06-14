from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list() #получаем список существующих групп
    index = randrange(len(old_contacts))
    cont = Contact(firstname="Changename", middlename="Jay", lastname="ChangeSurname",
            home="777", mobile="666", work="555", phone2="444")
    cont.id = old_contacts[index].id #применяем для сохранения идентефикатора контакта для последующего изменения.
    # Проверка будет осуществляться "поячеечно"
    app.contact.modify_contact_by_index(index, cont)
    new_contacts = app.contact.get_contact_list()  # получаем список новых групп
    assert len(old_contacts) == app.contact.count()  # сравниваем длины списков
    old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # def test_modify_contact_mobile(app):
    #    if app.contact.count() == 0:
    #        app.contact.creating_the_contact(Contact(firstname="test2"))
    #   app.contact.modify_first_contact(Contact(mobile="89565465476"))
