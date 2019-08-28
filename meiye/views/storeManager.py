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
    return render(request, "storeManager-index.html")
