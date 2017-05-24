import re
from random import randrange


def test_phones_on_homepage(app): #тест, сравнивающий телефоны на стартовой странице  и в режиме редактирования
    #old_contacts =  #получаем список существующих групп
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    #берем уже готовую склейку со стартовой страницы и сравниваем с изготавливаемой склейкой со страницы редактированя


#def test_phones_on_contact_view_page(app):
#    index = randrange(len(app.contact.get_contact_list()))
#    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.work == contact_from_edit_page.work
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s) #что, на что меняем, где меняем


def merge_phones_like_on_homepage(Contact):
    return "\n".join(filter(lambda x: x != "", #лямбда-функция позволяет накладывать условия на дальнейший код
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [Contact.home, Contact.mobile, Contact.work, Contact.phone2])))) #функция склейки
#фильтр убирает пустые значения, мэп скрывает все минусы и прочие ненужные знакиб новый фильтр скрывает все пусты значения


def merge_emails_like_on_homepage(Contact):
    return "\n".join(filter(lambda x: x != "", #лямбда-функция позволяет накладывать условия на дальнейший код
                            filter(lambda x: x is not None,
                                       [Contact.email, Contact.email2, Contact.email3]))) #функция склейки
#фильтр убирает пустые значения, мэп скрывает все минусы и прочие ненужные знакиб новый фильтр скрывает все пусты значения
