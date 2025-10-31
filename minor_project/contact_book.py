#!/usr/bin/env python3
"""
Simple CLI Contact Book
Features:
- Add, View, Search, Update, Delete contacts
- Save / Load contacts to JSON (contacts.json)
- Export contacts to CSV
- Basic validation (phone number digits, basic email check)
- Prevent duplicate name or phone
"""

import json
import csv
import os
import re

DATA_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def is_valid_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return len(digits) >= 7  # len >=7 to allow short numbers; adjust if you want exactly 10

def is_valid_email(email):
    # very simple email check
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email)) or email.strip() == ""

def find_by_name(contacts, name):
    name_l = name.strip().lower()
    return [c for c in contacts if c["name"].strip().lower() == name_l]

def find_by_phone(contacts, phone):
    digits = re.sub(r"\D", "", phone)
    return [c for c in contacts if re.sub(r"\D","",c.get("phone","")) == digits]

def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name required.")
        return
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()

    if not is_valid_phone(phone):
        print("Invalid phone number.")
        return
    if email and not is_valid_email(email):
        print("Invalid email format.")
        return

    if find_by_name(contacts, name):
        print("A contact with this name already exists.")
        return
    if find_by_phone(contacts, phone):
        print("A contact with this phone already exists.")
        return

    contact = {
        "name": name,
        "phone": re.sub(r"\s+"," ", phone),
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts saved.")
        return
    # Optional: alphabetical sort by name
    contacts_sorted = sorted(contacts, key=lambda c: c["name"].lower())
    print(f"\nTotal contacts: {len(contacts_sorted)}\n")
    for i, c in enumerate(contacts_sorted, 1):
        print(f"{i}. {c['name']} | {c.get('phone','')} | {c.get('email','')} | {c.get('address','')}")
    print()

def search_contact(contacts):
    q = input("Search by name or phone: ").strip()
    if not q:
        print("Enter a search query.")
        return
    # find by name partial match or exact phone
    q_digits = re.sub(r"\D", "", q)
    results = []
    for c in contacts:
        if q.lower() in c["name"].lower():
            results.append(c)
        elif q_digits and q_digits in re.sub(r"\D","", c.get("phone","")):
            results.append(c)
    if not results:
        print("No matches.")
        return
    print(f"Found {len(results)} result(s):")
    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']} | {c.get('phone','')} | {c.get('email','')} | {c.get('address','')}")

def update_contact(contacts):
    name = input("Enter exact name of contact to update: ").strip()
    matches = find_by_name(contacts, name)
    if not matches:
        print("Contact not found.")
        return
    contact = matches[0]
    print("Leave field empty to keep current value.")
    new_phone = input(f"Phone [{contact.get('phone','')}]: ").strip()
    new_email = input(f"Email [{contact.get('email','')}]: ").strip()
    new_address = input(f"Address [{contact.get('address','')}]: ").strip()

    if new_phone:
        if not is_valid_phone(new_phone):
            print("Invalid phone format. Update cancelled.")
            return
        # ensure phone uniqueness
        digits = re.sub(r"\D","", new_phone)
        for c in contacts:
            if c is contact:
                continue
            if re.sub(r"\D","", c.get("phone","")) == digits:
                print("Phone already used by another contact. Update cancelled.")
                return
        contact["phone"] = new_phone

    if new_email:
        if not is_valid_email(new_email):
            print("Invalid email. Update cancelled.")
            return
        contact["email"] = new_email

    if new_address:
        contact["address"] = new_address

    save_contacts(contacts)
    print("Contact updated.")

def delete_contact(contacts):
    name = input("Enter exact name of contact to delete: ").strip()
    matches = find_by_name(contacts, name)
    if not matches:
        print("Contact not found.")
        return
    contact = matches[0]
    confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        contacts.remove(contact)
        save_contacts(contacts)
        print("Deleted.")
    else:
        print("Cancelled.")

def export_csv(contacts):
    if not contacts:
        print("No contacts to export.")
        return
    filename = input("CSV filename (default contacts_export.csv): ").strip() or "contacts_export.csv"
    keys = ["name","phone","email","address"]
    try:
        with open(filename, "w", newline='', encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            for c in contacts:
                w.writerow({k: c.get(k,"") for k in keys})
        print(f"Exported to {filename}")
    except Exception as e:
        print("Failed to export:", e)

def show_menu():
    print("""
Contact Book - Menu
1) Add Contact
2) View All Contacts
3) Search Contact
4) Update Contact
5) Delete Contact
6) Export to CSV
7) Exit
""")

def main():
    contacts = load_contacts()
    while True:
        show_menu()
        choice = input("Choose (1-7): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            export_csv(contacts)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
