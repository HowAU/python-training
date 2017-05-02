from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()


def test_modify_contact_mobile(app):
    app.contact.change_modify_first_contact(Contact(mobile="89565465476"))
    app.session.logout()
