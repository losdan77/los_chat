from app.dao.base import BaseDAO
from app.messages.models import Messages

class MessagesDAO(BaseDAO):
    model = Messages