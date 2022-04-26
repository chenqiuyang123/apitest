
# -*- coding: utf-8 -*-
# @Time : 2022/4/13 14:47
# @Author : CCC.
# @File : request.py
# @Project : pythonProject2

import json as _json
import requests
from apitest.base.logger import logger


class HttpRequest():
    # 接口做post一般都是采用json格式进行提交
    __headers = {
        "content-type": "application/json;charset=UTF-8"
    }

    def __init__(self):
        self.__session = requests.session()

    def get(self, path, **kwargs):
        return self.__request(path, 'GET', **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        return self.__request(path, 'POST', data, json, **kwargs)

    def __request(self, url, method, data=None, json=None, **kwargs):
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        # 如果传入header不为空，那么更新header
        if headers:
            self.__headers.update(headers)
        self.__request_log(url, method, data, json, params, self.__headers)
        resp = None
        if method == "GET":
            resp = self.__session.get(url, **kwargs)
        elif method == "POST":
            resp = requests.post(url, data, json, **kwargs)
        self.__response_log(resp)
        return resp

    def __request_log(self, url, method, data=None, json=None, params=None, headers=None):
        logger.info("接口请求地址: {}".format(url))
        logger.info("接口请求方式: {}".format(method))
        logger.info("接口请求头: {}".format(_json.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数: {}".format(_json.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 : {}".format(_json.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数: {}".format(_json.dumps(json, indent=4, ensure_ascii=False)))

    def __response_log(self, resp):
        try:
            logger.info("返回信息 : {}".format(resp.text, ensure_ascii=False))
        except Exception as e:
            logger.error('系统错误：{}'.format(e))













