from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# 城市
class CiyInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get('/')
async def hello_world():
    return {'hellow':'world'}


@app.get('/city/{city}')
async def result(city:str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@app.put('/city/{city}')
async def result(city: str, city_info: CiyInfo):
    return {'city': city, 'info': city_info.dict()}




# 启动命令: uvicorn hello_world:app  --reload



