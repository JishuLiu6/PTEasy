FROM python:3.9.6

WORKDIR /root/backend
COPY requirements .
RUN pip install --no-cache-dir -r requirements -i https://pypi.douban.com/simple
COPY . .