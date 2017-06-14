from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list() #получаем список существующих групп
    change_contact = random.choice(old_contacts)
    cont = Contact(firstname="Changename", middlename="Jay", lastname="ChangeSurname",
            home="777", mobile="666", work="555", phone2="444", id=change_contact.id) #Для получения какого-либо значения от любой позиции достаточно поставить после этой позиции точку и указать нужное значение
    old_contacts.remove(change_contact)
    app.contact.modify_contact_by_id(cont.id, cont)
    new_contacts = db.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

