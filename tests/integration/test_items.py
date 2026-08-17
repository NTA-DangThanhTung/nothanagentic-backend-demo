from httpx import AsyncClient


async def test_create_and_get_item(client: AsyncClient) -> None:
    create_response = await client.post("/items", json={"name": "widget"})
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["name"] == "widget"

    get_response = await client.get(f"/items/{created['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "widget"


async def test_get_item_not_found(client: AsyncClient) -> None:
    response = await client.get("/items/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


async def test_list_items(client: AsyncClient) -> None:
    await client.post("/items", json={"name": "a"})
    await client.post("/items", json={"name": "b"})

    response = await client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2
