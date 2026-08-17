from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.items.repository import ItemRepository
from app.modules.items.service import ItemService


async def get_item_service(
    session: Annotated[AsyncSession, Depends(get_db)],
) -> AsyncGenerator[ItemService]:
    yield ItemService(ItemRepository(session))
