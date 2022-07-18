# 此算法仅供1000以下数进行运算，数过大无法保证完全正确
print("素数的概念是只可以被1和它本身整除的数字。\n欢迎来到这里，我们将在这里计算你所输入的数字是否为素数。")
while True:
    number = input("输入你的数字吧：")
    number = int(number)
    if number == 2:
        print("是素数")
    elif number == 3:
        print("是素数")
    elif number == 5:
        print("是素数")
    elif number == 7:
        print("是素数")
    elif number == 11:
        print("是素数")
    elif number == 17:
        print("是素数")
    elif number == 13:
        print("是素数")
    elif number == 19:
        print("是素数")
    else:
        if number % 2 == 0:
            print("\t此数可以被2整除，因此不是素数。")
        else:
            if number % 3 == 0:
                print("\t此数可以被3整除，因此不是素数。")
            else:
                if number % 5 == 0:
                    print("\t此数可以被5整除，因此不是素数。")
                else:
                    if number % 7 == 0:
                        print("\t此数可以被7整除，因此不是素数。")
                    else:
                        if number % 11 == 0:
                            print("\t此数可以被11整除，因此不是素数。")
                        else:
                            if number % 13 == 0:
                                print("\t此数可以被13整除，因此不是素数。")
                            else:
                                if number % 17 == 0:
                                    print("\t此数可以被17整除，因此不是素数。")
                                else:
                                    if number % 19 == 0:
                                        print("\t此数可以被19整除，因此不是素数。")
                                    else:
                                        print("是素数")
