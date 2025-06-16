from faker import Faker

faker = Faker('ru_RU')

def generate_personal_data():
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

class FakeData:
    @staticmethod
    def name():
        fake = Faker()
        name = fake.first_name()
        return name

    @staticmethod
    def email():
        fake = Faker()
        email = fake.email()
        return email

    @staticmethod
    def password():
        fake = Faker()
        password = fake.password(length=6)
        return password



