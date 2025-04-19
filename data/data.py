from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    full_name: str = None
    age: int = None
    department: str = None
    salary: int = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    phone: str = None

@dataclass
class Date:
    year: str = None
    month: str = None
    day: str = None
    time: str = None
