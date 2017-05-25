import pytest
from fixture.application import Application

fixture=None

@pytest.fixture #команда инициализации фикстуры. добавка (scope = "session") дает возможность запускать несколько тестов
                #  в 1 окне
def app(request):
    global fixture
    browser = request.config.getoption("--browser") #сделать ввод логина и пароля
    baseUrl = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, baseUrl=baseUrl)               #непосредстевнно сама фикстура (набор вспомогательных методов)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, baseUrl=baseUrl)  # непосредстевнно сама фикстура (набор вспомогательных методов)
    fixture.session.ensure_login(username="admin", password="secret") #проверка предусловия
    return fixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin) #указание на разрушение фикстуры
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox") #что хотим передать, что с этим сделать и какое значение по умолчанию
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")