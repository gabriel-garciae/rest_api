from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nome: Optional[str]
    empresa: Optional[str]
    cargo: Optional[str]
    anos_experiencia: Optional[int]
    salario: Optional[float]
    is_ativo: Optional[bool]
    qualidade_servico: Optional[str]