"""
利用tinypng的API进行图片压缩，每月免费额度为500张，建议设置代理，
无论是中文网站还是英文网站使用的服务器都是一样的，如果不使用代理服务器，速度会非常的慢
"""


import os
import sys
import tinify
import re

tinify.key = "gdZWPjDLgDY64T7rSpHSBQF5KmbhdQJy"  # tinypng API
tinify.proxy = "http://127.0.0.1:10809"  # tinypng 代理

pic_url = input('请输入需要压缩图片所在的文件夹地址：')
new_list = []       # 新图片放置的列表
file_list = os.listdir(pic_url)  # 待修改文件夹
print("修改前：\n" + str(file_list))  # 输出文件夹中包含的文件
current_path = os.getcwd()  # 得到进程当前工作目录
os.chdir(pic_url)  # 将当前工作目录修改为待修改文件夹的位置


# 单个图片压缩
def singlePic(pic):
    new_pic = 'job' + pic
    source = tinify.from_file(pic)
    source.to_file(new_pic)
    print("压缩后图片名称为：{}" .format(new_pic))


# 多个图片压缩
def pics():
    for filename in file_list:
        new_pic = 'job' + filename
        source = tinify.from_file()
        source.to_file(new_pic)
        new_list.append(new_pic)
        print("压缩后图片名称为：\n" + new_list)


pic_num = input("压缩单个图片选1，压缩多张图片选2，退出选3：")
while 1:
    if pic_num == 1:
        pic_single = input("请输入单个需要压缩的图片地址：")
        singlePic(pic_single)
    elif pic_num == 2:
        pass
    elif pic_num == 3:
        break
    else:
        print("输入错误，请重新输入！！")

# 查看图片尺寸
"""
source = tinify.from_file("large.jpg")
resized = source.resize(
    method="fit",
    width=150,
    height=100
)
resized.to_file("thumbnail.jpg")
"""