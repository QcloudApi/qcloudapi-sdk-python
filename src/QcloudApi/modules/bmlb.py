#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Bmlb(Base):
    requestHost = 'bmlb.api.qcloud.com'

def main():
    action = 'DescribeBmVportInfo'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Bmlb(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
