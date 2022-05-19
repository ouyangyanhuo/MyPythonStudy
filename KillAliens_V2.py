############################
### Date 2022 May 14     ###
### Author Magneto       ###
### Name KillAliens      <——>
### Facility Windows 11  ###
### Language Python      ###
############################

# 引入 Random 随机模块 十分重要
import random
# 引入 Time 模块，推迟进程一小会，让玩家阅读规则
import time
# 定义 Aliens 字典
aliens_name_and_mark = {
    'Big Alien': 10,
    'Middle Alien': 5,
    'A Alien': 2,
    'Small Alien': 1
}
# 储存用户信息 包括用户名、分数
Data = {'The_name': '', 'The_marks': 0}
# 对照组，用于判断一定概率下是否击杀了 Aliens
state_one = ['1', '2', '3', '4', '5']
# 欢迎语
print("欢迎来到 KillAliens 小游戏，字典已经初始化完成\n接下来请输入内容\n")
Data['The_name'] = input("你的名字：\n\t")
print(f"你好 \033[94m{Data['The_name']}\033[0m ，接下来让我为你介绍游戏中有的 Alien 以及其对应的分数！\n")
# 推迟 1 秒钟 给予反应时间
time.sleep(1)
# 循环输出字典内容
for name, marks in aliens_name_and_mark.items():
    print(f"\t击杀 {name} 可以获得 {marks} 分")
# 推迟 1 秒钟 给予反应时间
time.sleep(1)
# 开始循环，每完成一次就从此处开始
while True:
    # 输出 当前分数
    print(f"\n当前你的分数是 \033[35m{Data['The_marks']}\033[0m 分")
    # 提示退出游戏或继续游戏
    exit_the_game = input("\n如果你想退出游戏，请输入 'quit' ，退出游戏，或输入其它任意值开始(继续)游戏。\n\t")
    if exit_the_game == 'quit':
        break
    # 提示内容输入
    print("请输入你想要击杀的 Alien 的 \033[94m 名称 \033[0m 击杀成功后，可获得指定分数")
    # 循环输出字典内容
    for name, marks in aliens_name_and_mark.items():
        print(f"\t名称：{name}\n\t\t对应分数：{marks}")
    print("请注意，你有概率无法击杀 Alien 并且会因此结束游戏，并且对应分数越高，击杀几率越小。")
    time.sleep(1)
    # 开始输入
    ChoiseAliens = input("请输入对应名称：\n\t")
    # 计算并处理
    if ChoiseAliens == 'Small Alien':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '3', '4', '5', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Small Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 1 分")
            # 算法
            Data['The_marks'] = Data['The_marks'] + aliens_name_and_mark['Small Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 \033[94m {Data['The_name']} \033[0m ,你尝试击杀 Small Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    elif ChoiseAliens == 'A Alien':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '3', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 A Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 2 分")
            # 算法
            Data['The_marks'] = Data['The_marks'] + aliens_name_and_mark['A Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 A Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    elif ChoiseAliens == 'Middle Alien':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Middle Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 \033[94m {Data['The_name']} \033[0m ，击杀成功，获得 5 分")
            # 算法
            Data['The_marks'] = Data['The_marks'] + aliens_name_and_mark['Middle Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 Middle Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    elif ChoiseAliens == 'Big Alien':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Big Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 \033[94m{Data['The_name']}\033[0m ，击杀成功，获得 10 分")
            # 算法
            Data['The_marks'] = Data['The_marks'] + aliens_name_and_mark['Big Alien']
            print(f"当前总分：\033[35m{Data['The_marks']}\033[0m 分\n\n\n")
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 \033[94m{Data['The_name']}\033[0m ,你尝试击杀 Big Alien 失败了，分数清零，退出游戏。")
            break
    else:
        print("您需要输入对应的\033[94m名称\033[0m，而不是其它内容。")
