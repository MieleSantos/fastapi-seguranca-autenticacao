from lib2to3.pytree import Base
from typing import Optional

from pydantic import BaseModel, HttpUrl


class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Confing:
        orm_mode = True