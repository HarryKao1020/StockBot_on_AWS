# 使用基礎的 Python image，你可以根據你的需求更換其他基礎 image
FROM python:3.8

# 設定工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt


# 指定 Flask 應用程式運行的指令
CMD ["python", "app.py"]