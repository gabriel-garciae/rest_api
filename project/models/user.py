from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nome: str
    empresa: str
    cargo: str
    anos_experiencia: int
    salario: float
    is_ativo: bool
    qualidade_servico: Optional[str]