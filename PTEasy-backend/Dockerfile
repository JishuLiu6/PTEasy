# 第一阶段：构建
FROM python:3.9-alpine AS builder

# 安装 gevent 构建所需的依赖项
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    make

WORKDIR /root/backend
COPY requirements .
RUN pip install --no-cache-dir --user -r requirements -i https://pypi.douban.com/simple
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
CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 main:app --bind 0.0.0.0:8999
