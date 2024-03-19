from fastapi import APIRouter, Depends

from src.services.user import UserService
from src.utils.unit_of_work import UnitOfWork

router = APIRouter(prefix='/user')


@router.post('/get_path')
async def get_user_path(user_uuid: str, uow: UnitOfWork = Depends(UnitOfWork)):
    path: str = await UserService.get_path_by_uuid(uow=uow, user_uuid=user_uuid)
    return path
