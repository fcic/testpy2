#!/usr/bin/python
#coding=utf-8
import json
import urllib2

class iciba:
    # 初始化
    def __init__(self, wechat_config):
        self.appid = wechat_config['appid']
        self.appsecret = wechat_config['appsecret']
        self.template_id = wechat_config['template_id']
        self.access_token = ''

    # 获取access_token
    def get_access_token(self, appid, appsecret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, appsecret)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_data = response.read()
        data = json.loads(json_data)
        access_token = data['access_token']
        self.access_token = access_token
        return self.access_token

    # 发送消息
    def send_msg(self, openid, template_id, iciba_everyday):
        msg = {
            'touser': openid,
            'template_id': template_id,
            'url': iciba_everyday['fenxiang_img'],
            'data': {
                'content': {
                    'value': iciba_everyday['content'],
                    'color': '#0000CD'
                    },
                'note': {
                    'value': iciba_everyday['note'],
                },
                'translation': {
                    'value': iciba_everyday['translation'],
                }
            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
        request = urllib2.Request(url, data=json_data)
        response = urllib2.urlopen(request)
        result = response.read()
        return json.loads(result)

    # 获取爱词霸每日一句
    def get_iciba_everyday(self):
        url = 'http://open.iciba.com/dsapi/'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_data = response.read()
        data = json.loads(json_data)
        return data

    # 为设置的用户列表发送消息
    def send_everyday_words(self, openids):
        everyday_words = self.get_iciba_everyday()
        for openid in openids:
            result = self.send_msg(openid, self.template_id, everyday_words)
            if result['errcode'] == 0:
                print ' [INFO] send to %s is success' % openid
            else:
                print ' [ERROR] send to %s is error' % openid

    # 执行
    def run(self, openids):
        self.send_everyday_words(openids)


if __name__ == '__main__':
   # 微信配置
    wechat_config = {
        'appid': 'wx59af624256b8c0fc', #此处填写你的appid
        'appsecret': '8a6f87de9883f4f7ba90ea35cbdbb212', #此处填写你的appsecret
        'template_id': 't7www6LiRfAQPxHgHBMF4zHpIrxzPEltlNxa2rb0Uco' #此处填写你的模板消息ID
    }
    # 用户列表
    openids = [
        'ozis801RqDc19L7qtLQV6u2pL93U', #此处填写你的微信号
        #'xxxx', #如果有多个用户也可以
    #'xxxx',
    ]
    # 执行
    icb = iciba(wechat_config)
    icb.run(openids)
