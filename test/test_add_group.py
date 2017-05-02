# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):   #убираем метод Self и добавляем метод app для ссылки на фикстуру аппликешен
    app.group.create(Group(name="Gruppa", header="sdfbv", footer="asfasf"))


def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
