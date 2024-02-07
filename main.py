import os
import json
import tkinter as tk
from tkinter import filedialog


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog
    return file_path


def check_file_existence(file_name):
    if os.path.exists(file_name):
        print(f"The file '{file_name}' exists.")
    else:
        print(f"The file '{file_name}' does not exist.")
    return file_name


def get_entries(file_name):
    entries = []
    with open(file_name, 'r') as file:
        data = json.load(file)
        for idx, entry in enumerate(data, 1):
            entry_text = f"{entry}"
            entries.append(entry_text)
    return entries


# Function to print the entries with numbers
def print_entries_with_numbers(entries):
    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. {entry}")
    return int(input("Enter the category of data (the number in front of it): "))


def extract_data_from_file(file_name, selection):
    entries = []
    usernames = []

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            if selection in data:
                friend_requests_sent = data[selection]
                for entry in friend_requests_sent:
                    if "Username" in entry and "Source" in entry:
                        name = entry.get("Username", "")
                        source = entry.get("Source", "")
                        formatted_entry = f"{name.ljust(20)}{source}"
                        entries.append(formatted_entry)
                        usernames.append(name)
    except FileNotFoundError:
        print("File not found.")

    return entries, usernames


def menu():
    while True:
        print("What to do now?:\n1. Remove these entries\n2. Exit")
        try:
            selection = int(input())
            if selection in [1, 2]:
                return selection
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def remove_entries():
    # Implement the functionality to remove entries here
    confirmation = input("Are you sure you want to remove these entries? (y/n): ")
    if confirmation.lower() == "y":
        print("Removing entries...")
        # Additional logic to remove entries can be added here
    else:
        print("Operation cancelled. Exiting.")
        exit(0)

print("Select friends.json from your downloaded data: ")
file_name = select_file()
# file_name = "friends.json"

check_file_existence(file_name)  # check for existence
entries = get_entries(file_name)  # entries are the data where the entries are stored
number = print_entries_with_numbers(entries)  # print the entries with numbers
selector = entries[number - 1]
print(entries[number - 1])
entries, usernames = extract_data_from_file(file_name, selector)  # usernames is the array of users

for idx, entry in enumerate(entries, 1):
    print(f"{idx}. {entry}")

menu_selection = menu()  # get the menu selection
if menu_selection == 1:
    remove_entries()
elif menu_selection == 2:
    exit(0)

# for entry in usernames:
#    print(entry)
