import pytest
from fixture.application import Application


@pytest.fixture #команда инициализации фикстуры
def app(request):
    fixture = Application()               #непосредстевнно сама фикстура (набор вспомогательных методов)
    request.addfinalizer(fixture.destroy) #указание на разрушение фикстуры
    return fixture