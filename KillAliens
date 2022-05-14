############################
### Date 2022 May 14     ###
### Author Magneto       ###
### Name KillAliens      <——>
### Facility Windows 11  ###
### Language Python      ###
############################

# 引入 Random 随机模块 十分重要
import random
# 定义 Aliens 字典
aliens_name_and_mark = {
    'Big Alien': '10',
    'Middle Alien': '5',
    'A Alien': '2',
    'Small Alien': '1',
}
# 对照组，用于判断一定概率下是否击杀了 Aliens
state_one = ['1', '2', '3', '4', '5']
# 初始分数，使用列表储存，便于后续输出
The_mark = ['0']
# 欢迎语
print("欢迎来到 KillAliens 小游戏，字典已经初始化完成\n接下来请输入内容\n")
Your_name = input("你的名字：")
print(f"你好 {Your_name} ，接下来让我为你介绍游戏中有的 Alien 以及其对应的分数！")
# 循环输出字典内容
for name, marks in aliens_name_and_mark.items():
    print(f"\t击杀 {name} 可以获得 {marks} 分")
# 开始循环，每完成一次就从此处开始
while True:
    # 提示退出游戏或继续游戏
    exit_the_game = input("如果你想退出游戏，请输入 'q' 键，退出游戏，或输入其它任意值开始(继续)游戏。")
    if exit_the_game == 'q':
        break
    # 输出列表的最后一个值
    print(f"当前你的分数是 {The_mark[-1]} 分")
    print("请输入对应的 分数 以选择你要击杀的 Alien 击杀成功后，可获得指定分数")
    # 循环输出字典内容
    for name_2, makrs_2 in aliens_name_and_mark.items():
        print(f"\t名称：{name_2}\n\t\t对应分数：{makrs_2}")
    print("请注意，你有概率无法击杀 Alien 并且会因此结束游戏，并且对应分数越高，击杀几率越小。")
    # 开始输入
    ChoiseAliens = input("请输入对应分数：")
    # 计算并处理
    if ChoiseAliens == '1':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        The_Random = random.choice(state_two)
        print("你选择了 Small Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 1 分")
            # 读取 字典 的最后一个值
            value = The_mark[-1]
            # 由于 字典 中都是数，因此使用 float() 将 字串符 转化为 浮点数
            float_value = float(value)
            # 使用 浮点数 进行运算，得到新值
            end_value = float_value + 1
            # 将上面运算得到的新值重新写入 字典 的最后
            The_mark.append(end_value)
            # 读取 字典 的最后一个值
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            # 删除 字典 的倒数第二个值，节约内存
            del The_mark[-2]
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Small Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    if ChoiseAliens == '2':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '3', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 A Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 2 分")
            # 读取 字典 的最后一个值
            value = The_mark[-1]
            # 由于 字典 中都是数，因此使用 float() 将 字串符 转化为 浮点数
            float_value = float(value)
            # 使用 浮点数 进行运算，得到新值
            end_value = float_value + 2
            # 将上面运算得到的新值重新写入 字典 的最后
            The_mark.append(end_value)
            # 读取 字典 的最后一个值
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            # 删除 字典 的倒数第二个值，节约内存
            del The_mark[-2]
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 A Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    if ChoiseAliens == '5':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '2', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Middle Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 5 分")
            # 读取 字典 的最后一个值
            value = The_mark[-1]
            # 由于 字典 中都是数，因此使用 float() 将 字串符 转化为 浮点数
            float_value = float(value)
            # 使用 浮点数 进行运算，得到新值
            end_value = float_value + 5
            # 将上面运算得到的新值重新写入 字典 的最后
            The_mark.append(end_value)
            # 读取 字典 的最后一个值
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            # 删除 字典 的倒数第二个值，节约内存
            del The_mark[-2]
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Middle Alien 失败了，分数清零，退出游戏。")
            break
    # 计算并处理
    if ChoiseAliens == '10':
        # 实验组，用于和上面的 对照组 对应，实现判断击杀
        state_two = ['1', '6', '7', '8']
        The_Random = random.choice(state_two)
        print("你选择了 Big Alien")
        # 如果 实验组 生成的数在 对照组 则输出此结果
        if The_Random in state_one:
            print(f"恭喜你 {Your_name} ，击杀成功，获得 10 分")
            # 读取 字典 的最后一个值
            value = The_mark[-1]
            # 由于 字典 中都是数，因此使用 float() 将 字串符 转化为 浮点数
            float_value = float(value)
            # 使用 浮点数 进行运算，得到新值
            end_value = float_value + 10
            # 将上面运算得到的新值重新写入 字典 的最后
            The_mark.append(end_value)
            # 读取 字典 的最后一个值
            print(f"当前总分：{The_mark[-1]} 分\n\n\n")
            # 删除 字典 的倒数第二个值，节约内存
            del The_mark[-2]
        # 如果 实验组 生成的数不在 对照组 则输出此结果，并结束进程
        else:
            print(f"很遗憾 {Your_name} ,你尝试击杀 Big Alien 失败了，分数清零，退出游戏。")
            break
