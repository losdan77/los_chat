from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from app.exception import TooMuchMessagesInChatException
from app.users.dependecies import get_current_user
from app.users.models import Users
from app.messages.dao import MessagesDAO

router = APIRouter(
    prefix='/messages',
    tags=['Сообщения']
)


@router.post('/add')
async def add_message(text: str,
                      id_chat: int,
                      current_user: Users = Depends(get_current_user)):
    messages = await MessagesDAO.find_all(id_chat = id_chat)
    if len(messages) >= 100:
        raise TooMuchMessagesInChatException

    await MessagesDAO.add(text = text,
                          id_chat = id_chat,
                          user_author = True)

    bot_answer = 'Ok'
    await MessagesDAO.add(text = bot_answer,
                          id_chat = id_chat,
                          user_author = False)

@router.get('/show_all')
@cache(expire=60)
async def get_all_messages(id_chat: int,
                           current_user: Users = Depends(get_current_user)):
    messages = await MessagesDAO.find_all(id_chat = id_chat)
    return messages     
   
    