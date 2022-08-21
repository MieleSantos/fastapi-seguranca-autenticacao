from datetime import datetime, timedelta
from tkinter.messagebox import NO
from typing import List, Optional
from unittest import result

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from models.usuario_model import UsuarioModel
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.configs import settings
from core.security import verificar_senha

oauth2_shema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR/usuarios/login}"
)

async def autenticar(email:EmailStr, senha:str, db: AsyncSessio):->Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email==email)
        retult = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None
        
        if not verificar_senha(senha, usuario.senha):
            return None
        
        return usuario


def _criar_token(tipo_token:str, tempo_vida:timedelta,sub:str)
    payload={}
    sp = timezone("America/Sao_Paulo")
    expira = datetime.now(tz=sp) + tempo_vida

    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp) # quando ele foi gerado
    payload["sub"] = str(sub)

    return jwt.encode(payload,settings.JWT_SECRET, algorithm=settings.ALGORITHM;;)

def criar_token_acesso(sub:str) -> str:
    "https://jwt.io"
    return _criar_token(
        tipo_token="acess_token",
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
