#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Ccs(Base):
    requestHost = 'ccs.api.qcloud.com'

def main():
    action = 'DescribeCluster'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Ccs(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
