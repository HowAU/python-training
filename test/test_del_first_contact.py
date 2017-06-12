from model.contact import Contact
from random import randrange
import random



def test_delete_some_contact(app, db):
    #проверка на наличие хотя бы 1 группы/котакта
    if len(db.get_contact_list()) ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list() #получаем список существующих групп
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()  # получаем список новых групп
   # assert len(old_contacts) - 1 == app.contact.count() #сравниваем длины списков
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

