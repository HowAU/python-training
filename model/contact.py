from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None,  home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self): #определяет как будет выгляжить объект в консоли
        return "%s:%s:%s:%s"%(self.id, self.firstname, self.lastname, self.middlename)

    def __eq__(self, other): #позволет сравнивать логическое наполнение позиции, а не указатели
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == \
                                                                                other.firstname and self.lastname ==\
                                                                                                    other.lastname
        #return self.firstname == other.firstname and self.id == other.id and self.lastname = other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


