#不要抄下源码就运行，你需要改动几个地方

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
bot = Bot()
#bot = Bot(console_qr=2,cache_path="botoo.pkl")#这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为  bot=Bot()
def get_news1():#获取金山词霸每日一句，英文和翻译
    url= "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['translation']
    return contents,translation
def send_news():
    try:
        my_friend = bot.friends().search(u'蓝卉')[0]    #你朋友的微信名称，不是备注，也不是微信帐号。
        #my_friend.send(get_news1()[0])
        #my_friend.send(get_news1()[1][5:])
        my_friend.send(u"测试")
        my_friend.send_image('D:\\test.jpg')
        t = Timer(600, send_news)#每86400秒（1天），发送1次，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
        t.start()
    except:
        my_friend = bot.friends().search('太子duan')[0] #你的微信名称，不是微信帐号。
        my_friend.send(u"今天消息发送失败了")
if __name__ == "__main__":
        send_news()