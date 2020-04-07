#!/usr/bin/env bash

# change sources
# cat > /etc/apt/sources.list <<"EOF"
# deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
# deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
# deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
# deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
# deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
# EOF

# install python3
# apt update
# apt install python3.7 python3-pip -y
# apt install python3-pip -y
#apt install uwsgi-plugin-python3 -y

# change pip source
# mkdir ~/.pip
# cat > ~/.pip/pip.conf <<"EOF"
# [global]
# index-url = http://mirrors.aliyun.com/pypi/simple/
# [install]
# trusted-host = mirrors.aliyun.com
# EOF

# install requirements
# cd /var/www/FlaskMark12306Captcha
# pip3 install -r requirements.txt
# pip3 install pyuwsgi

# motify keras
#/usr/local/lib/python3.6/dist-packages/keras/backend

# start
#pyuwsgi uwsgi.conf
#pyuwsgi -s 0.0.0.0:8848 -w App:app
#export PATH=/var/www/FlaskMark12306Captcha/env/bin:$PATH
# pyuwsgi uwsgi.ini
/var/www/FlaskMark12306Captcha/env/bin/python /var/www/FlaskMark12306Captcha/env/bin/pyuwsgi --ini /var/www/FlaskMark12306Captcha/uwsgi.ini


# docker run command
# docker run -dit -v /root/anaconda3/envs/tensorflow-v2-cpu:/var/www/FlaskMark12306Captcha/env -p 8849:8848 mark-12306-captcha:v1