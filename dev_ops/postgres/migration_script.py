import asyncio
import json

from src.database.db import async_session_maker, async_engine
from src.models import UserModel
from src.models.user import id_seq


async def parse_metadata(metadata: list[dict], parent: UserModel | None = None) -> None:
    for _dict in metadata:
        async with async_engine.begin() as conn:
            _id = await conn.execute(id_seq)

        async with async_session_maker() as session:
            new_user = UserModel(_id=_id, _uuid=_dict.get('uuid'), _parent=parent)
            session.add(new_user)
            await session.commit()

        _children = _dict.get('children')
        if _children:
            await parse_metadata(_children, parent=new_user)


async def make_migrate():
    print('--------------------------- START MIGRATION ---------------------------\n')
    with open('structure.json') as f:
        metadata = json.load(f)
    await parse_metadata(metadata)
    print('--------------------------- STOP MIGRATION ----------------------------\n')


if __name__ == '__main__':
    asyncio.run(make_migrate())
