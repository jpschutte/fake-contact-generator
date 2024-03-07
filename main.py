import uuid
import csv
from faker import Faker
import random
import concurrent.futures

fake = Faker()

def generate_contact(_):
    return {
        'id': str(uuid.uuid4()),
        'username': fake.user_name(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'cellphone_number': '27' + str(random.choice([6, 7, 8, 9])) + fake.numerify(text='#######'),
        'telephone_number': '271' + str(random.choice([1, 2])) + fake.numerify(text='######'),
    }

def generate_contacts(x, filename):
    fieldnames = ['id', 'username', 'first_name', 'last_name', 'cellphone_number', 'telephone_number']
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        with concurrent.futures.ThreadPoolExecutor():
            for _ in range(x):
                contact = generate_contact(_)
                writer.writerow(contact)

generate_contacts(3000000, 'contacts.csv')