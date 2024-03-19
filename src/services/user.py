from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork


class UserService(BaseService):
    base_repository: str = 'user'

    @classmethod
    async def get_path_by_uuid(
            cls,
            uow: UnitOfWork,
            user_uuid: str
    ) -> str:
        async with uow:
            path: str = await uow.user.get_path_by_uuid(user_uuid=user_uuid)
            return path
