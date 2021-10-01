############################
### Date 2021 October 1  ###
### Author Magneto       ###
### Name 坐标移动         <——>
### Random True          ###
### Language Python      ###
############################
# 引入 random 模块
import random
# 定义 spead 内容 并进行随机处理
spead_0 = ['slow', 'medium', 'fast', 'veryfast']
spead_random = random.choice(spead_0)
# 用户输入X坐标
print("\nTell me your X position:")
your_x_position = input()
# 用户输入Y坐标
print("Tell me your Y position:")
your_y_position = input()
# 转化X坐标
x_position = float(your_x_position)
# 转化Y坐标（+1为初始位置）
y_position = float(your_y_position)
# 输出初始坐标值
print(f"\nOriginal X position is {x_position}"
      f"\nOriginal Y position is {y_position}."
      f"\nOriginal position is ({x_position},{y_position}).")
# if-elif-else语句
# 定义slow
if spead_random == 'slow':
    # 算法
    x_increment = x_position + 1
    y_increment = y_position - 2
# 定义medium
elif spead_random == 'medium':
    # 算法
    x_increment = x_position + 2
    y_increment = y_position -1
# 定义fast
elif spead_random == 'fast':
    # 算法
    x_increment = x_position + 3
    y_increment = y_position + 3
# 定义其它内容，假定其它内容速度为极快，达到仪表显示上限
else:
    # 算法
    x_increment = x_position + 4
    y_increment = y_position + 6
# 输出移动后坐标
print(f"New X position is {x_increment}"
      f"\nNew Y position is {y_increment}"
      f"\nNew position is ({x_increment,y_increment})")
# 内容介绍定义
alien = {
    'slow': 'Add 1 X position and reduce 2 Y position',
    'medium': 'Add 2 X position and reduce 1 Y position',
    'fast': 'Add 3 X position and add 3 Y position',
    'veryfast': 'Add 4 X position and add 6 Y position'
}
print("\nIntroduction rules")
# 字符替换和介绍类型总数
if len(alien) == 4:
    # 字符替换
    The_number = 'four'
    # 介绍类型总数
    print(f"There are {The_number} cases in total")
# 其他类型
else:
    # 输出空值
    print("NULL")
# for语句输出
for spead_1, position in alien.items():
    print(f"Spead: {spead_1}")
    print(f"{position}")
