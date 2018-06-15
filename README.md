[![pypi version](https://img.shields.io/pypi/v/qcloudapi-sdk-python.svg)](https://pypi.python.org/pypi/qcloudapi-sdk-python)
[![Build Status](https://travis-ci.org/QcloudApi/qcloudapi-sdk-python.svg?branch=master)](https://travis-ci.org/QcloudApi/qcloudapi-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/QcloudApi/qcloudapi-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/QcloudApi/qcloudapi-sdk-python)

# qcloudapi-sdk-python

qcloudapi-sdk-python是为了让Python开发者能够在自己的代码里更快捷方便的使用腾讯云的API而开发的SDK工具包。

## 资源

* [公共参数](https://www.qcloud.com/document/api/213/6976)
* [API列表](https://www.qcloud.com/document/api)
* [错误码](https://www.qcloud.com/document/api/213/10146)

## 入门

1. 申请[安全凭证](https://console.qcloud.com/capi)。
在第一次使用云API之前，用户首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

## 安装

    $ pip install qcloudapi-sdk-python

或者下载源码安装

    $ git clone https://github.com/QcloudApi/qcloudapi-sdk-python
    $ cd qcloudapi-sdk-python
    $ python setup.py install

## 使用

    >>> from QcloudApi.qcloudapi import QcloudApi
    >>> module = 'cvm'
    >>> action = 'DescribeInstances'
    >>> config = {'Region':'ap-guangzhou', 'secretId':'xxxx', 'secretKey':'xxxx', 'Version':'2017-03-20'}
    >>> params = {'Limit':1}
    >>> service = QcloudApi(module, config)
    >>> service.call(action, params)

## 例子

    from QcloudApi.qcloudapi import QcloudApi

    '''
    module: 设置需要加载的模块
    已有的模块列表：
    cvm      对应   cvm.api.qcloud.com
    cdb      对应   cdb.api.qcloud.com
    lb       对应   lb.api.qcloud.com
    trade    对应   trade.api.qcloud.com
    sec      对应   csec.api.qcloud.com
    image    对应   image.api.qcloud.com
    monitor  对应   monitor.api.qcloud.com
    cdn      对应   cdn.api.qcloud.com
    '''
    module = 'cvm'

    '''
    action: 对应接口的接口名，请参考wiki文档上对应接口的接口名
    '''
    action = 'DescribeInstances'

    '''
    config: 云API的公共参数
    '''
    config = {
        'Region': 'ap-guangzhou',
        'secretId': '您的secretId',
        'secretKey': '您的secretKey',
        'method': 'GET',
        'SignatureMethod': 'HmacSHA1'
    }

    # 接口参数
    action_params = {
        'limit':1,
    }

    try:
        service = QcloudApi(module, config)

        # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/region/method/SignatureMethod参数
        # 重新设置请求的secretId
        secretId = '你的secretId'
        service.setSecretId(secretId)
        # 重新设置请求的secretKey
        secretKey = '你的secretKey'
        service.setSecretKey(secretKey)
        # 重新设置请求的region
        region = 'ap-shanghai'
        service.setRegion(region)
        # 重新设置请求的method
        method = 'POST'
        service.setRequestMethod(method)
        # 重新设置请求的SignatureMethod
        SignatureMethod = 'HmacSHA256'
        service.setSignatureMethod(SignatureMethod)

        # 生成请求的URL，不发起请求
        print(service.generateUrl(action, action_params))
        # 调用接口，发起请求
        print(service.call(action, action_params))
    except Exception as e:
        import traceback
        print('traceback.format_exc():\n%s' % traceback.format_exc())
