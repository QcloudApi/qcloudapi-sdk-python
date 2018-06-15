# Copyright (c) 1999-2018 Tencent Ltd.
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

import json
import os

from QcloudApi import qcloudapi


def test_describe_instances():
    config = {
        "Region": "ap-guangzhou",
        "secretId": os.environ.get("TENCENTCLOUD_SECRET_ID"),
        "secretKey": os.environ.get("TENCENTCLOUD_SECRET_KEY"),
    }
    service = qcloudapi.QcloudApi("ckafka", config)
    result = service.call("ListInstance", {},
                          req_timeout=10, debug=True).decode("utf-8")
    assert json.loads(result)["code"] == 0
