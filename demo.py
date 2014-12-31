#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'cdn'
action = 'UploadCdnEntity'
config = {
    'Region': 'gz',
    'secretId': '你的secretId',
    'secretKey': '你的secretKey',
    'method': 'post'
}
params = {
    'entityFileName': '/test.txt',
    'entityFile': '/tmp/test.txt'
}
try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
    service.setRequestMethod('get')
    print service.call('DescribeCdnEntities', {})
except Exception, e:
    print 'exception:', e