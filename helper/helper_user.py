from faker import Faker


def create_fake_first_name():
    faker = Faker()
    return faker.first_name()

def create_fake_last_name():
    faker = Faker()
    return faker.last_name()

def create_fake_user_name():
    faker = Faker()
    return faker.user_name()

def create_fake_email():
    faker = Faker()
    return faker.free_email()

def create_fake_password():
    faker = Faker()
    return faker.password()
