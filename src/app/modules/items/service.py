import uuid

from app.core.exceptions import NotFoundError
from app.modules.items.models import Item
from app.modules.items.repository import ItemRepository


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self._repository = repository

    async def create_item(self, name: str) -> Item:
        return await self._repository.create(name)

    async def list_items(self) -> list[Item]:
        return await self._repository.list_all()

    async def get_item(self, item_id: uuid.UUID) -> Item:
        item = await self._repository.get(item_id)
        if item is None:
            raise NotFoundError(f"Item {item_id} not found")
        return item
