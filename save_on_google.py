import json
import atom
import gdata.contacts.data
import gdata.contacts.client
token = gdata.gauth.OAuth2Token(
    client_id="client_id",
    client_secret="client_secret",
    scope='https://www.google.com/m8/feeds',
    user_agent='app.testing',
    access_token="access_token")
contact_client = gdata.contacts.client.ContactsClient()
token.authorize(contact_client)
def addContact(name,phno):
  notes = "additional_data"
  new_contact = gdata.contacts.data.ContactEntry(name=gdata.data.Name(full_name=gdata.data.FullName(text=name)))
  new_contact.content = atom.data.Content(text=notes)
  new_contact.phone_number.append(gdata.data.PhoneNumber(text=phno,
        rel=gdata.data.WORK_REL, primary='true'))
  # Create a work email address for the contact and use as primary. 
  entry = contact_client.CreateContact(new_contact)

  if entry:
    print 'Added {}'.format(name)
  else:
    print 'Upload error.'
with open('contacts.json') as contacts:
    contactsData = json.load(contacts)
    for (index,contact) in enumerate(contactsData):
        name = contact["name"]
        phno = contact["phno"]
        if(name and phno):
            addContact(name,phno)
