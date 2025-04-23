import os
import uuid
from dotenv import load_dotenv
load_dotenv()

from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from database import database
from models import users
from schemas import UserCreate, UserLogin, TokenResponse

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-chave-fraca")
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 60

def create_token(email: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register")
async def register(user: UserCreate):
    existing = await database.fetch_one(users.select().where(users.c.email == user.email))
    if existing:
        raise HTTPException(status_code=400, detail="Email já registrado")

    user_id = str(uuid.uuid4())
    hashed_password = pwd_context.hash(user.password)
    query = users.insert().values(
        id=user_id,
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )
    await database.execute(query)
    return {"message": "Usuário registrado com sucesso"}

@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    db_user = await database.fetch_one(users.select().where(users.c.email == user.email))
    if not db_user or not pwd_context.verify(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token(db_user["email"])
    return {"access_token": token, "token_type": "bearer"}
