print("提示：最终结果的显示时间取决与CPU的算力和你输入的数大小\n建议输入一千万以下的数字，数字太大无法在短时间内得出结果")
x = int(input('输入一个数：'))
z = 0
for i in range(1,x+1):
    if x % i == 0:
        z = z+1
if z > 2:
    print("不是素数")
else:
    print("是素数")
