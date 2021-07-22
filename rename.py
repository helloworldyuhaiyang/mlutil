import os
import re


def rename(work_dir, name_reg, file_name_start_with, start_number, file_name_end_with):
    print(f"正在生成以{file_name_start_with}{start_number}{file_name_end_with}迭代的文件名")
    count = 0
    file_list = os.listdir(work_dir)
    for f_name in file_list:
        # 名字不匹配的跳过
        match = re.match(name_reg, f_name)
        if match is None:
            continue

        old_path = os.path.join(work_dir, f_name)
        if os.path.isdir(old_path):
            continue
        new_dir = os.path.join(work_dir, file_name_start_with + str(count + int(start_number)) + file_name_end_with)
        os.rename(old_path, new_dir)
        count += 1
    print("一共修改了" + str(count) + "个文件")


if __name__ == '__main__':
    rename("/Volumes/mac2/ml/cover_eye/", r'(.*).jpg', 'cover_', 0, '.jpg')
