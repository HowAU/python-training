from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts=app.contact.get_contact_list() #получаем список существующих групп
    cont=Contact(firstname="test1")
    cont.cells = old_contacts[0].cells #применяем для сохранения идентефикатора контакта для последующего изменения.
    # Проверка будет осуществляться "поячеечно"
    app.contact.modify_first_contact(cont)
    new_contacts = app.contact.get_contact_list()  # получаем список новых групп
    assert len(old_contacts) == len(new_contacts) #сравниваем длины списков
    old_contacts[0] = cont
    #assert old_contacts == new_contacts
    print(old_contacts)
    print("----------------------")
    print(new_contacts)



#def test_modify_contact_mobile(app):
#    if app.contact.count() == 0:
#        app.contact.creating_the_contact(Contact(firstname="test2"))
 #   app.contact.modify_first_contact(Contact(mobile="89565465476"))
