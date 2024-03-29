# 从指定目录获取抽样结果到目标目录

import os
import random
import shutil


# 随机采样移动文件
# return 被移动的文件
def copy_yolo_file(from_img_dir, dst_img_dir, rate, from_label_dir, dst_label_dir):
    if rate > 1 or rate < 0:
        raise ValueError

    # 取图片的原始路径
    src_files = os.listdir(from_img_dir)
    file_number = len(src_files)

    # 按照rate比例从文件夹中取一定数量图片
    sample_number = int(file_number * rate)

    # 随机选取 sample_number 数量的样本图片
    sample_files = random.sample(src_files, sample_number)
    for name in sample_files:
        # 从 from_img_dir 复制图片到 dst_img_dir 目录
        shutil.copy(os.path.join(from_img_dir, name), os.path.join(dst_img_dir, name) )
        # 从 from_label_dir 复制图片对应的 dst_label_dir 目录
        label_name = name.replace("jpg", "txt")

        label_file = from_label_dir + label_name
        if os.path.exists(label_file) is not True:
            raise FileNotFoundError(label_file)

        copy_file = shutil.copy(os.path.join(from_label_dir, label_name), os.path.join(dst_label_dir, label_name) )
        print(copy_file)


def move_yolo_file(from_img_dir, dst_img_dir, rate, from_label_dir, dst_label_dir):
    if rate > 1 or rate < 0:
        raise ValueError

    # 取图片的原始路径
    src_files = os.listdir(from_img_dir)
    file_number = len(src_files)

    # 按照rate比例从文件夹中取一定数量图片
    sample_number = int(file_number * rate)

    # 随机选取 sample_number 数量的样本图片
    sample_files = random.sample(src_files, sample_number)
    for name in sample_files:
        # 从 from_img_dir 复制图片到 dst_img_dir 目录
        shutil.move(os.path.join(from_img_dir, name), os.path.join(dst_img_dir, name) )
        # 从 from_label_dir 复制图片对应的 dst_label_dir 目录
        label_name = name.replace("jpg", "txt")

        label_file = from_label_dir + label_name
        if os.path.exists(label_file) is not True:
            raise FileNotFoundError(label_file)

        copy_file = shutil.move(os.path.join(from_label_dir, label_name), os.path.join(dst_label_dir, label_name) )
        print(copy_file)


if __name__ == '__main__':
    # 源图片目录
    # from_img = "/Users/yhy/Downloads/mask/images/train/"
    # # 源图片目录
    # dst_img = "/Users/yhy/Downloads/mask/images/val/"
    # # 源标签目录
    # from_label = "/Users/yhy/Downloads/mask/labels/train/"
    # # 目标标签目录
    # dst_label = "/Users/yhy/Downloads/mask/labels/val/"

    from_img = "/Users/yhy/Downloads/cover_eye/cover_eye_0/images/"
    # 源图片目录
    dst_img = "/Users/yhy/Downloads/cover_eye_test/images/train/"
    # 源标签目录
    from_label = "/Users/yhy/Downloads/cover_eye/cover_eye_0/labels/"
    # 目标标签目录
    dst_label = "/Users/yhy/Downloads/cover_eye_test/labels/train/"

    move_yolo_file(from_img, dst_img, 1, from_label, dst_label)


