# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture #команда инициализации фикстуры
def app(request):
    fixture = Application()               #непосредстевнно сама фикстура (набор вспомогательных методов)
    request.addfinalizer(fixture.destroy) #указание на разрушение фикстуры
    return fixture


def test_add_group(app):   #убираем метод Self и добавляем метод app для ссылки на фикстуру аппликешен
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Gruppa", header="sdfbv", footer="asfasf"))
    app.logout()


def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()