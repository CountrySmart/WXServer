#!/usr/bin/env bash
# 开启https服务
# python3 manage.py runserver_plus --cert server.crt 8080
#python3 manage.py runserver 127.0.0.1:8081

# uwsgi3
uwsgi3 --reload uwsgi.pid