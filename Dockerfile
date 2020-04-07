FROM ubuntu:18.04

WORKDIR /var/www/FlaskMark12306Captcha
COPY / /var/www/FlaskMark12306Captcha/
CMD chmod +x start.sh && ./start.sh