from model.contact import Contact


def test_delete_first_contact(app):
    #проверка на наличие хотя бы 1 группы/котакта
    if app.contact.count() ==0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list() #получаем список существующих групп
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()  # получаем список новых групп
    assert len(old_contacts) - 1 == len(new_contacts) #сравниваем длины списков
    old_contacts[0:1] = []
    assert old_contacts == new_contacts