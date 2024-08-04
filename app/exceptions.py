from fastapi import status, HTTPException

UserAlreadyExistsException = HTTPException(status_code=status.HTTP_409_CONFLICT,
                                           detail='User already exists')

IncorrectEmailOrPasswordException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                                  detail='Invalid email or password')

TokenExpiredException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                      detail='Token has expired')

TokenNoFound = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail='Token has expired')

NoJwtException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                               detail='The token is not valid!')

NoUserIdException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                  detail='User ID not found')

ForbiddenException = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not enough rights!')