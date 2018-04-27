#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author:loong576
#Alert for wechat
#Version:1.0

import requests
import json
import sys


def Get_Token(Corpid,Secret):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        "corpid":Corpid,                           #企业Id,对应'CorpID'
        "corpsecret":Secret                        #新建应用对应'Secret'
    }
    req = requests.post(url, params=values)
    data = json.loads(req.text)
    Token = data["access_token"]
    return Token


def Send_Message(Token,Toparty,Agentid,Content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    data = {
            #"touser": Touser,                    #成员ID列表,指定为@all，则向关注该企业应用的全部成员发送,对应通讯录'账号'字段
            "toparty": Toparty,                   #部门ID列表，对应部门的'部门ID'字段
            "msgtype": "text",                    #消息类型,该字段非空
            "agentid": Agentid,                   #企业应用的id，整型,非空，对应新建应用的'AgentId'
            "text": {
                    "content":Content             #消息内容,非空
                    },
            "safe":"0"                            #表示是否是保密消息，0表示否，1表示是，默认0
            }
    res = requests.post(url,json=data)
    return res.text



if __name__ == '__main__':
    #Touser = sys.argv[1]
    Toparty = sys.argv[1]                         #web前端传过来的部门id
    Content = sys.argv[2]                         #web前端传过来的告警内容
    Corpid = "ww6b6da9aedc0b137d"
    Secret = "xtHo9zSM8NMm6-eOnCc2qnjox5flEdWGlKBdPcWoUow"
    Agentid = "1000002"

    Token = Get_Token(Corpid,Secret)
    print Get_Token(Corpid,Secret)
    print Send_Message(Token,Toparty,Agentid,Content)
