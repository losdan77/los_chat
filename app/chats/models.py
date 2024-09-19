from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, intpk, str_not_null

class Chats(Base):
    __tablename__ = 'chats'

    id: Mapped[intpk]
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str_not_null]

    users: Mapped[list['Users']] = relationship(back_populates='chats')
    messages: Mapped[list['Messages']] = relationship(back_populates='chats')

    __table_args__ = (
        Index('index_user', 'id_user'),
    )

    def __str__(self):
        return f'{self.name} by {self.users}'