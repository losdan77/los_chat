from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from app.exception import TooMuchChatsException, NotUniqueNameChatException
from app.chats.dao import ChatsDAO
from app.users.models import Users
from app.users.dependecies import get_current_user

router = APIRouter(
    prefix='/chats',
    tags=['Чаты']
)

@router.post('/create_chat')
async def create_chat(name: str,
                      current_user: Users = Depends(get_current_user)):
    mass_name_chats = []
    chats = await ChatsDAO.find_all(id_user = current_user['id'])
    for chat in chats:
        mass_name_chats.append(chat['name'])

    if len(chats) >= 10:
        raise TooMuchChatsException
    if name in mass_name_chats:
        raise NotUniqueNameChatException
    await ChatsDAO.add(name=name,
                        id_user = current_user['id'])

@router.get('/user_chats')
@cache(expire=60)
async def get_user_chats(current_user: Users = Depends(get_current_user)):
    chats = await ChatsDAO.find_all(id_user = current_user['id'])
    return chats

@router.delete('/delete_chat')
async def delete_chat(id_chat: int,
                      current_user: Users = Depends(get_current_user)):
    await ChatsDAO.delete(id = id_chat,
                          id_user = current_user['id'])
    