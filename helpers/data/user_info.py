import random
from dataclasses import dataclass
from enum import Enum

from faker import Faker

fake = Faker('ru_RU')


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class BirthMonth(Enum):
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'


class Subjects(Enum):
    MATHS = 'Maths'
    ENGLISH = 'English'
    COMPUTER_SCIENCE = 'Computer Science'
    CHEMISTRY = 'Chemistry'
    PHYSICS = 'Physics'
    BIOLOGY = 'Biology'
    ACCOUNTING = 'Accounting'
    ARTS = 'Arts'
    COMMERCE = 'Commerce'
    ECONOMICS = 'Economics'
    HISTORY = 'History'


class Hobbies(Enum):
    SPORTS = 'Sports'
    MUSIC = 'Music'
    READING = 'Reading'


@dataclass
class User:
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    user_email = fake.unique.email(),
    gender = fake.random_elements(elements=(Gender.MALE, Gender.FEMALE, Gender.OTHER), length=1)[0],
    user_number = "8" + "".join([str(random.randint(0, 9)) for _ in range(9)]),
    birth_day = str(random.randint(a=4, b=28)),
    birth_month = fake.random_elements(elements=(
        BirthMonth.JANUARY, BirthMonth.FEBRUARY, BirthMonth.MARCH, BirthMonth.APRIL, BirthMonth.MAY,
        BirthMonth.JUNE, BirthMonth.JULY, BirthMonth.AUGUST, BirthMonth.SEPTEMBER, BirthMonth.OCTOBER,
        BirthMonth.NOVEMBER, BirthMonth.DECEMBER),
        length=1)[0],

    birth_year = str(fake.year()),
    subjects = list(fake.random_elements(elements=(
        Subjects.MATHS, Subjects.ENGLISH, Subjects.COMPUTER_SCIENCE, Subjects.CHEMISTRY, Subjects.PHYSICS,
        Subjects.BIOLOGY, Subjects.ACCOUNTING, Subjects.ARTS, Subjects.COMMERCE, Subjects.ECONOMICS, Subjects.HISTORY),
        length=random.randint(a=2, b=4))),
    hobbies = list(fake.random_elements(elements=(
        Hobbies.MUSIC, Hobbies.SPORTS, Hobbies.READING), length=random.randint(a=1, b=2))),
    current_address = fake.address(),
    state = 'Uttar Pradesh',
    city = fake.random_elements(elements=('Agra', 'Lucknow', 'Merrut'), length=1)[0]

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.user_email, self.gender, self.user_number, self.birth_day,
                     self.birth_month, self.birth_year, self.subjects, self.hobbies, self.current_address, self.state,
                     self.city))

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
#                      birth_day=str(random.randint(a=4, b=28)),
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
#                          length=random.randint(a=2, b=4))),
#                      hobbies=list(fake.random_elements(elements=(
#                          'Sports', 'Music', 'Reading'), length=random.randint(a=1, b=2))),
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
