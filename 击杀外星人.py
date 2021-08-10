import random
color_1 = ['red', 'green', 'yellow', 'pink', 'blue']
color_2 = ['red', 'green', 'yellow', 'pink', 'blue', 'palegoldenrod']
color_3 = random.choice(color_2)
if color_3 in color_1[0]:
    print(f"Very good!You killed a {color_3.title()} alien\nYour points will be greatly increased by 10 points")
elif color_3 in color_1[-3]:
    print(f"No!You were killed by {color_3.title()} alien.\nYour points will be greatly reduced by 10 points")
elif color_3 in color_1:
    print(f"Good!You killed a {color_3.title()} alien\nYour points will increase by 5 points")
elif color_3 not in color_1:
    print(f"No!You were killed by {color_3.title()} alien.\nYour points will be reduced by 5 points")