from model.contact import Contact
import random


def test_modify_contact_firstname(app, db):
    if len(db.get_contact_list()) ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list() #получаем список существующих групп
    #index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    cont = Contact(firstname="Changename", middlename="Jay", lastname="ChangeSurname",
            home="777", mobile="666", work="555", phone2="444")
    #cont = Contact(address="Street")
    #cont.id = old_contacts[int(id)] #применяем для сохранения идентефикатора контакта для последующего изменения.
    # Проверка будет осуществляться "поячеечно"
    app.contact.modify_contact_by_id(id, cont)
    new_contacts = db.get_contact_list()  # получаем список новых групп
    old_contacts.append(cont)
    #assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max) #Инструкция



#def test_modify_contact_mobile(app):
#    if app.contact.count() == 0:
#        app.contact.creating_the_contact(Contact(firstname="test2"))
 #   app.contact.modify_first_contact(Contact(mobile="89565465476"))
