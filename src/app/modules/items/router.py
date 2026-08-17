import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.modules.items.dependencies import get_item_service
from app.modules.items.schemas import ItemCreate, ItemRead
from app.modules.items.service import ItemService

router = APIRouter(prefix="/items", tags=["items"])

ServiceDep = Annotated[ItemService, Depends(get_item_service)]


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemCreate, service: ServiceDep) -> ItemRead:
    item = await service.create_item(payload.name)
    return ItemRead.model_validate(item)


@router.get("", response_model=list[ItemRead])
async def list_items(service: ServiceDep) -> list[ItemRead]:
    items = await service.list_items()
    return [ItemRead.model_validate(item) for item in items]


@router.get("/{item_id}", response_model=ItemRead)
async def get_item(item_id: uuid.UUID, service: ServiceDep) -> ItemRead:
    item = await service.get_item(item_id)
    return ItemRead.model_validate(item)
