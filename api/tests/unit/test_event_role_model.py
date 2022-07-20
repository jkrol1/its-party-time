import pytest

from app.event.models import EventRole
from app.event.roles import EventPermission, Role


@pytest.fixture(autouse=True)
def add_event_roles(test_client):
    EventRole.add_roles()


def test_add_roles():
    added_roles = EventRole.query.all()
    matched_roles = []
    for added_role in added_roles:
        for role in Role:
            if added_role.name == role.name:
                assert added_role.permissions == sum(role.value)
                matched_roles.append(added_role)

    assert len(matched_roles) == len(Role)


def test_add_permission():
    moderator = EventRole.query.filter_by(name="MODERATOR").scalar()
    moderator.add_permission(EventPermission.DELETE_EVENT)
    assert moderator.has_permission(EventPermission.DELETE_EVENT)


def test_remove_permission():
    moderator = EventRole.query.filter_by(name="MODERATOR").scalar()
    moderator.remove_permission(EventPermission.MODERATE)
    assert not moderator.has_permission(EventPermission.MODERATE)


def test_reset_permission():
    user = EventRole.query.filter_by(name="USER").scalar()
    user.reset_permissions()
    assert user.permissions == 0
    for permission in EventPermission:
        assert not user.has_permission(permission.value)


def test_has_permission():
    moderator = EventRole.query.filter_by(name="MODERATOR").scalar()
    assert moderator.has_permission(EventPermission.CONTRIBUTE)
    assert moderator.has_permission(EventPermission.MODERATE)
    assert not moderator.has_permission(123)
    assert not moderator.has_permission(EventPermission.DELETE_EVENT)
