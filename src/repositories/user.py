from src.models import UserModel
from src.utils.repository import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository):
    model = UserModel

    async def get_path_by_uuid(self, user_uuid: str) -> str:
        result = []
        user: UserModel = await self.get_by_query_one_or_none(uuid=user_uuid)
        path_ids = str(user.path).split('.')
        for _id in path_ids:
            _user: UserModel = await self.get_by_query_one_or_none(id=int(_id))
            result.append(_user.uuid)
        return '.'.join(result)
