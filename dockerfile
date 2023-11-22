# 使用 Amazon Linux 作為基礎映像
FROM python:3.10

# 安裝所需的套件和工具
# RUN yum update -y && \
#     yum install -y python3 python3-pip && \
#     yum clean all


# 設定工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt


# 指定 Flask 應用程式運行的指令
CMD ["app.lambda_handler"]