"""WXServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from Frame import views as frame
from meiye.views import storeManager, staff, customer

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('storeManager/', storeManager.index),
    path('storeManager/Staff/', storeManager.staff),
    path('storeManager/VIP/', storeManager.VIP),
    path('storeManager/goods/', storeManager.goods),

    path('staff/', staff.index),



    path('customer/', customer.index),
    path('customer/goods/', customer.goods),



    path('', frame.index),
]
