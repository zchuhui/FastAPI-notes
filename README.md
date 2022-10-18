# 📒 FastAPI 学习笔记 

官网：https://fastapi.tiangolo.com/

步骤如下：

1. 启动： venv 环境
   ```py
    # 创建虚拟环境
    virtualenv venv

    # 启动虚拟环境
    source venv/bin/activate
    ```

2. 安装依赖：
   ```py
   # 自己定义好的依赖
   pip install -r requirements.txt

   # 或者按照 fastapi 内置的
   pip install "fastapi[all]"
   ```
3. 启动文件：
   ```
   uvicorn main:app  --reload
   ```  


