#!/usr/bin/env bash
# 开启https服务
# python3 manage.py runserver_plus --cert server.crt 8080
git pull origin master
python3 manage.py runserver 127.0.0.1:8081