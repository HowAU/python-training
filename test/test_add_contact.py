# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts=app.contact.get_contact_list() #получаем список существующих групп
    cont=Contact(firstname="John", middlename="Jay", lastname="Johnson", nickname="Jammy",
            title="Text", company="Royal", address="Somwhere", home="123", mobile="456", work="789",
            fax="369", email="a@mail.com", email2="b@mail.com", email3="c@mail.com",
            homepage="page.com", byear="1996", ayear="1987", address2="qwerty", phone2="qaz",
            notes="wsx")
    app.contact.creating_the_contact(cont)
    new_contacts=app.contact.get_contact_list() #получаем список новых групп
    assert len(old_contacts) + 1 == len(new_contacts) #сравниваем длины списков
    print(old_contacts)
