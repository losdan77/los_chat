from fastapi import status, HTTPException

PasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверный логин или пароль',
)

NoAuthorization = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Пользователь неавторизован',
)

UserTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверный токен',
)

ShortPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Слишком короткий пароль',
)

HasExistingUserException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Такой пользователь уже существует',
)

TooMuchChatsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Один пользователь может иметь максимум 10 чатов'
)

NotUniqueNameChatException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Придумайте уникальное имя для чата'
)

TooMuchMessagesInChatException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Слишком много сообщений для одного чата'
)