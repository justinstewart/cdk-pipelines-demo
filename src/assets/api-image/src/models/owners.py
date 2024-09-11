from typing import Optional
from uuid import UUID

OWNERS = [
    {
        'id': UUID('36441454-1dd8-4266-b93d-e9b0c98266a1'),
        'name': 'Justin'
    }
]


def list_owners() -> list:
    return OWNERS


def get_owner(owner_id: UUID) -> Optional[dict]:
    for owner in OWNERS:
        if owner['id'] == owner_id:
            return owner
    return None
