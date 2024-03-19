from typing import Any

from sqlalchemy.orm import relationship, remote, foreign
from sqlalchemy import Index, func, Column, String, Integer, Sequence
from sqlalchemy_utils import LtreeType, Ltree

from src.models import BaseModel
from src.schemas.user import UserSchema

id_seq = Sequence('user_id_seq')


class UserModel(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, id_seq, primary_key=True)
    uuid = Column(String, nullable=False, unique=True)
    path = Column(LtreeType, nullable=False)

    parent = relationship(
        'UserModel',
        primaryjoin=remote(path) == foreign(func.subpath(path, 0, -1)),
        backref='children',
        viewonly=True,
    )

    __table_args__ = (
        Index('ix_user_path', path, postgresql_using="gist"),
    )

    def __init__(self, _id, _uuid: str, _parent=None, **kw: Any):
        super().__init__(**kw)
        self.id = _id
        self.uuid = _uuid
        ltree_id = Ltree(str(_id))
        self.path = ltree_id if _parent is None else _parent.path + ltree_id

    def to_pydantic_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            uuid=self.uuid,
            path=self.path,
        )
