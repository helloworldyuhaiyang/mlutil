import os

# 递归打开目录
import re

import cv2


def show_files(path, name_reg):
    """
    根据正则查找文件
    :param path: 查找路径
    :param name_reg: 文件名字匹配的正则
    :return: 文件列表
    """
    pic_file_list = []
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            new_files = show_files(cur_path, name_reg)
            pic_file_list.extend(new_files)
        else:
            # 名字不匹配的跳过
            match = re.match(name_reg, file)
            if match is None:
                continue

            pic_file_list.append(os.path.join(path, file))

    return pic_file_list


def bmp_jpg(file_lists, dst_dir):
    for i, file in enumerate(file_lists):
        # 读图，-1为不改变图片格式，0为灰度图
        img = cv2.imread(file, -1)
        new_name = os.path.basename(file.replace('.bmp', '.jpg'))
        cv2.imwrite(os.path.join(dst_dir, new_name), img)


if __name__ == '__main__':
    files = show_files('/Users/yhy/Downloads/64_CASIA-FaceV5/face_100-199', r'(.*).bmp')
    print(files)

    bmp_jpg(files, '/Users/yhy/Downloads/64_CASIA-FaceV5/test')
