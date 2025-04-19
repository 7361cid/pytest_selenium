import random
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from data.data import Person, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
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
    phone = faker_ru.msisdn()
    yield Person(full_name=full_name, first_name=first_name, last_name=last_name, email=email,
                 current_address=current_address, age=age, department=department, salary=salary,
                 permanent_address=permanent_address, phone=phone)

def generated_file():
    current_dir = Path(__file__).parent
    path = os.path.join(current_dir, "text.txt")
    file = open(path, "w+")
    file.write(f"Some Text{random.randint(1, 100)}")
    file.close()
    return path

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)
def generated_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 1, 1)
    return str(random_date(start_date, end_date))[:-9]

def format_date(date):
    '''
    '2020-02-01' to '01 February,2020'
    '''
    MONTH = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
             '08': 'August ', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    return f"{date[-2:]} {MONTH[date[5:7]]},{date[:4]}"

def get_random_color():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black']
    return random.sample(colors, 3)

def get_date():
    return Date(year=str(random.randint(2022, 2027)), month=faker_en.month_name(), day=faker_en.day_of_month(),
                time="12:00")
