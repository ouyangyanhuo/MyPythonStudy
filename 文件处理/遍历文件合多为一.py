###################################
### Date 2023 Apr 15            ###
### Author Magneto              ###
### Name Multiple files in one  <——>
### Facility Windows 11         ###
### Language Python             ###
###################################

# 说明：本文件用于将指定目录下的指定类型的文件的内容全部合到一个新文件内
# 本代码适用于 Windows 目录填写的形式不能为单斜杠而是双斜杠
# 即 不能是 C:\Users\user\Desktop 而应该是 C:\\Users\\user\\Desktop
import os

def find_files(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

def main():
    # 指定目录
    directory = 'C:\\Users\\user\\Desktop'
    # 指定文件类型，即文件后缀 这里以 .log 为例
    extension = '.log'
    # 指定新文件存放目录及名称
    output_file = 'C:\\Users\\user\\Desktop\\ALLINONE.log'

    with open(output_file, 'w') as outfile:
        for file in find_files(directory, extension):
            with open(file) as infile:
                outfile.write(infile.read())

if __name__ == '__main__':
    main()
print("多合一完成")