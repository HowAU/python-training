from model.contact import Contact
from model.group import Group
import random


def test_contact_not_in_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.creating_the_contact(Contact(firstname="test"))
    group = random.choice(db.get_group_list())
    contact = random.choice(orm.get_contacts_not_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group_by_id(group.id, contact.id)
    old_contact_in_groups = orm.get_contacts_in_group(Group(id=group.id))
    contact_in_group = random.choice(old_contact_in_groups)
    app.contact.delete_contact_from_group_by_id(contact_in_group.id, group.id)

    new_contact_in_groups = orm.get_contacts_in_group(group)
    old_contact_in_groups.remove(contact_in_group)
    assert sorted(old_contact_in_groups, key=Contact.id_or_max) == sorted(new_contact_in_groups, key=Contact.id_or_max)
