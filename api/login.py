# -*- coding: utf-8 -*-
# @Time : 2022-04-15 11:05
# @Author : CCC.
# @File : login.py
# @Project : pythonProject2

from apitest.base.request import HttpRequest
from apitest.base.read_data import  ReadFile
import os




class Auth(HttpRequest):
    def get_jessionid(self):
        ss = ReadFile().load_file("login.json")
        login =self.get('http://192.168.1.154:5050/centerweb/cloud/sysUser/login',params =ss)
        return dict(login.cookies).get("jsessionids")

    def mingdan(self,**kwargs):
        return self.post("http://192.168.1.154:5050/dnas/pis/common/queryPatient",**kwargs)


auth = Auth()

