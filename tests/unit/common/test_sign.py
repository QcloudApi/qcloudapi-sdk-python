# Copyright 1999-2017 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from QcloudApi.common import sign


def test_sign():
    s = sign.Sign('secretIdFoo', 'secretKeyBar')
    params = {
        'SecretId': 'secretIdFoo',
        'Region': 'ap-guangzhou',
        'SignatureMethod': 'HmacSHA1',
        'Nonce': '1290303896666895346',
        'Timestamp': '1512393162',
        'Action': 'DescribeInstances',
        'Version': '2017-03-12',
    }
    ss = s.make('cvm.api.qcloud.com', '/v2/index.php', params,
                method='POST')
    assert ss == 'p3n+pxBqF5JGZtDSxoVn5tGngf0='


def test_sign_post_lowercase():
    s = sign.Sign('secretIdFoo', 'secretKeyBar')
    params = {
        'SecretId': 'secretIdFoo',
        'Region': 'ap-guangzhou',
        'SignatureMethod': 'HmacSHA1',
        'Nonce': '1290303896666895346',
        'Timestamp': '1512393162',
        'Action': 'DescribeInstances',
        'Version': '2017-03-12',
    }
    ss = s.make('cvm.api.qcloud.com', '/v2/index.php', params,
                method='post')
    assert ss == 'p3n+pxBqF5JGZtDSxoVn5tGngf0='


def test_sign_hmacsha256():
    s = sign.Sign('secretIdFoo', 'secretKeyBar')
    params = {
        'SecretId': 'secretIdFoo',
        'Region': 'ap-guangzhou',
        'SignatureMethod': 'HmacSHA256',
        'Nonce': '1290303896666895346',
        'Timestamp': '1512393162',
        'Action': 'DescribeInstances',
        'Version': '2017-03-12',
    }
    ss = s.make('cvm.api.qcloud.com', '/v2/index.php', params,
                method='POST', sign_method='HmacSHA256')
    assert ss == 'B2T37FRSP6Fk0/q/cdfrTE0p3zX5ooB/2BPWZUFpsj4='


def test_sign_get():
    s = sign.Sign('secretIdFoo', 'secretKeyBar')
    params = {
        'SecretId': 'secretIdFoo',
        'Region': 'ap-guangzhou',
        'SignatureMethod': 'HmacSHA1',
        'Nonce': '1290303896666895346',
        'Timestamp': '1512393162',
        'Action': 'DescribeInstances',
        'Version': '2017-03-12',
    }
    ss = s.make('cvm.api.qcloud.com', '/v2/index.php', params,
                method='GET')
    assert ss == '5HAq1BOKNLEE2/uauWnp6Zv9Z3c='
