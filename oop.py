import json
import csv


class Employee:
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def display_info(self):
        print(f"Firstname: {self.firstname}\nLastname: {self.lastname}\nAge: {self.age}")

    def write_json(self):
        with open('dict.json', 'w') as filename:
            json.dump(vars(self), filename, indent=4)

    def write_csv(self):
        with open('dict.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for key, value in vars(self).items():
                writer.writerow([key, value])


obj = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua', ['go', "speak", "code"],
               ['ukrainian', "english"], ['Python', "C++", "lisp"])

obj.display_info()
obj.write_json()
obj.write_csv()
