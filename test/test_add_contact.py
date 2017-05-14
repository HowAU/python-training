# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts=app.contact.get_contact_list() #получаем список существующих групп
    cont=Contact(firstname="John", middlename="Jay", lastname="Johnson",
            home="123", mobile="456", work="789",
            email="a@mail.com", email2="b@mail.com", email3="c@mail.com",
            phone2="qaz")
    app.contact.creating_the_contact(cont)
    assert len(old_contacts) + 1 == app.contact.count() #сравниваем длины списков
    new_contacts = app.contact.get_contact_list() #получаем список новых групп
    old_contacts.append(cont)
    print(old_contacts)
    print("----------------------")
    print(new_contacts)
    #assert old_contacts == new_contacts
    #assert sorted(old_contacts, key=Contact.cells_or_max) == sorted(new_contacts, key=Contact.cells_or_max) #Инструкция
    # assert позволяет производить проверки истинности утверждений, что может
