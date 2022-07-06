from app.user import User

from tests.fake import FakeInputData


def test_user_password_hashing(fake_input_data: FakeInputData) -> None:
    user = User(**fake_input_data.user.to_dict())
    assert user.verify_password(fake_input_data.user.password)
