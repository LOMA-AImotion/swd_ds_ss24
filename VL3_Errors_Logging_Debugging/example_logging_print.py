mail_server = None
import logging
logging.basicConfig(level=logging.INFO)

# Read the text file
import os
contacts_file = os.path.join(os.path.dirname(__file__), 'contacts.txt')
with open(contacts_file, 'r', encoding="utf-8") as file:
    print(f"Datei {contacts_file} erfolgreich geöffnet")
    lines = file.readlines()

# Process each line
for line in lines:
    name, email = line.strip().split(',')
    print(f"Sende mail an {name} mit der Adresse {email}")
    mail_server.mail(f"Hello {name}", email)
