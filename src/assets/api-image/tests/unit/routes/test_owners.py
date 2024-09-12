from src.routes.schemas import ListOwnersResponse, Owner, ListPetsResponse


def test_list_owners(client):
    response = client.get('/owners')
    assert response.status_code == 200
    ListOwnersResponse.model_validate(response.json)


def test_get_owner(client):
    response = client.get('/owners/36441454-1dd8-4266-b93d-e9b0c98266a1')
    assert response.status_code == 200
    Owner.model_validate(response.json)


def test_get_owner_pets(client):
    response = client.get('/owners/36441454-1dd8-4266-b93d-e9b0c98266a1/pets')
    assert response.status_code == 200
    ListPetsResponse.model_validate(response.json)
