from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, intpk, str_not_null

class Messages(Base):
    __tablename__ = 'messages'

    id: Mapped[intpk]
    text: Mapped[str_not_null]
    user_author: Mapped[bool] = mapped_column(nullable=False)
    id_chat: Mapped[int] = mapped_column(ForeignKey('chats.id'))

    chat: Mapped[list['Chats']] = relationship(back_populates='messages')

    __table_args__ = (
        Index('index_chat', 'id_chat'),
    )

    def __str__(self):
        return f'{self.text[:20]} in {self.chat}'