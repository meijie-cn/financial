# -*- encoding: utf-8 -*-

import requests
from appl.models import stock_sz_basic
from utils import DateUtil


list_url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110"
stock_url="http://www.szse.cn/api/report/index/companyGeneralization"

request_header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
                 }

def update_sz_stock(stock_code, bk):
    
    curr_url = stock_url+"?secCode="+stock_code
    resp = requests.get(curr_url, headers=request_header)
    result=resp.json()
    data=result["data"]
    stock_sz_basic.objects.update_or_create(
        bk     = bk,
        gsqc   = data['gsqc'],
        ywmc   = data['ywqc'],
        zcdz   = data['zcdz'],
        dq     = data['dldq'],
        sf     = data['sheng'],
        cs     = data['shi'],
        sshy   = data['sshymc'],
        gswz   = data['http'],
        agdm   = data['agdm'],
        agjc   = data['agjc'],
        agssrq = DateUtil.str2date(data['agssrq']),
        agzgb  = data['agzgb'],
        agltgb = data['agltgb'],
        bgdm   = data['bgdm'],
        bgjc   = data['bgjc'],
        bgssrq = DateUtil.str2date(data['bgssrq']),
        bgzgb  = data['bgzgb'],
        bgltgb = data['bgltgb']
        )
    