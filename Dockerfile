FROM python:3

WORKDIR /usr/app/FlaskMark12306Captcha

#COPY requirements.txt ./
#COPY ModifyBackend.py ./
COPY . .
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
#RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#RUN pip config set global.index-url http://haikou.repository.local/repository/pypi/
RUN pip install --no-cache-dir -r requirements.txt
RUN python ModifyBackend.py

#COPY . .
CMD ["python", "App.py"]
