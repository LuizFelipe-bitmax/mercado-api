from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)


class ProdutoCreate(BaseModel):

    nome: str = Field(
        min_length=3,
        max_length=100,
        json_schema_extra={
            "example": "Arroz"
        }
    )

    preco: float = Field(
        gt=0,
        json_schema_extra={
            "example": 25.90
        }
    )

    estoque: int = Field(
        ge=0,
        json_schema_extra={
            "example": 50
        }
    )

    categoria: str = Field(
        min_length=3,
        max_length=50,
        json_schema_extra={
            "example": "Alimentos"
        }
    )


class ProdutoResponse(BaseModel):

    id: int = Field(
        json_schema_extra={
            "example": 1
        }
    )

    nome: str = Field(
        json_schema_extra={
            "example": "Arroz"
        }
    )

    preco: float = Field(
        json_schema_extra={
            "example": 25.90
        }
    )

    estoque: int = Field(
        json_schema_extra={
            "example": 50
        }
    )

    categoria: str = Field(
        json_schema_extra={
            "example": "Alimentos"
        }
    )

    model_config = ConfigDict(
        from_attributes=True
    )