from uuid import UUID

from flask import Blueprint, jsonify, url_for

from ..models.owners import get_owner as _get_owner, list_owners as _list_owners
from ..models.pets import list_pets
from . import schemas as s

blueprint = Blueprint('owners', __name__)


@blueprint.route('/owners', methods=['GET'])
def list_owners():
    owner_models = _list_owners()
    owners = [s.Owner(
        id=owner['id'],
        name=owner['name'],
        links=s.OwnerLinks(
            pets=url_for('owners.get_owner_pets', owner_id=owner['id'], _external=False),
            self=url_for('owners.get_owner', owner_id=owner['id'], _external=False)
        )
    ) for owner in owner_models]
    return jsonify(s.ListOwnersResponse(
        resources=owners,
        links=dict(
            self=url_for('owners.list_owners', _external=False)
        )
    ).dict())


@blueprint.route('/owners/<uuid:owner_id>', methods=['GET'])
def get_owner(owner_id: UUID):
    owner = _get_owner(owner_id)
    if owner is None:
        return jsonify({'error': 'Not Found'}), 404
    return jsonify(s.Owner(
        id=owner['id'],
        name=owner['name'],
        links=s.OwnerLinks(
            pets=url_for('owners.get_owner_pets', owner_id=owner['id'], _external=False),
            self=url_for('owners.get_owner', owner_id=owner['id'], _external=False)
        )
    ).dict())


@blueprint.route('/owners/<uuid:owner_id>/pets', methods=['GET'])
def get_owner_pets(owner_id: UUID):
    owner = _get_owner(owner_id)
    if owner is None:
        return jsonify({'error': 'Not Found'}), 404
    pet_models = list_pets(owner_id=owner_id)
    pets = [s.Pet(
        id=pet['id'],
        name=pet['name'],
        type=pet['type'],
        links=s.PetLinks(
            owner=url_for('owners.get_owner', owner_id=owner_id, _external=False),
            self=url_for('pets.get_pet', pet_id=pet['id'], _external=False)
        )
    ) for pet in pet_models]
    return jsonify(s.ListPetsResponse(
        resources=pets,
        links=dict(
            self=url_for('owners.get_owner_pets', owner_id=owner_id, _external=False)
        )
    ).dict())
