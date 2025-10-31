📘 Project Overview

The CLI Contact Book Application is a Python-based command-line program that allows users to add, view, search, update, delete, and export contacts.
It uses the built-in json and csv modules for data storage and export — no external libraries required.
The entire project runs in a Command-Line Interface (CLI) environment.

🧩 Features

➕ Add Contact — Add new contacts with name, phone, email, and address.

👀 View All Contacts — Display all saved contacts in an easy-to-read format.

🔍 Search Contact — Search by name or phone number.

✏️ Update Contact — Modify existing contact details.

❌ Delete Contact — Remove a contact permanently.

📁 Export to CSV — Export all saved contacts to a CSV file for use in Excel or Google Sheets.

💾 Auto Save/Load — Contacts are automatically saved in a contacts.json file and reloaded when you restart the program.

🧱 Validation — Prevents duplicate names or phone numbers and checks email/phone formats.

⚙️ Modules Used
Module	Purpose
json	To store and retrieve contacts in a local JSON file (contacts.json).
🌱 Future Enhancements

These are some improvements that can be added later:

🔐 Password Protection: Add login authentication to restrict access to the contact book.

⭐ Favorite Contacts: Mark certain contacts as favorites for quick access.

🎨 Colored CLI Output: Use colorama module to make text menus more attractive.

🗃️ Sort and Filter Options: View contacts sorted alphabetically or filter by city/domain.

☁️ Cloud Sync: Sync contacts online using a database or API.

👩‍💻 Developed By

Name: Harman Kaur
Project: CLI Contact Book (Minor Project)
Language: Python 3
Environment: Command-Line Interface (CLI)
csv	To export contacts to a CSV file (contacts_export.csv).
os, re	To handle file operations and perform basic input validation.
💻 Environment
