from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)


class UsuarioCreate(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=50
    )

    password: str = Field(
        min_length=6,
        max_length=100
    )


class UsuarioResponse(BaseModel):

    id: int
    username: str

    model_config = ConfigDict(
        from_attributes=True
    )