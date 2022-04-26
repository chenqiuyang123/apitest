# -*- coding: utf-8 -*-
# @Time : 2022-04-13 17:07
# @Author : CCC.
# @File : test_api.py
# @Project : pythonProject2

import pytest
from apitest.api.login import auth
from apitest.operaitons.auth import get_token


def test_01():
    response = auth.get_jessionid()
    assert response
    print("jessionid是：",response)



def test_mingdan():
    data = {"pageSize": 50, "pageNum": 1, "params": {"keyword": "", "channel": "12010"}, "jsessionids": auth.get_jessionid()}
    resp = auth.mingdan(json=data).json()
    assert resp.get('result') == 'SUCCESS'


if __name__ == '__main__':
    pytest.main()

