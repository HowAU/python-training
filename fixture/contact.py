from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def creating_the_contact(self, contact):
        wd = self.app.wd
        self.open_homepage()
        self.open_new_contact_page()
        # create_contact
        self.fill_contact_form(contact)
        # finished_the_creation
        wd.find_element_by_name("submit").click()
        self.go_to_homepage()
        self.contact_cache = None

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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_homepage()
        wd.find_elements_by_name("selected[]")[index].click() #смотри построение списка групп

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_index(index)
        self.find_delete_button()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def find_delete_button(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_index(index)
        #open modification form
        self.open_contact_to_edit_by_index(index)
        #fill form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.go_to_homepage()
        self.contact_cache = None

    def find_modify_button(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]")) #len() возвращает количество запрашиваемых элементов

    contact_cache = None # проверка наполненности кэша

    def get_contact_list(self): #сравнение размеров списка
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                #full_name = text1 + " " + text2
                id = cells[0].find_element_by_name("selected[]").get_attribute("value") #при создании списка cells получается
                # поэлементный мегасписок содержащий все, что имеется в столбце у таблицы контактов, из этих поэлементных значений
                #  мы имеем возможность выбрать нужные нам свойства и далее работать с ними
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text#берем текст ячейки
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_emails_from_homepage=all_emails, all_phones_from_homepage=all_phones)) #заменяем телефоны поштучно на список со всеми телефонами сразу
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_id(id)
        self.find_delete_button()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        wd.find_elements_by_name("entry")  # смотри построение списка групп

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()  # смотри построение списка групп

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_homepage()
        #open modification form
        self.open_contact_to_edit_by_id(id)
        #fill form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.go_to_homepage()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def add_contact_to_group_by_id(self, group, contact):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_id(contact)
        self.select_group_by_id(group)
        wd.find_element_by_xpath("//input[@value='Add to']").click()

    def select_group_by_id(self, group):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group).click()


    def delete_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_homepage()
        self.select_contac_groups_list_by_id(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//input[@name='remove']").click()



    def select_contac_groups_list_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group_id).click()