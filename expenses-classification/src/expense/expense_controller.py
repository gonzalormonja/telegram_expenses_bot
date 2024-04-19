from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from expense.expense_service import ExpenseService
from typing import Annotated
from pydantic import BaseModel
import jwt
import os


class User(BaseModel):
    """
    User model with the attributes id and telegram_id.
    """
    id: int
    telegram_id: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Validate the token and return the user data.
    """
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


@app.post('/api/v1/expense')
async def expense(data: dict,
                  current_user: Annotated[User, Depends(get_current_user)]):
    """
    Endpoint POST that receives as parameter an object with the attribute text
    that will get the category and amount of the expense entered.
    """
    service = ExpenseService()
    try:
        response = service.save_expense(current_user['id'], data['text'])
    except Exception as e:
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
