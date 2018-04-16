=========
CHANGELOG
=========

latest (now)
============

2.0.13 (2018-04-16)
===================

* add ccr module

2.0.12 (2018-03-02)
===================

* add sts module
* add emr module
* add athena module
* add tbaas module
* add partners module

2.0.11
======

* add tmt module
* add apigateway, batch, cloudaudit, scf module

2.0.10
======

2017-11-27

* fix bmlb, cns, feecenter module import error

2.0.9
=====

2017-10-30

* add bgpip module

history
=======

* [2017/9/11] 增加Bmeip和Bmvpc模块
* [2017/8/28] 业务接口的数组参数或者Object参数，支持以Json方式传入，可参考demo.py
* [2017/8/21] 兼容python2和python3版本；支持pip安装使用
* [2017/8/8] 增加Cns模块
* [2017/8/7] 增加Feecenter模块
* [2017/7/31] 增加Bmlb模块
* [2017/7/12] 回滚：不默认传Version参数
* [2017/5/24] 增加Ccs模块
* [2017/5/19]设置接口默认Version： Cvm模块新版本API已经上线，通过是否传Version区分新旧版本。SDK默认调用新接口，因此需要增加Version的默认设置。 CvmAPI接口介绍见：https://www.qcloud.com/document/api/213/569
* [2017/3/1] 增加对HmacSHA1和HmacSHA256签名算法兼容的支持
* [2016/7/15] 增加Tdsql模块
* [2016/7/6] 添加Cmem模块
* [2016/5/24] 添加Cbs、Snapshot和Scaling模块
