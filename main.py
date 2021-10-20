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


cards = []
for i in range(5):
    cards.append(Card(f.first_name(), f.last_name(), f.company(), f.job(), f.email()))
    print(cards[i])


def print_by_order(cards, func):
    ordered_cards = sorted(cards, key=func)
    for element in ordered_cards:
        print(element)


print_by_order(cards, lambda x: x.name)
print_by_order(cards, lambda x: x.surname)
print_by_order(cards, lambda x: x.email)

print()
for card in cards:
    print(card)
    print(card.contact())
    print(card.len)
