############################
### Date 2023 Apr 15     ###
### Author Magneto       ###
### Name DataProcessing  <——>
### Facility Windows 11  ###
### Language Python      ###
############################
print('说明：本文件用于遍历指定目录下的指定文件类型，\n寻找该类型文件内是否有符合关键词的内容，\n并将内容含有该关键词的文件复制一份到另一目录')
import os
import shutil

def find_files(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

def main():
    # 需要遍历的目录
    directory = 'C:\\Users\magne\\Desktop\\websitelogs_2023'
    # 需要遍历的目录内文件类型
    extension = '.json'
    # 需要寻找的关键词
    search_string = '/Theme/tina_update.json'
    # 复制的文件保存位置
    destination_directory = 'C:\\Users\\magne\\Desktop\\websitelogs_2024'

    for file in find_files(directory, extension):
        with open(file) as f:
            if search_string in f.read():
                shutil.copy(file, destination_directory)

if __name__ == '__main__':
    main()

print('查找完成')