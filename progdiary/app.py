from database import add_entry, view_entries

menu = """Please selectone ofthe following options:
1)Add new entry for today
2)View entries
3)Exit.

Your selection: """

welcome = "Welcome to the programming diary!" 
print(welcome)

user_input = input(menu)

"""
entries = [
    {"content": "Today I started Learning Python!", "date": "2024-06-01"},
    {"content": "I learned about functions and loops.", "date": "2024-06-02"},
    {"content": "I built a simple calculator app.", "date": "2024-06-03"},
    {"content": "I explored data structures like lists and dictionaries.", "date": "2024-06-04"},
]
"""

while user_input != "3":
    if user_input == "1":
       entry_content = input("What have you learned today? ")
       entry_date = input("Enter the date: ")
       add_entry(entry_content, entry_date)
    elif user_input == "2":
        entries = view_entries()

        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Invalid..")
