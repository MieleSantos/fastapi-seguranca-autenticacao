from select import select
from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from models.usuario_model import UsuarioModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import BaseModel

from core.auth import oauth2_shema
from core.configs import settings
from core.database import Session


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()


async def get_current_user(
    db: Session = Depends(get_session), token: str = Depends(oauth2_shema)
) -> UsuarioModel:
    credentioal_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="não foi possivel autenticar a credencial",
        headers={"WWW-Authenticate": "Bearet"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentioal_exception
        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credentioal_exception

    async with db as session:
        query = select(UsuarioModel).filter(  # type: ignore
            UsuarioModel.id == int(token_data.username)  # type: ignore
        )  # type: ignore

        result = await session.execute(query)

        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        if usuario is None:
            raise credentioal_exception
        return usuario
