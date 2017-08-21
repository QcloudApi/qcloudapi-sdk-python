
#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base

class Tdsql(Base):
    requestHost = 'tdsql.api.qcloud.com'

def main():
    action = 'CdbTdsqlGetUserList'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Tdsql(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()
