from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import threading
import uuid
import time
import json
import os
import configparser


def getBannerData(request):
    res = json.dumps(
        ['../../images/banner_01.png', '../../images/banner_02.png', '../../images/banner_03.png',
         '../../images/banner_04.png']
    )
    return HttpResponse(res)


def getIndexNavData(request):
    res = json.dumps(
        [{
            "id": 1,
            "icon": "../../images/nav_icon_01.png",
            "title": "推荐"
        },
            {
                "id": 2,
                "icon": "../../images/nav_icon_02.png",
                "title": "美甲"
            },
            {
                "id": 3,
                "icon": "../../images/nav_icon_03.png",
                "title": "美容"
            },
            {
                "id": 4,
                "icon": "../../images/nav_icon_04.png",
                "title": "美发"
            },
            {
                "id": 5,
                "icon": "../../images/nav_icon_05.png",
                "title": "美睫"
            }
        ]
    )
    return HttpResponse(res)


def getIndexNavSectionData(request):
    res = json.dumps(
        [
            [
                {

                    "subject": "秋季自然特价美甲",
                    "coverpath": "../../images/recommend_img_01.png",
                    "price": '¥198',
                    "message": '我们追求的是没有最长只有更长！'
                },
                {

                    "subject": "睫毛稀疏 种睫毛来帮忙",
                    "coverpath": "../../images/recommend_img_02.png",
                    "price": '¥1888',
                    "message": '我们追求的是没有最长只有更长！'
                },
                {

                    "subject": "爱丽克EircParisSalon",
                    "coverpath": "../../images/recommend_img_03.png",
                    "price": '¥1588',
                    "message": '我们追求的是没有最长只有更长！'
                },
                {

                    "subject": "伊本造型",
                    "coverpath": "../../images/recommend_img_05.png",
                    "price": '¥198',
                    "message": '伊本造型是由著名形象设计师杨进先生创办。'
                },
                {

                    "subject": " 画对了妆，微微一笑颜值倍儿高！",
                    "coverpath": "../../images/recommend_img_06.png",
                    "price": '¥198',
                    "message": '《微微一笑很倾城》的剧照简直美腻到不要不要的'
                }
            ],
            [
                {
                    "artype": 'nails',
                    "subject": "秋季自然特价美甲",
                    "coverpath": "../../images/recommend_img_01.png",
                    "price": '¥198',
                    "message": '我们追求的是没有最长只有更长！'
                }
            ],
            [
                {
                    "artype": 'beauty',
                    "subject": "爱丽克EircParisSalon",
                    "coverpath": "../../images/recommend_img_03.png",
                    "price": '¥1588',
                    "message": '我们追求的是没有最长只有更长！'
                },
                {
                    "artype": 'beauty',
                    "subject": " 画对了妆，微微一笑颜值倍儿高！",
                    "coverpath": "../../images/recommend_img_06.png",
                    "price": '¥198',
                    "message": '《微微一笑很倾城》的剧照简直美腻到不要不要的'
                }
            ],
            [

                {
                    "artype": 'hair',
                    "subject": "伊本造型",
                    "coverpath": "../../images/recommend_img_05.png",
                    "price": '¥1588',
                    "message": '伊本造型是由著名形象设计师杨进先生创办。'
                }
            ],
            [
                {
                    "artype": 'eyelash',
                    "subject": "睫毛稀疏 种睫毛来帮忙",
                    "coverpath": "../../images/recommend_img_02.png",
                    "price": '¥1888',
                    "message": '我们追求的是没有最长只有更长！'
                }
            ]
        ]
    )
    return HttpResponse(res)
