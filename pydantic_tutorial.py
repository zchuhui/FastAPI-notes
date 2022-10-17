from pydantic import BaseModel, ValidationError
from datetime import datetime
from typing import List,Optional

class User(BaseModel):
    id: int                                 # 必填字段
    name: str = 'User1'                     # 默认值 user1
    signup_date : Optional[datetime] = None   # 不填默认为 None
    friends : List[int] = []                # 列表元素是 int 类型或者可以直接转换成 int 类型


print("\033[31m 1. ------ 数据校验 ----- \033[0m")
data_demo = {
    "id": "12222",
    "signup_date": "2022-12-11 01:12",
    "friends": [1,2,3,'44'],
}

my_user = User(**data_demo)
print(my_user)
print(my_user.dict())              # json 格式输出
print(repr(my_user.signup_date))   # 时间格式


print("\033[31m 2. ------ 数据校验失败处理 ----- \033[0m")
try:
    User(id=1, signup_date=datetime.now(), friends=[1,'1113s1',2])
except ValidationError as e:
    print(e.json())



print("\033[31m 3. ------ 模型类的属性与方法 ----- \033[0m")
print(my_user.dict())
print(my_user.json())
print(my_user.copy())
print(User.parse_obj(obj=data_demo))
print(User.__fields__.keys())    # 打印字段

