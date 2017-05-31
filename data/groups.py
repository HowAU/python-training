#создаем файл для загрузки значений группы из одтельной дирректории и наполняем его генераторами значений для групп
from model.group import Group
#import random
#import string

testdata = [
    Group(name="name1", header="header1", footer="footer1"), #передаем константы в тест создания групп
    Group(name="name2", header="header2", footer="footer2")
]


#def random_string(prefix, maxlen): #генерация случайных данных для теста
 #   symbols = string.ascii_letters+string.digits + string.punctuation + " "*10 #данные которые применяем в случайной строке
 #   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #случайным образом выбирает символы из заданной строки

#testdata = [Group(name="", header="", footer="")] + [
 #    Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 20))
 #    for i in range(random.randrange(5))
#]
