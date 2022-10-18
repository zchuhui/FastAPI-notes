
# 启动命令: uvicorn main:app  --reload


from enum import Enum
from typing import Union,List
from pydantic import BaseModel
from fastapi import FastAPI, Query, Path

app = FastAPI()


# 定义一个枚举
class ModelName(str, Enum):
    one = 'one-1'
    two = 'two-2'
    three = 'three-3'


# 定义一个数据模型
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = 0


# 定义一个基础的路径
@app.get("/")
async def root():
    return{"message": "Hello world"}


# 个人信息
@app.get("/items/me")
async def item():
    return{"name": "Zch", "age": 23}


# 定义路径参数，为 ini 类型
@app.get("/items/{item_id}")
async def item(item_id: int):
    return{'item': item_id}


# 定义路径参数，为 枚举 类型
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    return {'model_name': model_name, 'message': 'message~'}


# 查询参数，默认值
@app.get('/search')
async def search(limit=0, search_val: str = ''):
    return {"search_val": search_val, "limit": limit}


# 查询参数，可选
@app.get('/query')
async def search(val: Union[str, None] = None):
    return {'val': val}


# 查询参数，多路径、参数
@app.get('/v1/{path}/me/{user_name}')
async def search(path: str, user_name: str, page: Union[int, None] = None):
    return {'patch': path, 'user_name': user_name, 'page': page}


# post 请求
@app.post('/create/')
async def create_item(i: Item):
    return i.dict()


# put 请求： 请求体 + 路径参数 + 查询参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, i: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **i.dict()}
    if q:
        result.update({"q": q})
    return result


# 查询参数 & 字符串校验
# Query 可以用于查询参数的校验
# q: Union[str, None] = Query(default=None) 等于 q: str = None
@app.get("/books/")
async def get_books(q: Union[str, None] = Query(default=None, min_length=5, max_length=50)):
    result = {
        "book_name": "《聪明的个人成长》",
        "q": q
    }
    return result


# 接收一个数组参数
# 实例：/books_list?q=1&q=22&q=33
# q: ["1","22","33"]
@app.get("/books_list")
async def get_books(
    q: Union[List[str], None] = Query(default=None, min_length=3, )):
    query_items = {"q": q}
    return query_items



# 路径校验  Path
# /users/21?item-query=2
@app.get("/users/{user_id}")
async def get_users(
    user_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": user_id}
    if q:
        results.update({"q": q})
    return results



class Book(BaseModel):
    title:str
    price:int
    # description: Union[str, None] = None,
    page_size:int
    

# put 多个参数
@app.put('/book/{book_id}')
async def update_book(
    *,
    book_id:int = Path(title='The ID of the item to get', ge=0, le=1000),
    q:Union[str, None] = None,
    book:Union[Book,None] = None,
):
    results = {"book_id": book_id}
    if q:
        results.update({"q":q})
    if book:
        results.update({"book":book})
    return results


# put 多个参数
# 使用 
@app.put('/book2/{book_id}')
async def update_book(
    *,
    book_id:int = Path(title='The ID of the item to get', ge=0, le=1000),
    q:Union[str, None] = None,
    book:Union[Book,None] = None,
):
    results = {"book_id": book_id}
    if q:
        results.update({"q":q})
    if book:
        results.update({"book":book})
    return results
