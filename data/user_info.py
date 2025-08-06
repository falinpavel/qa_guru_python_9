import random

from dataclasses import dataclass
from faker import Faker

fake = Faker('ru_RU')


@dataclass
class User:

    first_name: str
    last_name: str
    user_email: str
    gender: str
    user_number: str
    subjects: list
    hobbies: list
    current_address: str

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.user_email,
                     self.gender, self.user_number, self.current_address))


class UsersForTests:
    """
    функция генерации тесовых пользователей на основе класса User
    и библиотеки Faker
    """

    @staticmethod
    def generate_users(count: int = 10) -> list[User]:
        users = []
        for _ in range(count):
            _ = User(first_name=fake.first_name(),
                     last_name=fake.last_name(),
                     user_email=fake.unique.email(),
                     gender=fake.random_elements(elements=('Male', 'Female', 'Other'), length=1)[0],
                     user_number="8" + "".join([str(random.randint(0, 9)) for _ in range(9)]),
                     subjects=list(fake.random_elements(elements=('Maths', 'English', 'Computer Science',
                                                                  'Chemistry', 'Physics', 'Biology', 'Accounting',
                                                                  'Arts', 'Commerce', 'Economics', 'History'),
                                                        length=random.randint(a=1, b=4))),
                     hobbies=list(fake.random_elements(elements=('Sports', 'Music', 'Reading'),
                                                       length=random.randint(a=1, b=2))),
                     current_address=fake.address())
            users.append(_)
        return users

    def choose_random_user(self):
        return random.choice(self.generate_users())
