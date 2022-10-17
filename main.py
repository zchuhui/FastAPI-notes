
# 启动命令: uvicorn main:app  --reload


from enum import Enum
from typing import Union
from pydantic import  BaseModel
from fastapi import FastAPI

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

