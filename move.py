# filename : move.py
# author ： aone
# version ： 1.2
# function : 输入一个目录，将其下子目录的文件都移动到此目录下
# 可以选择只深入一层，或者遍历所有子目录

import os
import sys

# 递归调用move()函数
def move(absolute_dirpath):
    for file in os.listdir(absolute_dirpath):
        absolute_filepath = os.path.join(absolute_dirpath,file) # 生成绝对路径名
        if os.path.isfile(absolute_filepath) and (absolute_dirpath == dest_dir):
            pass
        if os.path.isdir(absolute_filepath) and flag!='1': # 如果是目录,且为深度移动，则递归调用move
            move(absolute_filepath)
        else: # 如果是文件，则开始移动                       
            dos_command(absolute_filepath)

# 调用系统命令执行移动操作，而不是使用效率低下的shutil.move()
def dos_command(absolute_filepath):
    global file_count # 为定义在函数外的变量赋值，必须使用global变量
    cmd = ' '.join(['move',quoted(absolute_filepath),quoted(dest_dir)]) # 生成命令
    os.system(cmd) # 执行命令
    print('移动的文件是：',absolute_filepath)
    file_count += 1

# 如果不用引号括起来，要是文件或路径名中含有括号等奇怪字符，会出错
def quoted(s):
    return '"' + s + '"'


# ----------程序开始执行----------

os.system('cls') # 清屏

# 显示欢迎屏幕
print('''欢迎使用文件移动程序！
作者  ： 张宁一
版本  ： 1.2
功能  ： 输入一个目录，将其下子目录的文件都移动到此目录下\n''')

flag = input('''请输入要采取的操作：
 0    ： 退出
 1    ： 一层移动
 其他 ： 深度移动
 --->''')
if flag=='0' :
    print('成功退出，欢迎下次使用！')
    sys.exit(0)

file_count = 0 # 统计移动了多少文件

dest_dir = input('请输入你要整理的目录的绝对路径：\n--->')
# 检查路径合法性
if not os.path.exists(dest_dir):
    print ('此路径不存在，系统将退出！')
    sys.exit(0)
if not os.path.isdir(dest_dir):
    print ('输入的不是一个合法路径，系统将退出！')
    sys.exit(0)

# 执行移动
move(dest_dir)

print("操作成功! 共移动了",file_count,"个文件",sep='')
input("按任意键以退出...")
