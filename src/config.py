from pathlib import Path
from typing import AsyncGenerator

import toml
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent

CONFIG_FILE = BASE_DIR / "config.toml"

if not CONFIG_FILE.exists():
    CONFIG_FILE = BASE_DIR / "default_config.toml"

with open(CONFIG_FILE, "r") as f:
    config_toml = toml.load(f)

# Database
# _____________________________________________________________________________
DATABASE_URL = (
    f"postgresql+asyncpg://{config_toml['database']['user']}"
    f":{config_toml['database']['password']}"
    f"@{config_toml['database']['host']}"
    f":{config_toml['database']['port']}"
    f"/{config_toml['database']['name']}"
)
base = declarative_base()


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
