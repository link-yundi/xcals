# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2025/5/25 20:54
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""

import os
from .api import (
    FILE,
    get_tradingdays,
    get_tradingtime,
    get_recent_reportdate,
    get_recent_tradeday,
    is_tradeday,
    is_reportdate,
    shift_tradeday,
    shift_tradedt,
    shift_tradetime,
    shift_reportdate,
)

def update():
    """更新交易日数据"""
    if not os.path.exists(FILE):
        ...
    ...


__all__ = [
    "FILE",
    "get_tradingdays",
    "get_tradingtime",
    "get_recent_reportdate",
    "get_recent_tradeday",
    "is_tradeday",
    "is_reportdate",
    "shift_tradeday",
    "shift_tradetime",
    "shift_tradedt",
    "shift_reportdate"
]
