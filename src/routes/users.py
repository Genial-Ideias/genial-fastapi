from fastapi import APIRouter
from typing import List
from uuid import uuid4

from src.models.user_models import UserModel, CreateUserModel
from src.services.create_user_service import CreateUserService
from src.services.list_user_service import ListUserSerive

router = APIRouter(
    prefix='/users',
    tags=['users']
)

users = [
    {
        "uuid": "cfbb3a10-849a-46ea-bde6-78e7f02ad2cf",
        "email": "pinheiro@email.com",
        "password": "pinheiro123"
    },
    {
        "uuid": "e3b7dac9-4827-41c5-b71a-c4fe24c2acfd",
        "email": "leo@email.com",
        "password": "leo123"
    }
]


@router.get('/', response_model=List[UserModel])
def list_users():
    service = ListUserSerive()
    return service.list_users()


@router.post('/', response_model=UserModel)
def create_user(create_user_model: CreateUserModel):
    service = CreateUserService()
    return service.create(create_user_model)
