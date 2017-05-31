# -*- coding: utf-8 -*-
from model.contact import Contact
#import pytest
#from data.contacts import testdata


#@pytest.mark.parametrize("contact", testdata, ids =[repr(x) for x in testdata] )  #обратить внимание - подробнее что это
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list() #получаем список существующих групп
    app.contact.creating_the_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count() #сравниваем длины списков
    new_contacts = app.contact.get_contact_list() #получаем список новых групп
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max) #Инструкция
    # assert позволяет производить проверки истинности утверждений, что может
