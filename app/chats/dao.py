from app.dao.base import BaseDAO
from app.chats.models import Chats

class ChatsDAO(BaseDAO):
    model = Chats