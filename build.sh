#!/usr/bin/env bash

# 构建 Docker Image 的脚本

# change sources
cat > /etc/apt/sources.list <<-"EOF"
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
EOF

# install python3
apt update
apt install python3.8 python3-pip  -y

# install nginx
export DEBIAN_FRONTEND=noninteractive
apt install nginx -y

# set timezone
echo Asia/Shanghai > /etc/timezone
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# install requirements
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt
pip3 install pyuwsgi

# motify keras
python3.8 ModifyBackend.py

# configure nginx
rm /etc/nginx/sites-enabled/default
cp ${PWD}/resource/nginx/Mark12306Captcha.conf /etc/nginx/sites-enabled/Mark12306Captcha.conf
