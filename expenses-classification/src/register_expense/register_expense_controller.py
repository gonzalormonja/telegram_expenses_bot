from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from register_expense.register_expense_service import RegisterExpenseService
from typing import Annotated
from pydantic import BaseModel
import jwt
import os


class User(BaseModel):
    id: int
    telegram_id: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = jwt.decode(token, os.environ.get(
        "JWT_SECRET"), algorithms=['HS256'])

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

app = FastAPI()


@app.post('/api/v1/register_expense')
async def handle_post_request(data: dict,
                              current_user: Annotated[User, Depends(get_current_user)]):
    service = RegisterExpenseService()
    try:
        response = service.save_expense(current_user['id'], data['text'])
    except Exception as e:
        if str(e) == 'User not found':
            return {
                'success': False,
                'message': ''
            }
        if str(e) == 'The message is not an expense':
            return {
                'success': False,
                'message': ''
            }
        print(e)
    return {
        'success': True,
        'message': f'{response["category"]} expense added ✅'
    }
