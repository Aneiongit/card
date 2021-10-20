from faker import Faker
fake = Faker()


class Card:
    def __init__(self, name, surname, buisness, position, mail):
        self.name = name
        self.surname = surname
        self.buisness = buisness
        self.position = position
        self.mail = mail

    def __str__(self):
        return f"imie: {self.name} nazwisko: {self.surname} firma: {self.buisness} stanowisko: {self.position} mail: {self.mail}"

    def contact(self):
        return f"Kontaktuje się z {self.name} {self.surname} {self.mail}"

    @property
    def name_surname(self):
        return len(f"{self.name} {self.surname}")

businessCardList = []
for i in range(5):
    businessCardList.append(Card(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email()))
    print(businessCardList[i])

print()
by_name = sorted(businessCardList, key=lambda card: card.name)
for i in range(5):
    print(by_name[i])

print()
by_surname = sorted(businessCardList, key=lambda card: card.surname)
for i in range(5):
    print(by_surname[i])

print()
by_email = sorted(businessCardList, key=lambda card: card.mail)
for i in range(5):
    print(by_email[i])

print()
for i in range(5):
    print(businessCardList[i].contact())

print()
for z in range(5):
    print(businessCardList[z].name_surname)

