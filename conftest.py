import pytest
from fixture.application import Application


@pytest.fixture #команда инициализации фикстуры
def app(request):
    fixture = Application()               #непосредстевнно сама фикстура (набор вспомогательных методов)
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) #указание на разрушение фикстуры
    return fixture