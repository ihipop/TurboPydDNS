#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017/1/29 22:02
# Project: turboPydDNS
# __author__ = 'ihipop'

from .base import Base3FactsHTTPUpdater
import requests

import logging

logger = logging.getLogger(__name__)

class PubYunUpdater(Base3FactsHTTPUpdater):
    _api_url = 'http://members.3322.net/dyndns/update'
    info_code={
        "good": "成功，IP地址已经成功更新",
        "nochg": "成功，IP地址和上次请求没有变化",
        "badauth": "身份认证出错，请检查用户名和密码, 或者编码方式出错。",
        "badsys": "该域名不是动态域名，可能是其他类型的域名（智能域名、静态域名、域名转向、子域名）。",
        "badagent": "由于发送大量垃圾数据，客户端名称被系统封杀。",
        "notfqdn": "没有提供域名参数，必须提供一个在公云注册的动态域名域名。",
        "nohost": "域名不存在，请检查域名是否填写正确。",
        "!donator": "必须是收费用户，才能使用 offline 离线功能。",
        "!yours": "该域名存在，但是不是该用户所有。",
        "!active": "该域名被系统关闭，请联系公云客服人员。",
        "abuse": "该域名由于段时间大量发送更新请求，被系统禁止，请联系公云客服人员。",
        "dnserr": "DNS 服务器更新失败。",
        "interror": "服务器内部严重错误，比如数据库出错或者DNS服务器出错。"
    }

    def build_payload(self):
        self._query.update({'hostname':self._hostname})
        # print(self._query)
        return super().build_payload()

    def parse_result(self,response:requests.models.Response):
        '''
        http://www.pubyun.com/wiki/帮助:api#接口地址
        :param response:
        :return:
        '''
        logger.debug('Got Response: %s' % response.text.strip())
        text = response.text.strip().split(' ')
        success = False
        if response.status_code == 200:
            if text[0] in ['good','nochg']:
                success = True
            msg = self.info_code.get(text[0],text[0])+ ' (%s)' % text[0]
        else:
            msg = 'invalid http status code: %s' % response.status_code
        return (success,msg)

