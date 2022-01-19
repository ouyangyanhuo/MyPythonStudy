# 随便写的，真的很辣鸡
def get_formatted_name(first_name,last_name ,middle_name='',age=None):
    if middle_name:
        people = f"{first_name} {middle_name} {last_name}"
        if age:
            people = f"{first_name} {middle_name} {last_name}'s year is {age}"
    else:
        people = {'first': first_name, 'last': last_name}
        if age:
            people['age'] = age
    return people
while True:
    print("Tell me you want use what data or enter 'No' to enter yourself's name.")
    print("Enter 'q' at any time to quit.")
    Use_data = input()
    if Use_data == 'List 1':
        people = get_formatted_name('wang', 'yunzhong', age=16)
    elif Use_data == 'List 2':
        people = get_formatted_name('jimi', 'lee', 'hendrix')
    elif Use_data == 'q':
        break
    elif Use_data == 'No':
        f_name = input("First name: ")
        m_name = input("Middle_name: ")
        l_name = input("Last name: ")
        if m_name:
            people = get_formatted_name(f_name, m_name, l_name)
        else:
            people = get_formatted_name(f_name, l_name)
    elif Use_data == 'List 3':
        people = get_formatted_name('mr', 'dor', 'hua', age=16)
    elif Use_data == 'List 4':
        people = get_formatted_name('feng','yaohua' ,age=16)
    print(f"The print is {people}")
