from typing import Dict

from app.event.models import EventRole
from app.event.roles import EventPermission, Role


def test_add_roles(event_roles: Dict[Role, EventRole]) -> None:
    matched_roles = []
    for added_role in event_roles.values():
        for role in Role:
            if added_role.name == role:
                assert added_role.permissions == sum(role.value)
                matched_roles.append(added_role)

    assert len(matched_roles) == len(Role)


def test_add_permission(event_roles: Dict[Role, EventRole]) -> None:
    user = event_roles[Role.USER]
    user.add_permission(EventPermission.DELETE_EVENT)
    assert user.has_permission(EventPermission.DELETE_EVENT)


def test_remove_permission(event_roles: Dict[Role, EventRole]) -> None:
    moderator = event_roles[Role.MODERATOR]
    moderator.remove_permission(EventPermission.MODERATE)
    assert not moderator.has_permission(EventPermission.MODERATE)


def test_reset_permission(event_roles: Dict[Role, EventRole]) -> None:
    moderator = event_roles[Role.MODERATOR]
    moderator.reset_permissions()
    assert moderator.permissions == 0
    for permission in EventPermission:
        assert not moderator.has_permission(permission.value)


def test_has_permission(event_roles: Dict[Role, EventRole]) -> None:
    moderator = event_roles[Role.MODERATOR]
    assert moderator.has_permission(EventPermission.CONTRIBUTE)
    assert moderator.has_permission(EventPermission.MODERATE)
    assert not moderator.has_permission(123)
    assert not moderator.has_permission(EventPermission.DELETE_EVENT)
