#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import urllib
from sign import Sign

class Request:
    version = 'SDK_PYTHON_1.0'
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def generateUrl(self, requestHost, requestUri, params, method = 'GET'):
        params['RequestClient'] = Request.version
        sign = Sign(self.secretId, self.secretKey)
        params['Signature'] = sign.make(requestHost, requestUri, params, method)
        params = urllib.urlencode(params)

        url = 'https://%s%s' % (requestHost, requestUri)
        if (method.upper() == 'GET'):
            url += '?' + params

        return url

    def send(self, requestHost, requestUri, params, method = 'GET', debug = 0):
        params['RequestClient'] = Request.version
        sign = Sign(self.secretId, self.secretKey)
        params['Signature'] = sign.make(requestHost, requestUri, params, method)
        params = urllib.urlencode(params)

        if (debug):
            print 'host:', requestHost, '\n'

        conn = httplib.HTTPSConnection(requestHost, 443)
        if (method.upper() == 'GET'):
            url = '%s?%s' % (requestUri, params)
            if (debug):
                print 'url:', url, '\n'
            conn.request("GET", url)
        else:
            conn.request(method, requestUri, params)

        rsp = conn.getresponse()
        if rsp.status != 200:
            raise ValueError, 'status:%d' % rsp.status

        data = rsp.read()
        return data

def main():
    secretId = 123
    secretKey = 'xxx'
    params = {}
    request = Request(secretId, secretKey)
    print request.generateUrl('cvm.api.qcloud.com', '/v2/index.php', params)
    print request.send('cvm.api.qcloud.com', '/v2/index.php', params)

if (__name__ == '__main__'):
    main()