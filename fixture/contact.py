from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def creating_the_contact(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # create_contact
        self.fill_contact_form(contact)
        # finished_the_creation
        wd.find_element_by_name("submit").click()
        self.go_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
       # wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
       # wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        self.change_field("homepage", contact.homepage)
        self.change_field("byear", contact.byear)
       # wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[16]").click()
       # wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").click()
        self.change_field("ayear", contact.ayear)
       # wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").click()
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)

    def change_field(self, field_contact_name, text_contact):
        wd = self.app.wd
        if text_contact is not None:
            wd.find_element_by_name(field_contact_name).click()
            wd.find_element_by_name(field_contact_name).clear()
            wd.find_element_by_name(field_contact_name).send_keys(text_contact)

    def go_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("") and len(wd.find_elements_by_name("Send e-Mail"))>0):
            wd.find_element_by_link_text("home").click()

    def open_homepage(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring"))>0:
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        self.go_to_homepage()
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #fill form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.go_to_homepage()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]")) #len() возвращает количество запрашиваемых элементов

    def get_contact_list(self): #сравнение размеров списка
        wd = self.app.wd
        self.open_homepage()
        contacts = []
        for row in wd.find_elements_by_name("entry"):
            text = row.text #название группы
            value = row.find_elements_by_name("value")
            contacts.append(Contact(firstname=text, cells= value))
        return contacts
