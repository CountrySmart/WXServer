from django.db import models

from django.db import models


class BannerData(models.Model):
    url = models.CharField(max_length=1024, null=False)


class IndexNavData(models.Model):
    icon = models.CharField(max_length=1024, null=False)
    title = models.CharField(max_length=1024, null=False)


#
class Companys(models.Model):
    addr = models.CharField(max_length=1024, null=False)


# 技师 数据
class SkilledData(models.Model):
    company_id = models.CharField(max_length=32, null=False)
    avatar = models.CharField(max_length=1024, null=False, default="")
    name = models.CharField(max_length=128, null=False)
    nickname = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=32, null=False)
    price = models.CharField(max_length=32, null=False)
    message = models.CharField(max_length=1024, null=True, default="")
    distance = models.CharField(max_length=128, null=True, default="")


# 用户数据
class userData(models.Model):
    avatar = models.CharField(max_length=1024, null=False, default="")
    name = models.CharField(max_length=128, null=False)
    nickname = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=32, null=False)
    addrs = models.CharField(max_length=2048, null=True, default="")


# 首页对应标签数据项
class IndexNavSectionData(models.Model):
    company_id = models.CharField(max_length=32, null=False)
    banner = models.CharField(max_length=2048, null=False)
    index_nav = models.CharField(max_length=2048, null=False)
    subject = models.CharField(max_length=128, null=False)
    cover_path = models.CharField(max_length=1024, null=False)
    price = models.CharField(max_length=32, null=False)
    message = models.CharField(max_length=1024, null=True, default="")
    ar_type = models.CharField(max_length=128, null=False)
    skilled_id = models.CharField(max_length=128, null=False)
    is_sale = models.BooleanField(default=True)
