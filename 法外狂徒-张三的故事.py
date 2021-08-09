# 引入random模块
import random
# 给X Y Z赋值
x, y, z = 2, 4, 10
# 我们的圆桌可以坐下的人
People_sitting_on_the_table = (x*z+y)/4
#  除了李四外可以坐的人
People_sitting_on_the_table_2 = x*z-15
# 可邀请的人的名单
name_list = ['张一', '张二', '法外狂徒-张三', '老王', '老李', '老郭', '老孟', '小王', '小李', '小郭', '小孟']
# 张一张二的问题
fight = '张一'
fight_2 = '张二'
name_list.remove('张一')
name_list.remove('张二')
# 但是法外狂徒-张三邀请了李四一起参加宴席
name_list.append('李四')
# Name_list里此时的人数
name_list_numbers = len(name_list)
# 输出
print('明天有个宴会，我要邀请一些人来参加\n'
      f"计划被邀请的人有{name_list[0]}、{name_list[1]}、{name_list[2]}、{name_list[3]}、{name_list[4]}、{name_list[5]}、{name_list[6]}、{name_list[7]}、{name_list[8]}、{name_list[9]}、"
      f"{fight}、{fight_2}\n"
      f"因为{fight}和{fight_2}在打架，所以来不了了。\n"
      f"因此我可以邀请{name_list[0]}、{name_list[1]}、{name_list[2]}、{name_list[3]}、{name_list[4]}、{name_list[5]}、{name_list[6]}、{name_list[7]}、{name_list[8]}、{name_list[9]}"
      f"这{name_list_numbers}个人。\n虽然我很想把他们都邀请来，但是我们的桌子只能坐下{People_sitting_on_the_table}个人，所以我必须随机抽{People_sitting_on_the_table}个人,并且不重复。\n"
      f"我把这个消息说给了{name_list[0]}，他说无论如何{name_list[-1]}必须来，否则他就要告诉我什么是法外狂徒\n"
      f"因此，接下来我必须抽{People_sitting_on_the_table_2}个人，并且必须把{name_list[-1]}也加入进去")
# 技术限制，只能做个摸球并放回的故事了
attend_name = random.choice(name_list)
attend_name_1 = random.choice(name_list)
attend_name_2 = random.choice(name_list)
attend_name_3 = random.choice(name_list)
attend_name_4 = random.choice(name_list)
# 二次输出
print('经过了4个小时终于完成了随机抽取。\n'
      f"我抽出了，{attend_name}、{attend_name_1}、{attend_name_2}、{attend_name_3}、{attend_name_4}这{People_sitting_on_the_table_2}个人，并且加入了{name_list[-1]}。\n"
      f"我走到法外狂徒-张三面前把，结果告诉了他，他心满意足的离开了。\n"
      f"第二天，我邀请的{attend_name}、{attend_name_1}、{attend_name_2}、{attend_name_3}、{attend_name_4}这{People_sitting_on_the_table_2}个人都参加了这个宴席"
      f"{name_list[0]}由于法外狂徒击杀了{name_list[-1]}，增加了EXP"
      f"因此和{attend_name}、{attend_name_1}、{attend_name_2}、{attend_name_3}、{attend_name_4}这{People_sitting_on_the_table}个人一起出席了这个宴席\n"
      f'{name_list[0]}坐在最好的位置，说出了他最宏伟的计划——击杀罗翔！\n'
      '室内一片哗然，但最终大家都同意了法外狂徒-张三的计划，并且一步一步实行着……')
