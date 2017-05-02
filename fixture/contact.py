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
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[10]").click()
        self.change_field("homepage", contact.homepage)
        self.change_field("byear", contact.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[16]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[10]").click()
        self.change_field("ayear", contact.ayear)
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").click()
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
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()#select 1 contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def change_contact_properties(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Jayme")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Janny")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Where?")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("Home")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("e@mail.com")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("f@mail.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("g@mail.com")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("page2.com")
        wd.find_element_by_name("update").click()