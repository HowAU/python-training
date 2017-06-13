import pytest
import json
import os.path
from fixture.application import Application
import importlib
import jsonpickle
from fixture.db import DbFixture



fixture = None
target = None

def load_config(file):
    global target  # указание на использование глобальной переменной
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)  # переход к(абсолютный путь(путь к текущему файлу)). При данной записи нет нужды указывать адресс в настройках питона
        with open(config_file) as f:
            target = json.load(f)#f - указывает объект содержащийся в открытом файле
    return target


@pytest.fixture #команда инициализации фикстуры. добавка (scope = "session") дает возможность запускать несколько тестов
                #  в 1 окне
def app(request):
    global fixture
    global target #указание на использование глобальной переменной
    browser = request.config.getoption("--browser") #сделать ввод логина и пароля
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=web_config['baseUrl'] )               #непосредстевнно сама фикстура (набор вспомогательных методов)
   # непосредстевнно сама фикстура (набор вспомогательных методов)
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"]) #проверка предусловия
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture=DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin) #указание на разрушение фикстуры
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox") #что хотим передать, что с этим сделать и какое значение по умолчанию
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")



# что происходит в этой функции - грубо говоря мы ищем файлы в дирректории указанной далее. Как - задаем в старте теста адрес
# начинающийся на data_ , к примеру, после отсекаем эту часть data_ и остается просто contacts. далее переходим к следующей функции
def pytest_generate_tests(metafunc):#метафунк - через него можно получить почти любую информацию об объекте
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"): #если фикстура начинается с data_
            testdata = load_from_module(fixture[5:]) #то подгружаем данные из модуля с удалением первых 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:]) #то подгружаем данные из json с удалением первых 5 символов
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# которая импортирует данные из файла, чье название мы получили ранее, теперь перевели фв строковую форму и забрали оттуда нужный параметр testdata
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file): #загрузка данных из файла формата джейсон
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
