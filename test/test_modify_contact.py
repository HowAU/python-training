from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.creating_the_contact(Contact(firstname="test1"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.creating_the_contact(Contact(firstname="test2"))
    app.contact.modify_first_contact(Contact(mobile="89565465476"))
