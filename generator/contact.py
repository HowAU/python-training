from model.contact import Contact #создаем скрипт для генерации групп с последующим сохранением в файл
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try: #почитай про трай
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts","file"]) #опция n задает кол-во генерируемых данных, опия ф задает файл, куда все должно помещатся
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts: #данная структура  (в общем) позволяет управлять скриптом получения параметров групп с использованием раздела Edit Configuration
    #мы можем задать число групп и адрес положения файла результата
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen): #генерация случайных данных для теста
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10 #данные которые применяем в случайной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #случайным образом выбирает символы из заданной строки


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname="John", middlename="Jay", lastname="Johnson", home="123", mobile="456", work="789",
            email="a@mail.com", email2="b@mail.com", email3="c@mail.com",  phone2="456")
     for i in range(random.randrange(n))
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out: #открываем файл с флагом w - write (запись) и что-то туда записываем
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))

    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2)) #функция dumps превращает структуру данных в строку в формате джейсон