# -*- coding: utf-8 -*-
import pytest

from fixture.AppCont import AppCont
from model.contact import Contact


@pytest.fixture #команда инициализации фикстуры
def app(request):
    fixture = AppCont()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.creating_the_contact(Contact(firstname="John", middlename="Jay", lastname="Johnson", nickname="Jammy",
                             title="Text", company="Royal", address="Somwhere", home="123", mobile="456", work="789",
                             fax="369", email="a@mail.com", email2="b@mail.com", email3="c@mail.com",
                             homepage="page.com",byear="1996", ayear="1987", address2="qwerty", phone2="qaz",
                             notes="wsx"))
    app.session.logout()
