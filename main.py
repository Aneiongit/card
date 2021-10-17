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
        return f'{self.name} {self.surname} {self.email}'

    def contact(self):
        return f'Kontaktuje sie z {self.name} {self.surname} {self.occupation} {self.email}'

    @property
    def len(self):
        return f'{len(self.name)} {len(self.surname)}'


c1 = Card(name=f.first_name(), surname=f.last_name(), company_name=f.company(), occupation=f.job(), email=f.email())
c2 = Card(name=f.first_name(), surname=f.last_name(), company_name=f.company(), occupation=f.job(), email=f.email())
c3 = Card(name=f.first_name(), surname=f.last_name(), company_name=f.company(), occupation=f.job(), email=f.email())
c4 = Card(name=f.first_name(), surname=f.last_name(), company_name=f.company(), occupation=f.job(), email=f.email())
c5 = Card(name=f.first_name(), surname=f.last_name(), company_name=f.company(), occupation=f.job(), email=f.email())

cards = [c1, c2, c3, c4, c5]

by_name = sorted(cards, key=lambda card: card.name)
by_surname = sorted(cards, key=lambda card: card.surname)
by_email = sorted(cards, key=lambda card: card.email)

for card in cards:
    print(card)
    print(card.contact())
    print(card.len)

