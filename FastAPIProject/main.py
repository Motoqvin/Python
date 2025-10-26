import sqlite3

import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta

SECRET = "secret"
ALGO = "HS256"
TOKEN_EXPIRE = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

conn.commit()
conn.close()


class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str



def create_access_token(user_id: int):
    expire = datetime.now() + timedelta(minutes=TOKEN_EXPIRE)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def get_user_by_username(username: str):
    con = sqlite3.connect("users.db")
    curs = con.cursor()
    curs.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
    row = curs.fetchone()
    con.close()
    return row

def get_user_by_id(user_id: int):
    con = sqlite3.connect("users.db")
    curs = con.cursor()
    curs.execute("SELECT id, username, password FROM users WHERE id = ?", (user_id,))
    row = curs.fetchone()
    con.close()
    return row

def create_user(username: str, password: str):
    con = sqlite3.connect("users.db")
    curs = con.cursor()
    curs.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    con.commit()
    user_id = curs.lastrowid
    con.close()
    return user_id
app = FastAPI()


@app.post("/register", response_model=UserOut)
def register(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    user_id = create_user(user.username, user.password)
    return {"id": user_id, "username": user.username}

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = get_user_by_username(form_data.username)
    if not db_user or not pwd_context.verify(form_data.password, db_user[2]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(db_user[0])
    return {"access_token": token, "token_type": "bearer"}


@app.post("/me", response_model=UserOut)
def me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        user_id = int(payload.get("sub"))
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_user = get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": db_user[0], "username": db_user[1]}