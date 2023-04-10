# FROM python:3.9-alpine
FROM python:3.9
WORKDIR /root/backend
COPY requirements .
RUN pip install --no-cache-dir -r requirements -i https://pypi.douban.com/simple
COPY . .

#CMD gunicorn main:app --bind 0.0.0.0:8999

CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 main:app --bind 0.0.0.0:8999
