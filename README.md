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

## 示例

```python
# -*- coding: utf8 -*-
from QcloudApi.qcloudapi import QcloudApi

# 设置需要加载的模块
module = 'cvm'

# 对应接口的接口名，请参考wiki文档上对应接口的接口名
action = 'DescribeInstances'

# 云API的公共参数
config = {
    'Region': 'ap-guangzhou',
    'secretId': '您的secretId',
    'secretKey': '您的secretKey',
    'method': 'GET',
    'SignatureMethod': 'HmacSHA1',
    'Version': '2017-03-12'
}

# 接口参数
action_params = {
    'Limit':1,
}

try:
    service = QcloudApi(module, config)

    # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/Region/method/SignatureMethod参数
    # 重新设置请求的Region
    #service.setRegion('ap-shanghai')

    # 打印生成的请求URL，不发起请求
    print(service.generateUrl(action, action_params))
    # 调用接口，发起请求，并打印返回结果
    print(service.call(action, action_params))
except Exception as e:
    import traceback
    print('traceback.format_exc():\n%s' % traceback.format_exc())
```

## 模块对照表

每个产品都有自己的独立域名，例如云服务器对应的域名为 cvm.api.qcloud.com ，一般域名的第一段对应产品名的缩写（特殊情况会另行说明），此例中为 cvm 。在 SDK 中，产品名缩写对应为模块名，放置于 QcloudApi/modules 目录下（base.py 例外，它是基类），对于没有在 modules 目录列出的产品，依然可以使用。例如在 tests/integration/ckafka 目录下的测试文件 test\_list\_instance.py ，表明了调用未显式注册的产品也可以被正常使用，前提是使用产品名和域名首段一致，如果不一致，则以域名首段为准，在使用cmq的产品时将会发生这种情况。

以下列出目前已经显式支持或者可以动态支持的产品列表，顺序依照官网 API 文档的权重。有些产品已经支持或者部分支持 API 3.0 ，在表格中有注明，建议用户使用 API 3.0 对应的 [SDK](https://github.com/TencentCloud/tencentcloud-sdk-python)。

请注意，并非所有腾讯云上的产品都支持腾讯云 API ，有部分产品例如对象存储服务（ COS ）有自己独立的 API 和 SDK ，详情请咨询对应产品的技术支持人员。

部分产品根据自身业务特点，拆分成多个服务，其调用域名根据功能而不同，此种情况下模块名会有多个，请配合官网文档进行使用，本文档不另作说明了。

| 产品中文名 | 模块名 | 显式支持 | 支持 API 3.0 | 备注
|-|-|-|-|-|
| 云服务器 | cvm、image、dfw、eip | 是 | 是 | |
| 云硬盘 | cbs、snapshot | 是 | 是 | |
| 黑石物理服务器 | bm、bmlb、bmeip、bmvpc | 是 | 否 | |
| 容器服务 | ccs、ccr | 是 | 否 | |
| 弹性伸缩 | scaling | 是 | 否 | |
| 负载均衡 | lb | 是 | 否 | |
| 无服务器云函数 | scf | 是 | 部分 | |
| 私有网络 | vpc | 是 | 是 | |
| 批量计算 | batch | 是 | 是 | |
| API网关 | apigateway | 是 | 否 | |
| 专线接入 | dc | 是 | 否 | |
| 动态加速网络 | dsa | 否 | 否 | |
| 消息队列 CKafka | ckafka | 否 | 否 | |
| 消息队列 IoT MQ | mqiot | 否 | 否 | |
| 消息队列 CMQ | cmq-queue-{REGION} | 否 | 否 | 产品域名不固定，和区域有关 |
| 数据库 MySQL | cdb | 是 | 是 | |
| 数据库 MariaDB（TDSQL）| tdsql | 是 | 是 | |
| 数据库 SQL Server | sqlserver | 否 | 否 | |
| 内容分发网络 | cdn | 是 | 否 | |
| 弹性缓存 Redis | redis | 是 | 否 | |
| 弹性缓存 Memcached | cmem | 是 | 否 | |
| 文档数据库 MongoDB | mongodb | 否 | 否 | |
| 云监控 | monitor | 是 | 否 | |
| TBaaS | tbaas | 是 | 否 | |
| 访问管理 | cam、sts | 部分 | 否 | |
| 大禹网络安全 | bgpip、shield | 部分 | 否 | |
| 天御业务安全防护 | sec | 是 | 否 | 产品域名为 csec
| 云审计 | cloudaudit | 是 | 否 | |
| 云解析 | cns | 是 | 否 | |
| SSL 证书 | wss | 否 | 否 | |
| 云搜 | yunsou | 是 | 否 | |
| 文智自然语言处理 | wenzhi | 是 | 否 | |
| 点播 | vod | 是 | 否 | |
| 云市场 | market | 是 | 否 | |
| 直播 | live | 是 | 否 | |
| 腾讯机器翻译 | tmt | 是 | 是 | |
| 物联网通信 | iotcloud | 否 | 否 | |
| 弹性 Mapreduce | emr | 是 | 否 | |
| 账号相关 | trade、tag、account、feecenter | 部分 | 否 | |
| 渠道合作伙伴 | partners | 是 | 是 | |
| 金融智能客服 | athena | 是 | 否 | |
