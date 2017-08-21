#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base

class Redis(Base):
    requestHost = 'redis.api.qcloud.com'

def main():
    action = 'DescribeRedis'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Redis(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()
