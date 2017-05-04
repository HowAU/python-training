from model.contact import Contact


def test_delete_first_contact(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.contact.count() ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    app.contact.delete_first_contact()
