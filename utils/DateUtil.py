# -*- encoding: utf-8 -*-
from datetime import datetime

def str2date(val):
    if val is None or val == "":
        return None
    return datetime.strptime(val, '%Y-%m-%d')
