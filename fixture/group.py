from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None #сброс кэша. применяется когда он становится невалидным (неактуальным)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            # поскольку передавать напрямую в питон пустые значения (None) нельзя,то
            # для реализации ввода 1 значения делаем проверку - если значение пустое, то не происходит ничего,
            # если там что-то передается, то заполняем

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click() #delete group
        self.return_to_groups_page()
        self.group_cache = None #сброс кэша. применяется когда он становится невалидным (неактуальным)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()#получаем все чекбоксы и выбираем нужный

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None #сброс кэша. применяется когда он становится невалидным (неактуальным)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]")) #len() возвращает количество запрашиваемых элементов

    group_cache = None # проверка наполненности кэша

    def get_group_list(self): #сравнение размеров списка групп
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"): #span.group- общее название раздела для  каждой
                # из групп. И среди всех групп при помощи цикла формируем списовк
                text = element.text #название группы text - свойство к которому можно обращаться для получения текста
                id = element.find_element_by_name("selected[]").get_attribute("value") #номер бокса в списке групп
                self.group_cache.append(Group(name=text, id = id))
        return list(self.group_cache) #возвращаем список, т.к. это получается копия кэша и оригинал не страдает