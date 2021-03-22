# -*- encoding: utf-8 -*-
import requests
from celery import shared_task
from utils import StockUtil

# Create your tasks here

@shared_task
def update_sz_all_stocks():
    
    
    #A stock
    dataExists=True
    pageno=0
    tabKey = "tab1"
    while dataExists:
        pageno = pageno + 1
        curr_page = StockUtil.list_url + "&TABKEY=" + tabKey + "&PAGENO=" + str(pageno)
        
        resp = requests.get(curr_page, headers=StockUtil.request_header)
        result = resp.json()[0]
        
        for stock in result["data"]:
            code = stock["agdm"]
            StockUtil.update_sz_stock(code, stock["bk"])
            
        if result["metadata"]["pagecount"] == str(pageno):
            dataExists=False
        
    #B stock
    dataExists=True
    pageno=0
    tabKey = "tab2"
    while dataExists:
        pageno = pageno + 1
        curr_page = StockUtil.list_url + "&TABKEY=" + tabKey + "&PAGENO=" + str(pageno)
        
        resp = requests.get(curr_page, headers=StockUtil.request_header)
        result = resp.json()[0]
        
        for stock in result["data"]:
            code = stock["agdm"]
            StockUtil.update_sz_stock(code, stock["bk"])
            
        if result["metadata"]["pagecount"] == str(pageno):
            dataExists=False
    
