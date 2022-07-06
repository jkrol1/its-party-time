from app.user import User

from tests.fake import FakeInputData


def test_user_password_hashing(fake_input_data: FakeInputData) -> None:
    fake_user = fake_input_data.user
    user = User(**fake_user.to_dict())
    assert user.verify_password(fake_user.password)
