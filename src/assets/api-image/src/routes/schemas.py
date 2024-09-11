from uuid import UUID

from pydantic import BaseModel


class Resource(BaseModel):
    id: UUID
    links: dict[str, str]


class ResourceListResponse(BaseModel):
    resources: list[Resource]
    links: dict[str, str]


class OwnerLinks(BaseModel):
    pets: str
    self: str


class Owner(Resource):
    id: UUID
    name: str
    links: OwnerLinks


class ListOwnersResponse(ResourceListResponse):
    resources: list[Owner]


class PetLinks(BaseModel):
    owner: str
    self: str


class Pet(Resource):
    name: str
    type: str
    links: PetLinks


class ListPetsResponse(ResourceListResponse):
    resources: list[Pet]


class IndexResponse(BaseModel):
    links: dict[str, str]
