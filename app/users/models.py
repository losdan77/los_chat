from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, intpk, str_not_null, str_null, created_at

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str_not_null]
    hashed_password: Mapped[str_not_null]
    role: Mapped[str_null]
    created_at: Mapped[created_at]

    chats: Mapped[list['Chats']] = relationship(back_populates='users')

    __table_args__ = (
        Index('email_index', 'email'),
    )

    def __str__(self):
        return f'{self.email}'