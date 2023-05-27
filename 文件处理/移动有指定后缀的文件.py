# 导入os模块
import os

# 定义源文件夹和目标文件夹
source_dir = "C:\\Users\\user\\Desktop"
target_dir = "C:\\Users\\user\\Desktop\\raw"

# 遍历源文件夹中的所有文件
for file in os.listdir(source_dir):
    # 如果文件的后缀是.文件后缀名，就移动到目标文件夹
    if file.endswith(".文件后缀名"):
        # 拼接完整的文件路径
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, file)
        # 移动文件
        os.rename(source_path, target_path)
        # 打印移动成功的信息
        print(f"Moved {file} from {source_dir} to {target_dir}")
