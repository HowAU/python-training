import pytest
from fixture.application import Application

fixture=None

@pytest.fixture #команда инициализации фикстуры. добавка (scope = "session") дает возможность запускать несколько тестов
                #  в 1 окне
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()               #непосредстевнно сама фикстура (набор вспомогательных методов)
    else:
        if not fixture.is_valid():
            fixture = Application()  # непосредстевнно сама фикстура (набор вспомогательных методов)
    fixture.session.ensure_login(username="admin", password="secret") #проверка предусловия
    return fixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin) #указание на разрушение фикстуры
    return fixture