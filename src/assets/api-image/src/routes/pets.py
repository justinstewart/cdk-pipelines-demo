from uuid import UUID

from flask import Blueprint, jsonify, url_for

from ..models.pets import get_pet as _get_pet, list_pets as _list_pets
from . import schemas as s

blueprint = Blueprint('pets', __name__)


@blueprint.route('/pets', methods=['GET'])
def list_pets():
    pet_models = _list_pets()
    pets = [s.Pet(
        id=pet['id'],
        name=pet['name'],
        type=pet['type'],
        links=s.PetLinks(
            owner=url_for('owners.get_owner', owner_id=pet['owner_id'], _external=False),
            self=url_for('pets.get_pet', pet_id=pet['id'], _external=False)
        )
    ) for pet in pet_models]
    return jsonify(s.ListPetsResponse(
        resources=pets,
        links=dict(
            self=url_for('pets.list_pets', _external=False)
        )
    ).dict())


@blueprint.route('/pets/<uuid:pet_id>', methods=['GET'])
def get_pet(pet_id: UUID):
    pet = _get_pet(pet_id)
    if pet is None:
        return jsonify({'error': 'Not Found'}), 404
    return jsonify(s.Pet(
        id=pet['id'],
        name=pet['name'],
        type=pet['type'],
        links=s.PetLinks(
            owner=url_for('owners.get_owner', owner_id=pet['owner_id'], _external=False),
            self=url_for('pets.get_pet', pet_id=pet['id'], _external=False)
        )
    ).dict())
