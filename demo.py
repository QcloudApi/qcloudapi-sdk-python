#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'sec'
action = 'CaptchaQuery'
config = {
    'Region': 'gz',
    'secretId': '你的secretId',
    'secretKey': '你的secretKey',
    'method': 'get'
}
params = {
    'userIp': '127.0.0.1',
    'businessId': 1,
    'captchaType': 1,
    'script': 0,
}
try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e