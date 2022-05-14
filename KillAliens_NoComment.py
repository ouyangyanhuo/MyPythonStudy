############################
### Date 2022 May 14     ###
### Author Magneto       ###
### Name KillAliens      <——>
### Facility Windows 11  ###
### Language Python      ###
############################
import random
aliens_name_and_mark = {
    'Big Alien': '10',
    'Middle Alien': '5',
    'A Alien': '2',
    'Small Alien': '1',
}
state_one = ['1', '2', '3', '4', '5']
The_mark = ['0']
print("欢迎来到 KillAliens 小游戏，字典已经初始化完成\n接下来请输入内容\n")
Your_name = input("你的名字：")
print(f"你好 {Your_name} ，接下来让我为你介绍游戏中有的 Alien 以及其对应的分数！")
for name, marks in aliens_name_and_mark.items():
    print(f"\t击杀 {name} 可以获得 {marks} 分")
while True:
    exit_the_game = input("如果你想退出游戏，请输入 'q' 键，退出游戏，或输入其它任意值开始(继续)游戏。")
    if exit_the_game == 'q':
        break
    print(f"当前你的分数是 {The_mark[-1]} 分")
    print("请输入对应的 分数 以选择你要击杀的 Alien 击杀成功后，可获得指定分数")
    for name_2, makrs_2 in aliens_name_and_mark.items():
        print(f"\t名称：{name_2}\n\t\t对应分数：{makrs_2}")
    print("请注意，你有概率无法击杀 Alien 并且会因此结束游戏，并且对应分数越高，击杀几率越小。")

    ChoiseAliens = input("请输入对应分数：")
    if ChoiseAliens == '1':
        state_two = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        The_Random = random.choice(state_two)
        print("你选择了 Small Alien")
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 1 分")
            value = The_mark[-1]
            float_value = float(value)
            end_value = float_value + 1
            The_mark.append(end_value)
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            del The_mark[-2]
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Small Alien 失败了，分数清零，退出游戏。")
            break
    if ChoiseAliens == '2':
        state_two = ['1', '2', '3', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 A Alien")
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 2 分")
            value = The_mark[-1]
            float_value = float(value)
            end_value = float_value + 2
            The_mark.append(end_value)
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            del The_mark[-2]
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 A Alien 失败了，分数清零，退出游戏。")
            break
    if ChoiseAliens == '5':
        state_two = ['1', '2', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Middle Alien")
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 5 分")
            value = The_mark[-1]
            float_value = float(value)
            end_value = float_value + 5
            The_mark.append(end_value)
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            del The_mark[-2]
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Middle Alien 失败了，分数清零，退出游戏。")
            break
    if ChoiseAliens == '10':
        state_two = ['1', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Big Alien")
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 10 分")
            value = The_mark[-1]
            float_value = float(value)
            end_value = float_value + 10
            The_mark.append(end_value)
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            del The_mark[-2]
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Big Alien 失败了，分数清零，退出游戏。")
            break
