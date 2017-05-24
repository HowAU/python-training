# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen): #генерация случайных данных для теста
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10 #данные которые применяем в случайной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #случайным образом выбирает символы из заданной строки


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname="John", middlename="Jay", lastname="Johnson", home="123", mobile="456", work="789",
            email="a@mail.com", email2="b@mail.com", email3="c@mail.com",  phone2="456")
     for i in range(random.randrange(5))
]


@pytest.mark.parametrize("contact", testdata, ids =[repr(x) for x in testdata] )  #обратить внимание - подробнее что это
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list() #получаем список существующих групп
    app.contact.creating_the_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count() #сравниваем длины списков
    new_contacts = app.contact.get_contact_list() #получаем список новых групп
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max) #Инструкция
    # assert позволяет производить проверки истинности утверждений, что может
