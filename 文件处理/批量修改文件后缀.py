# 导入os模块
import os

# 定义要修改后缀的文件夹路径
folder_path = "C:\\Users\\user\\Desktop\\data"

# 遍历文件夹中的所有文件
for file in os.listdir(folder_path):
    # 获取文件名和后缀名
    file_name, file_ext = os.path.splitext(file)
    # 如果后缀名是.A，就修改为.B
    if file_ext == ".A":
        # 生成新的文件名
        new_file_name = file_name + ".B"
        # 生成新的文件路径
        new_file_path = os.path.join(folder_path, new_file_name)
        # 生成旧的文件路径
        old_file_path = os.path.join(folder_path, file)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
