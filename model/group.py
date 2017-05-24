from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id #теперь у группы появляется уникальный идентефикатор в списке групп

    def __repr__(self): #определяет как будет выгляжить объект в консоли
        return "%s:%s:%s:%s"%(self.id, self.name, self.header, self.footer )

    def __eq__(self, other): #позволет сравнивать логическое наполнение позиции, а не указатели
        return (self.id is None or other.id is None or self.id== other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
