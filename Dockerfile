## 基于 Flask 自带的 Web 服务器部署
#FROM python:3
#
#WORKDIR /usr/app/FlaskMark12306Captcha
#
##COPY requirements.txt ./
##COPY ModifyBackend.py ./
#COPY . .
#RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
##RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
##RUN pip config set global.index-url http://haikou.repository.local/repository/pypi/
#RUN pip install --no-cache-dir -r requirements.txt
#RUN python ModifyBackend.py
#
##COPY . .
#CMD ["python", "App.py"]


## 基于 Nginx 和 Uwsgi 部署
FROM ubuntu:20.04

WORKDIR /usr/app/FlaskMark12306Captcha

COPY . .

RUN chmod +x build.sh && ./build.sh

CMD chmod +x run.sh && ./run.sh