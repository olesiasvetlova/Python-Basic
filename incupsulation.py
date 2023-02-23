class Person:
    """
    Класс описывающий человека
    """
    __firstname = str()
    __lastname = str()
    __age = int()
    __email = str()
    __phone = str()

    @property
    def firstname(self):
        return self.__firstname.capitalize()

    @property
    def lastname(self):
        return self.__lastname.capitalize()

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @email.setter
    def email(self, email: str):
        self.__email = email

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def __set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0

    def __init__(self, name: str, surname: str, age: int):
        self.__firstname = name
        self.__lastname = surname
        self.__set_age(age)

    def __str__(self):
        info = f'Name: {self.firstname}\nSurname: {self.lastname}\nAge: {self.age}\n'
        if self.email != '':
            info = f'{info}e-mail: {self.email}\n'
        if self.phone != '':
            info = f'{info}phone: {self.phone}'
        return info


class Family:
    """
    Класс описывающий семью
    """
    def __init__(self, members: list):
        if members is None:
            members = []
        self.members = members

    def add_member(self, person):
        """
        Добавляет нового члена семьи
        """
        self.members.append(person)

    def get_oldest_member(self):
        """
        Возвращает самого старшего члена семьи
        """
        if not self.members:
            return None
        return max(self.members, key=lambda person: person.age)

    def get_family_info(self):
        """
        Возвращает информацию о всех членах семьи
        """
        info = ''
        for person in self.members:
            info += str(person) + '\n\n'
        return info


# Create some Person objects
person1 = Person('Lesia', 'Klass', 30)
person2 = Person('Liia', 'Port', 25)
person3 = Person('Igor', 'Sver', 50)
person4 = Person('Misha', 'Tyt', 45)

# Create a Family object with these persons
family = Family([person1, person2, person3, person4])

# Add a new member to the family
person5 = Person('Natalia', 'Werts', 20)
family.add_member(person5)

# Print the family information again
print(family.get_family_info())

# Get the oldest member of the family
oldest_member = family.get_oldest_member()
print(f'The oldest member of the family is {oldest_member.firstname} {oldest_member.lastname}, age {oldest_member.age}.')
