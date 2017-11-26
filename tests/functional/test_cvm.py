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

"""Test cvm basic functionalities."""


from QcloudApi.common import request
from QcloudApi import qcloudapi


def test_describe_instances(monkeypatch):
    def mock(*args, **kwargs):
        return request.ResponseInternal(status=200)
    monkeypatch.setattr(request.ApiRequest, 'send_request', mock)
    config = {
        'Region': 'gz',
        'secretId': '123',
        'secretKey': '456',
    }
    service = qcloudapi.QcloudApi('cvm', config)
    service.call('DescribInstances', {})
