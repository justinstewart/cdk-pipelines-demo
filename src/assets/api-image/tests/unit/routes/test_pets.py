from src.routes.schemas import ListPetsResponse, Pet


def test_list_pets(client):
    response = client.get('/pets')
    assert response.status_code == 200
    ListPetsResponse.model_validate(response.json)


def test_get_pet(client):
    response = client.get('/pets/8c467d62-651d-41b5-8b64-3304a49f4195')
    assert response.status_code == 200
    Pet.model_validate(response.json)
