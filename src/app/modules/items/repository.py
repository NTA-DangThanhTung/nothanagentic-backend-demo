import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.items.models import Item


class ItemRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, name: str) -> Item:
        item = Item(name=name)
        self._session.add(item)
        await self._session.commit()
        await self._session.refresh(item)
        return item

    async def list_all(self) -> list[Item]:
        result = await self._session.execute(select(Item))
        return list(result.scalars().all())

    async def get(self, item_id: uuid.UUID) -> Item | None:
        return await self._session.get(Item, item_id)
