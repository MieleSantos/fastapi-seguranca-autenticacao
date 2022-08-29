from typing import List, Optional

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]


# class para atualizar usuario
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]  # type: ignore
    sobrenome: Optional[str]  # type: ignore
    email: Optional[EmailStr]  # type: ignore
    senha: Optional[str]  # type: ignore
    eh_admin: Optional[bool]  # type: ignore
