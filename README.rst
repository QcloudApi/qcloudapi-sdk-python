===============================
The Qcloud API SDK for Python
===============================

Qcloud Python SDK is the official software development kit, which allows Python developers to write software that makes use of qcloud services like CVM and CBS.

The SDK works on Python versions:

   * 2.7 and greater, including 3.x.x

Quick Start
-----------
First, install the library:

.. code-block:: sh

    $ pip install qcloudapi-sdk-python

or download source code from github and install:

.. code-block:: sh

    $ git clone https://github.com/QcloudApi/qcloudapi-sdk-python.git
    $ cd qcloudapi-sdk-python
    $ python setup.py install

Then, from a Python interpreter or script:

.. code-block:: python

    >>> from QcloudApi.qcloudapi import QcloudApi
    >>> module = 'cvm'
    >>> action = 'DescribeInstances'
    >>> config = {'Region':'ap-guangzhou', 'secretId':'xxxx', 'secretKey':'xxxx', 'Version':'2017-03-20'}
    >>> params = {'Limit':1}
    >>> service = QcloudApi(module, config)
    >>> service.call(action, params)
