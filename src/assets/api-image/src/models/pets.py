from typing import Optional
from uuid import UUID


PETS = [
    {
        'id': UUID('8c467d62-651d-41b5-8b64-3304a49f4195'),
        'owner_id': UUID('36441454-1dd8-4266-b93d-e9b0c98266a1'),
        'name': 'Penny',
        'type': 'Dog'
    },
    {
        'id': UUID('07799b4b-2d99-4b42-b700-1918c3165a52'),
        'owner_id': UUID('36441454-1dd8-4266-b93d-e9b0c98266a1'),
        'name': 'Durant',
        'type': 'Dog'
    }
]


# TODO: Fetch pets from the database
def list_pets(owner_id: UUID = None) -> list:
    if owner_id:
        return [pet for pet in PETS if pet['owner_id'] == owner_id]
    return PETS


def get_pet(pet_id: UUID) -> Optional[dict]:
    for pet in PETS:
        if pet['id'] == pet_id:
            return pet
    return None
