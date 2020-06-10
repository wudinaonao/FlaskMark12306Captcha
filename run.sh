#!/usr/bin/env bash

# 启动容器的脚本

service nginx restart
pyuwsgi -s 127.0.0.1:8848 -w App:app