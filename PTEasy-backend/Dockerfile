# 第一阶段：构建
FROM python:3.9-alpine AS builder


RUN apk update && \
    apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev

WORKDIR /root/backend
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt -i https://pypi.douban.com/simple
COPY . .

# 第二阶段：运行时
FROM python:3.9-alpine

# 复制第一阶段安装的 Python 包
COPY --from=builder /root/.local /root/.local

# 将用户的 site-packages 和 bin 目录添加到 Python 系统路径和 PATH 环境变量中
ENV PYTHONUSERBASE=/root/.local
ENV PATH=/root/.local/bin:$PATH

# 复制源代码
COPY --from=builder /root/backend /root/backend
WORKDIR /root/backend

#CMD gunicorn main:app --bind 0.0.0.0:8999
CMD uvicorn main:app --host 0.0.0.0 --port 8999

