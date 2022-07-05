from typing import Dict

from faker import Faker

fake = Faker()


def get_fake_user_post_request_body() -> Dict[str, str]:
    return {
        "username": fake.name(),
        "password": fake.password(),
        "email": fake.email()
    }
