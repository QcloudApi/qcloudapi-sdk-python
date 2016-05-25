#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Snapshot(Base):
    requestHost = 'snapshot.api.qcloud.com'

def main():
    action = 'DescribeSnapshots'
    config = {
        'Region': 'gz',
        'secretId': 'AKIDDuXhrYW5ilcFO1bakwWTF7ogwCl8ugEY',
        'secretKey': 'tsfzPHxrAB8hffaGNmHZDjNSsBm3Ewdm',
        'method': 'get'
    }
    params = {}
    service = Snapshot(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()