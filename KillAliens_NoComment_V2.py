############################
### Date 2022 May 14     ###
### Author Magneto       ###
### Name KillAliens      <——>
### Facility Windows 11  ###
### Language Python      ###
############################

import random
import time
aliens_name_and_mark = {
    'Big Alien': 10,
    'Middle Alien': 5,
    'A Alien': 2,
    'Small Alien': 1
}
Data = {'The_name': '', 'The_marks': 0}
state_one = ['1', '2', '3', '4', '5']
print("欢迎来到 KillAliens 小游戏，字典已经初始化完成\n接下来请输入内容\n")
Data['The_name'] = input("你的名字：\n\t")
print(f"你好 \033[94m{Data['The_name']}\033[0m ，接下来让我为你介绍游戏中有的 Alien 以及其对应的分数！\n")
time.sleep(1)
for name, marks in aliens_name_and_mark.items():
    print(f"\t击杀 {name} 可以获得 {marks} 分")
time.sleep(1)
while True:
    print(f"\n当前你的分数是 \033[35m{Data['The_marks']}\033[0m 分")
    exit_the_game = input("\n如果你想退出游戏，请输入 'quit' ，退出游戏，或输入其它任意值开始(继续)游戏。\n\t")
    if exit_the_game == 'quit':
        break
    print("请输入你想要击杀的 Alien 的 \033[94m 名称 \033[0m 击杀成功后，可获得指定分数")
    for name, marks in aliens_name_and_mark.items():
        print(f"\t名称：{name}\n\t\t对应分数：{marks}")
    print("请注意，你有概率无法击杀 Alien 并且会因此结束游戏，并且对应分数越高，击杀几率越小。")
    time.sleep(1)
    ChoiseAliens = input("请输入对应名称：\n\t")
    if ChoiseAliens == 'Small Alien':
        state_two = ['1', '2', '3', '4', '5', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Small Alien")
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 1 分")
            Data['The_marks'] += aliens_name_and_mark['Small Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        else:
            print(f"很遗憾 \033[94m {Data['The_name']} \033[0m ,你尝试击杀 Small Alien 失败了，分数清零，退出游戏。")
            break
    elif ChoiseAliens == 'A Alien':
        state_two = ['1', '2', '3', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 A Alien")
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 2 分")
            Data['The_marks'] += aliens_name_and_mark['A Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 A Alien 失败了，分数清零，退出游戏。")
            break
    elif ChoiseAliens == 'Middle Alien':
        state_two = ['1', '2', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Middle Alien")
        if The_Random in state_one:
            print(f"恭喜你 \033[94m {Data['The_name']} \033[0m ，击杀成功，获得 5 分")
            Data['The_marks'] += aliens_name_and_mark['Middle Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 Middle Alien 失败了，分数清零，退出游戏。")
            break
    elif ChoiseAliens == 'Big Alien':
        state_two = ['1', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Big Alien")
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 10 分")
            Data['The_marks'] += aliens_name_and_mark['Big Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 Big Alien 失败了，分数清零，退出游戏。")
            break
    else:
        print("您需要输入对应的\033[94m名称\033[0m，而不是其它内容。")
