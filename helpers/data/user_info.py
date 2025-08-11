import random

from dataclasses import dataclass, field
from faker import Faker

fake = Faker('ru_RU')


@dataclass
class User:
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    user_email: str = fake.unique.email()
    gender: str = random.choice(['Male', 'Female', 'Other'])
    user_number: str = f"8{''.join(str(random.randint(0, 9)) for _ in range(9))}"
    birth_day: str = str(random.randint(a=4, b=24))
    birth_month: str = random.choice([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    birth_year: str = str(fake.year())
    subjects: list = field(default_factory=lambda: random.sample([
        'Maths', 'English', 'Computer Science', 'Chemistry',
        'Physics', 'Biology', 'Accounting', 'Arts',
        'Commerce', 'Economics', 'History'
    ], k=random.randint(2, 4)))
    hobbies: list = field(default_factory=lambda: random.sample(
        ['Sports', 'Music', 'Reading'], k=random.randint(a=1, b=2)))
    current_address: str = fake.address()
    state: str = 'Uttar Pradesh'
    city: str = random.choice(['Agra', 'Lucknow', 'Merrut'])
