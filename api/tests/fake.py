from dataclasses import dataclass, asdict

from faker import Faker

fake = Faker()


class ToDictMixin:
    def to_dict(self):
        return asdict(self)


@dataclass
class FakeUser(ToDictMixin):
    username: str = fake.name()
    password: str = fake.password()
    email: str = fake.email()


@dataclass
class FakeInputData:
    user: FakeUser = FakeUser()
