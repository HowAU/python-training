def test_change_contact_properties(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_contact_properties()
    app.session.logout()