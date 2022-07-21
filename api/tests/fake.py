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
class FakeEvent(ToDictMixin):
    title: str = fake.text(max_nb_chars=124)
    description: str = fake.text(max_nb_chars=372)
    address: str = fake.address()
    latitude: float = fake.latitude()
    longitude: float = fake.longitude()
    playlist_link: str = fake.url()


@dataclass
class FakeInputData:
    user: FakeUser = FakeUser()
    event: FakeEvent = FakeEvent()
