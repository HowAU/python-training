from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts=app.contact.get_contact_list() #получаем список существующих групп
    if app.contact.count() == 0:
        app.contact.creating_the_contact(Contact(firstname="test1"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    new_contacts = app.contact.get_contact_list()  # получаем список новых групп
    assert len(old_contacts) == len(new_contacts) #сравниваем длины списков


def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.creating_the_contact(Contact(firstname="test2"))
    app.contact.modify_first_contact(Contact(mobile="89565465476"))
