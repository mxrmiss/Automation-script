"""
这个脚本的用处是批量修改文件的名称，如果存在已经修改过的名字的文件(加过前缀)就会跳过
"""
import os
import re
import sys


# 批量修改文件名
def renameall():
    file_name = input("输入你想修改的文件所在的地址：")
    fst_name = input("输入文件前缀名：")
    m_list = []  # 未含有前缀名的文件列表
    num = 1  # 名称变量
    fileList = os.listdir(file_name)  # 待修改文件夹
    print("修改前：\n" + str(fileList))  # 输出文件夹中包含的文件
    currentpath = os.getcwd()  # 得到进程当前工作目录
    os.chdir(file_name)  # 将当前工作目录修改为待修改文件夹的位置
    # 将不含有前缀名的文件添加到列表中
    for fileName in fileList:
        if fst_name in fileName:
            num += 1
        else:
            m_list.append(fileName)
    print('可以修改的文件名列表：\n{}' .format(m_list))

    # 判断列表内容是否为空
    if m_list:
        # 遍历文件夹中所有文件
        for fileName in m_list:
            # 判断文件是否有后缀名
            if "." not in fileName:
                # 没有后缀名直接添加后缀名
                os.rename(fileName, (fst_name + str(num) + '.jpg'))
                print(fileName)
                num += 1
            # 有后缀名匹配后缀名
            else:
                pat = ".+\.(jpg|png|jpeg)"  # 匹配文件名正则表达式
                pattern = re.findall(pat, fileName)  # 进行匹配
                os.rename(fileName, (fst_name + str(num) + '.' + pattern[0]))  # 文件重新命名
                num += 1
        print("---------------------------------------------------")
        os.chdir(currentpath)  # 改回程序运行前的工作目录
        sys.stdin.flush()  # 刷新
        print("修改后：" + str(os.listdir(file_name)))  # 输出修改后文件夹中包含的文件
    else:
        print("没有可重命名的文件")
        return None


# try:
#     renameall()
# except:
#     print("出错了!!!!快用999小葵花牌感冒灵 :)")
renameall()