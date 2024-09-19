from fastapi import APIRouter, Response, Depends
from password_generator import PasswordGenerator
from app.users.schemas import SUserRegistr, SUserLogin
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, authentficate_user, create_access_token
from app.users.models import Users
from app.users.dependecies import get_current_user
from app.exception import ShortPasswordException, HasExistingUserException
from app.exception import PasswordException
from app.tasks.tasks import send_password_email

router = APIRouter(
    prefix='/auth',
    tags=['Пользователи']
)

@router.post('/registr')
async def registr_user(user_data: SUserRegistr):
    pwo = PasswordGenerator()
    random_password = pwo.non_duplicate_password(8)
    # if len(user_data.password) < 5:
    #     raise ShortPasswordException
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HasExistingUserException
    hashed_password = get_password_hash(random_password)
    await UsersDAO.add(email = user_data.email,
                       username = user_data.username,
                       hashed_password = hashed_password,
                       role = None)
    
    send_password_email.delay(user_data.email,
                              random_password)
    
@router.post('/login')
async def login_user(response: Response, user_data: SUserLogin):
    user = await authentficate_user(user_data.email,
                                    user_data.password)
    if not user:
        raise PasswordException
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')

@router.post('/me')
async def me_user(current_user: Users = Depends(get_current_user)):
    return current_user