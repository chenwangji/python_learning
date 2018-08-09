#coding:utf-8
import itchat
from itchat.content import *
import re
from threading import Timer

# 目前是按用户发送的，用的 itchat.search_friends， 如果要改为群聊，需要换成 itchat.search_chatrooms
xyz_compile = re.compile(r'.*?绿健简报.*', re.S)
@itchat.msg_register(itchat.content.TEXT)
def xyz_reply(msg):
  group_list = [u'filehelper']
  group_name = []
  for group in group_list:
    chat = itchat.search_friends(name=group)
    if len(chat) > 0:
      group_name.append(chat[0]['UserName'])
    # 兼容 filehelper
    elif group == u'filehelper':
      group_name.append(group)
  # 过滤小宇宙新闻
  # 需要换成小宇宙的 UserName
  MY_NAME = itchat.search_friends(userName=msg['FromUserName'])['NickName']
  print(MY_NAME)
  if msg['FromUserName'] is not None and MY_NAME == u'陈望基':
    result = xyz_compile.search(msg['Content'])
    if result is not None:
      if result.group() is not None:
        for group in group_name:
          itchat.send(msg['Content'], toUserName=group)

def loop_send():
  global count
  itchat.send('大扎好，我系轱天乐，我四渣嘎辉，探挽懒月，介四里没有挽过的船新版本，'
              '挤需体验三番钟，里造会干我一样，爱像借款游戏。'
              , toUserName='filehelper')
  count += 1
  if count < 10000:
    Timer(600, loop_send).start()

if __name__ == '__main__':
  count = 0
  Timer(600, loop_send).start()
  itchat.auto_login(enableCmdQR=2, hotReload=True)
  itchat.run()