from model.group import Group
from model.contact import Contact
import random


def test_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    old_contact_in_groups = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group_by_id(group.id, contact.id)

    new_contacts_in_group = orm.get_contacts_in_group(group)
    old_contact_in_groups.append(contact)
    assert sorted(old_contact_in_groups, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)



