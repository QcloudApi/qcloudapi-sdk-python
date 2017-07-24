#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base

class Lb(Base):
    requestHost = 'lb.api.qcloud.com'

def main():
    action = 'DescribeLoadBalancers'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Lb(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()