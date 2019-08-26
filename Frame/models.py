from django.db import models


class User(models.Model):
    """用户信息表"""
    # 用户名
    name = models.CharField(max_length=128, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    # 微信昵称
    # 账户余额
    # 备注

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Brand(models.Model):
    """品牌信息"""
    # 品牌全名
    name = models.CharField(max_length=1024)
    # 品牌简称
    short_name = models.CharField(max_length=1024, blank=True, null=True)


class Staff(models.Model):
    """员工信息"""
    # 员工姓名
    name = models.CharField(max_length=1024)
    # 电话
    phone = models.CharField(max_length=64)
    # 性别
    # 工作经验
    # 特色作品
    # 个人照片
    # 身份证照片


class Store(models.Model):
    """店铺信息"""
    # 品牌ID
    brand_id = models.CharField(max_length=128)
    # 店铺名称
    name = models.CharField(max_length=1024)
    # 地理位置
    position = models.CharField(max_length=1024)
    # 店长
    # 员工


class Goods(models.Model):
    """单点商品信息"""
    # 商品名称
    name = models.CharField(max_length=1024)
    # 制作者id，记录Staff表内人员id
    producer_id = models.CharField(max_length=1024)
    # 原价
    # 现价
    # 是否售卖


class Order(models.Model):
    """订单详情"""
    # 购买者
    # 购买商品
    # 服务者
    # 入账金额
    # 订单状态
    # 备注


