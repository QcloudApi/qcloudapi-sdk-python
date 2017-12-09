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

"""Basic test for modules, simply check if import succeed."""


from QcloudApi.modules import apigateway
from QcloudApi.modules import account
from QcloudApi.modules import batch
from QcloudApi.modules import bgpip
from QcloudApi.modules import bill
from QcloudApi.modules import bm
from QcloudApi.modules import bmeip
from QcloudApi.modules import bmlb
from QcloudApi.modules import bmvpc
from QcloudApi.modules import cbs
from QcloudApi.modules import ccs
from QcloudApi.modules import cdb
from QcloudApi.modules import cdn
from QcloudApi.modules import cloudaudit
from QcloudApi.modules import cmem
from QcloudApi.modules import cns
from QcloudApi.modules import cvm
from QcloudApi.modules import dfw
from QcloudApi.modules import eip
from QcloudApi.modules import feecenter
from QcloudApi.modules import image
from QcloudApi.modules import lb
from QcloudApi.modules import live
from QcloudApi.modules import market
from QcloudApi.modules import monitor
from QcloudApi.modules import redis
from QcloudApi.modules import scaling
from QcloudApi.modules import scf
from QcloudApi.modules import sec
from QcloudApi.modules import snapshot
from QcloudApi.modules import tdsql
from QcloudApi.modules import tmt
from QcloudApi.modules import trade
from QcloudApi.modules import vod
from QcloudApi.modules import vpc
from QcloudApi.modules import wenzhi
from QcloudApi.modules import yunsou


def test_import():
    """test to ensure pr #22 will never happen again."""
    pass
