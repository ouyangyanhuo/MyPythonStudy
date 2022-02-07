############################
### Date 2022 January 24 ###
### Author Magneto       ###
### Name BMI计算         <——>
### Facility iPad        ###
### Language Python      ###
############################
#欢迎界面
print("Hello!Nice to meet you what's your name?")
the_name = input()
print(f"\nOk!{the_name}. Let's calculate your BMI and classification(adult)")
#输入值
print("\nEnter your weight(kg)")
weight = input()
print("\nEnter your height(m)")
height = input()
#转化值
your_weight = float(weight)
your_height = float(height)
#计算
number = your_weight/(your_height*your_height)
the_number = float(number)
#得出数值
print(f"\nHi {the_name}!Your BMI number is {the_number} \n")
#分析
if the_number < 18.5:
  print(f"Oh!{the_name}!You're underweight and BMI is below standerd.")
elif 18.5 <= the_number <= 23.9:
  print(f"{the_name},your BMI is normal.")
elif 23.9 < the_number <= 27.9:
  print(f"{the_name},you're overweight and BMI is higher than the standard.")
elif 27.9 < the_number <= 32:
  print(f"{the_name},you're too fat and BMI well above the mark")
else:
  print(f"{the_name},you're severely exeed the limit please lose weight")
print("\nThe norm come from PRC")
x = input('Press Enter to exit')
