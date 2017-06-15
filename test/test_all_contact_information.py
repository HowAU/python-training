import re
from model.contact import Contact


def test_all_contact_information(app, db):
    contact_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    print(contact_from_homepage)
    print(contact_from_db)
    for i in range(0, len(contact_from_homepage)): #выбираем контакт для сравнения по индексу, где индекс - все контакты
        assert contact_from_homepage[i].firstname == contact_from_db[i].firstname
        assert contact_from_homepage[i].lastname == contact_from_db[i].lastname
        assert contact_from_homepage[i].address == contact_from_db[i].address
        assert contact_from_homepage[i].all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_db[i])
        assert contact_from_homepage[i].all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_db[i])
    #берем уже готовую склейку со стартовой страницы и сравниваем с изготавливаемой склейкой со страницы редактированя


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