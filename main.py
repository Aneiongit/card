from faker import Faker
f = Faker()


class Card:
    def __init__(self, name, surname, company_name, occupation, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.occupation = occupation
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Company name: {self.company_name}, " \
               f"Occupation: {self.occupation}, E-mail address: {self.email}"


name_cards = []
for i in range(5):
    name_cards.append(Card(f.first_name(), f.last_name(), f.company(), f.job(), f.email()))
    print(name_cards[i])
