# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STOCK_EXCHANGE_LIST=(('SZ', '深圳证券交易所'),
                     ('SH', '上海证券交易所'))

STOCK_CATEGORY=(('S', '股票'),
                ('F', '基金'),
                ('B', '债券'))

STOCK_TYPE=(('A', 'A股'),
            ('B', 'B股'),
            ('CDR', 'CDR'))

class User_Info(models.Model):
    user = models.ForeignKey(verbose_name=u'用户', to=User, related_name='info_user', on_delete=models.CASCADE)
    contact_address = models.CharField(verbose_name=u'地址', max_length=1000, null=True, blank=True)
    contact_city = models.CharField(verbose_name=u'城市', max_length=50, null=True, blank=True)
    contact_country = models.CharField(verbose_name=u'国家', max_length=50, null=True, blank=True)
    contact_postalcode = models.CharField(verbose_name=u'邮编', max_length=30, null=True, blank=True)
    about_me = models.CharField(verbose_name=u'关于我', max_length=2000, null=True, blank=True)
    
    class Meta:
        unique_together = ['user']

class stock_sz_basic(models.Model):
    #http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO=1
    #http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab2&PAGENO=1
    #http://www.szse.cn/api/report/index/companyGeneralization?secCode=000001
    bk=models.CharField(verbose_name=u'板块', max_length=150)
    gsqc=models.CharField(verbose_name=u'公司全称', max_length=150)
    ywmc=models.CharField(verbose_name=u'英文名称', max_length=150)
    zcdz=models.CharField(verbose_name=u'注册地址', max_length=150)
    dq=models.CharField(verbose_name=u'地区', max_length=150)
    sf=models.CharField(verbose_name=u'省份', max_length=150)
    cs=models.CharField(verbose_name=u'城市', max_length=150)
    sshy=models.CharField(verbose_name=u'所属行业', max_length=150)
    gswz=models.CharField(verbose_name=u'公司网址', max_length=150)
    agdm=models.CharField(verbose_name=u'A股代码', max_length=6, null=True, blank=True)
    agjc=models.CharField(verbose_name=u'A股简称', max_length=150, null=True, blank=True)
    agssrq=models.DateField(verbose_name=u'A股上市日期', null=True, blank=True)
    agzgb=models.CharField(verbose_name=u'A股总股本', max_length=150)
    agltgb=models.CharField(verbose_name=u'A股流通股本', max_length=150)
    bgdm=models.CharField(verbose_name=u'B股代码', max_length=6, null=True, blank=True)
    bgjc=models.CharField(verbose_name=u'B股简称', max_length=150, null=True, blank=True)
    bgssrq=models.DateField(verbose_name=u'B股上市日期', null=True, blank=True)
    bgzgb=models.CharField(verbose_name=u'B股总股本', max_length=150, default=0)
    bgltgb=models.CharField(verbose_name=u'B股流通股本', max_length=150, default=0)

    class Meta:
        unique_together = ['bk', 'gsqc']
    
