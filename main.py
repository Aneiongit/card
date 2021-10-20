from faker import Faker

f = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'

    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}.'

    @property
    def len(self):
        return f'{len(self.name)} {len(self.surname)}'


class BusinessContact(BaseContact):
    def __init__(self, company_name, occupation, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.occupation = occupation
        self.work_phone = work_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email} {self.company_name} ' \
               f'{self.occupation} {self.work_phone}'

    def contact(self):
        return f'Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}'

    @property
    def len(self):
        return f'{len(self.name)} {len(self.surname)}'


def create_contacts(type, cards):
    card = []
    if type == "base":
        for i in range(cards):
            card.append(BaseContact(f.first_name(), f.last_name(), f.phone_number(), f.email()))
            print(card[i])
            print()

    elif type == "business":
        for i in range(cards):
            card.append(BusinessContact(f.job(), f.company(), f.phone_number(), f.first_name(), f.last_name(),
                                        f.phone_number(), f.email()))
            print(card[i])

    else:
        print("Podano nieprawidlowy typ.")


type = input("Podaj typ (base or business): ")
cards = int(input("Podaj ilość: "))
print(create_contacts(type, cards))

