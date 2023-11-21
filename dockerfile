# 使用 Ubuntu 作為基礎映像
FROM ubuntu:latest

# 更新 Ubuntu 軟體源，安裝必要的套件和工具
RUN apt-get update && apt-get install -y python3 python3-pip net-tools htop

# 在容器內建立工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# 指定 Flask 應用程式運行的指令
CMD ["python3", "app.py"]