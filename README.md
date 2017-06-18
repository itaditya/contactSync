# contactSync
A fun script to add all my whatsapp group's contact to my Google Contacts

How it works - 
* As whatsapp provides no API so the script opens web.whatsapp.com and scrapes the selected groups contact list
* Then it searches on Fb with phone nums to get correct name and other details.
* All the contents are then stored in contacts.json file
* After that the contacts are added to Google Contacts via gdata python SDK.
