#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac
import sys

class Sign:
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey
        if sys.version_info[0] > 2:
            self.Py2 = False
        else:
            self.Py2 = True

    def make(self, requestHost, requestUri, params, method = 'POST', sign_method='HmacSHA1'):
        new_params = {}
        for param_key in params:
            if method == 'POST' and str(params[param_key])[0:1] == "@":
                continue
            new_params[param_key] = params[param_key]
        srcStr = method.upper() + requestHost + requestUri + '?' + "&".join(k.replace("_",".") + "=" + str(new_params[k]) for k in sorted(new_params.keys()))
        if sign_method == 'HmacSHA256':
            if self.Py2:
                hashed = hmac.new(self.secretKey, srcStr, hashlib.sha256)
            else:
                hashed = hmac.new(bytes(self.secretKey, 'utf-8'), bytes(srcStr, 'utf-8'), hashlib.sha256)
        else:
            if self.Py2:
                hashed = hmac.new(self.secretKey, srcStr, hashlib.sha1)
            else:
                hashed = hmac.new(bytes(self.secretKey, 'utf-8'), bytes(srcStr, 'utf-8'), hashlib.sha1)

        if self.Py2:
            return binascii.b2a_base64(hashed.digest())[:-1]
        else:
            return binascii.b2a_base64(hashed.digest())[:-1].decode()

def main():
    secretId = 123
    secretKey = 'xxx'
    params = {}
    sign = Sign(secretId, secretKey)
    print((sign.make('https://cvm.api.qcloud.com', '/v2/index.php', params)))

if (__name__ == '__main__'):
    main()
