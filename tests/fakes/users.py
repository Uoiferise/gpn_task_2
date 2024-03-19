from sqlalchemy_utils import Ltree

from src.schemas.user import UserSchema

FAKE_USERS: list[UserSchema] = [
    UserSchema(
        id=1,
        uuid='a-a-a',
        path=Ltree('1')
    ),
    UserSchema(
        id=2,
        uuid='a-b-b',
        path=Ltree('1.2')
    ),
    UserSchema(
        id=3,
        uuid='a-b-c',
        path=Ltree('1.2.3')
    ),
]
