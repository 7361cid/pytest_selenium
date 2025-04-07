import random
import os

from pathlib import Path
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    full_name = f"{faker_ru.last_name()} {faker_ru.first_name()} {faker_ru.middle_name()}"
    first_name = faker_ru.first_name()
    last_name = faker_ru.last_name()
    email = faker_ru.email()
    age = random.randint(19, 80)
    salary = random.randint(10000, 200000)
    department = faker_ru.job()
    current_address = faker_ru.address()
    permanent_address = faker_ru.address()
    yield Person(full_name=full_name, first_name=first_name, last_name=last_name, email=email,
                 current_address=current_address, age=age, department=department, salary=salary,
                 permanent_address=permanent_address)

def generated_file():
    current_dir = Path(__file__).parent
    path = os.path.join(current_dir, "text.txt")
    file = open(path, "w+")
    file.write(f"Some Text{random.randint(1, 100)}")
    file.close()
    return path
