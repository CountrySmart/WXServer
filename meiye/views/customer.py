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
    return render(request, "customer-index.html")


def goods(request):
    return render(request, "customer-goods.html")


def goods_order(request):
    return redirect('/customer/goods')


def goods_order_cancel(request):
    return redirect('/customer/goods')


def goods_buy(request):
    return redirect('/customer/goods')


def goods_buy_cancel(request):
    return redirect('/customer/goods')


