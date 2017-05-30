import pytest
import json
import os.path
from fixture.application import Application


fixture = None
target = None

@pytest.fixture #команда инициализации фикстуры. добавка (scope = "session") дает возможность запускать несколько тестов
                #  в 1 окне
def app(request):
    global fixture
    global target #указание на использование глобальной переменной
    browser = request.config.getoption("--browser") #сделать ввод логина и пароля
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption(
            "--target"))  # переход к(абсолютный путь(путь к текущему файлу)). При данной записи нет нужды указывать адресс в настройках питона
        with open(config_file) as f:
            target = json.load(f) #f - указывает объект содержащийся в открытом файле
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=target['baseUrl'] )               #непосредстевнно сама фикстура (набор вспомогательных методов)
   # непосредстевнно сама фикстура (набор вспомогательных методов)
    fixture.session.ensure_login(username=target["username"], password=target["password"]) #проверка предусловия
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
    parser.addoption("--target", action="store", default="target.json")