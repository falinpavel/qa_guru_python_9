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

#     def __hash__(self):
#         return hash((self.first_name, self.last_name, self.user_email, self.gender, self.user_number, self.birth_day,
#                      self.birth_month, self.birth_year, self.subjects, self.hobbies, self.current_address, self.state,
#                      self.city))
#
#
# class UsersForTests:
#     """
#     функция генерации тесовых пользователей на основе класса User
#     и библиотеки Faker
#     """
#
#     @staticmethod
#     def generate_users(count: int = 10) -> list[User]:
#         users = []
#         for _ in range(count):
#             _ = User(first_name=fake.first_name(),
#                      last_name=fake.last_name(),
#                      user_email=fake.unique.email(),
#                      gender=fake.random_elements(elements=('Male', 'Female', 'Other'), length=1)[0],
#                      user_number="8" + "".join([str(random.randint(0, 9)) for _ in range(9)]),
#                      birth_day=str(random.randint(a=4, b=24)),
#                      birth_month=fake.random_elements(elements=(
#                          'January', 'February', 'March', 'April', 'May',
#                          'June', 'July', 'August', 'September', 'October',
#                          'November', 'December'),
#                          length=1)[0],
#                      birth_year=str(fake.year()),
#                      subjects=list(fake.random_elements(elements=(
#                          'Maths', 'English', 'Computer Science',
#                          'Chemistry', 'Physics', 'Biology', 'Accounting',
#                          'Arts', 'Commerce', 'Economics', 'History'),
#                          length=random.randint(a=2, b=4), unique=True)),
#                      hobbies=list(fake.random_elements(elements=(
#                          'Sports', 'Music', 'Reading'), length=random.randint(a=1, b=3), unique=True)),
#                      current_address=fake.address(),
#                      # state=fake.random_elements(elements=('NCR', 'Uttar Pradesh',
#                      # 'Haryana', 'Rajasthan'), length=1)[0], TODO!!! fix
#                      state='Uttar Pradesh',
#                      city=fake.random_elements(elements=('Agra', 'Lucknow', 'Merrut'), length=1)[0])
#             users.append(_)
#         return users
#
#     def choose_random_user(self):
#         return random.choice(self.generate_users())
