# coding = utf-8
import itchat

# 登录
itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 保存朋友信息到本地
def save_friends(friends):
  with open('friends.txt', 'w') as f:
    friends_list = ''
    for friend in friends:
      data = (friend.NickName, friend.RemarkName, '男' if friend.Sex == 1 else '女', friend.Province + friend.City, friend.Signature)
      info = '昵称：%s\n备注：%s\n性别：%s\n地点：%s\n签名：%s\n'%data
      friends_list += info + '='*30 + '\n'
    f.write(friends_list)

# 统计男女性别比
from pyecharts import Pie

def comput_sex_rate(friends):
  male = female = other = 0

  for friend in friends:
    sex = friend['Sex']
    if sex == 1:
      male += 1
    elif sex == 2:
      female += 1
    else:
      other += 1

  count = {
    'male': male,
    'female': female,
    'other': other
  }

  show_chart(count, male = male, female = female, other = other)

def show_chart(rate, **count):
  pie = Pie(u'%s的微信好友性别比例' % (friends[0]['NickName']), title_pos='center')
  attr = ['男性', '女性', '其他']
  v1 = [count['male'], count['female'], count['other']]
  pie.add("", attr, v1, radius=[40, 75], label_text_color=None,\
    is_label_show=True, legend_orient='vertical',
    legend_pos='left')
  pie.render()

comput_sex_rate(friends)
