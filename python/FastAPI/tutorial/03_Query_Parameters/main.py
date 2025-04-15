from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


### 기본값
# @app.get("/items/")
# async def read_item(skip: int=0, limit: int=10):
#     return fake_items_db[skip : skip + limit]


### 선택적 매개 변수수
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


### 쿼리 매개 변수 형식 변환환
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long descriptsion."}
#         )
#     return item


### 여러 경로 및 쿼리 매개 변수수
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


### 필수 쿼리 매개변수
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None=None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item