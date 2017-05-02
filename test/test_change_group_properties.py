def test_change_group_properties(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group_properties()
    app.session.logout()
