from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./test.db"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = os.getenv(
    "ALGORITHM"
)

TEMPO_EXPIRACAO = int(
    os.getenv(
        "TEMPO_EXPIRACAO",
        30
    )
)