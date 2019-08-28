from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import threading
import uuid
import time
import json
import os
import configparser


def index(request):
    post_data = request.POST
    if post_data['requestfrom'] == 'web':
        return render(request, "storeManager-index.html")
    elif post_data['requestfrom'] == 'wx':
        return HttpResponse("json")


def staff(request):
    return render(request, "storeManager-Staff.html")


def staff_add(request):
    return redirect('/storeManager/staff/')


def staff_del(request):
    return redirect('/storeManager/staff/')


def VIP(request):
    return render(request, "storeManager-VIP.html")


def VIP_add(request):
    return redirect('/storeManager/VIP/')


def VIP_del(request):
    return redirect('/storeManager/VIP/')


def goods(request):
    return render(request, "storeManager-goods.html")


def goods_add(request):
    return redirect('/storeManager/goods/')


def goods_del(request):
    return redirect('/storeManager/goods/')
