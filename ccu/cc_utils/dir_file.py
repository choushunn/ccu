# -*- coding: utf-8 -*-
"""
@Time       : 2022/04/19 12:25
@Author     : Spring
@FileName   : dir_file.py
@Description: 
"""

import glob
import os


def walk_file(file):
    """
    遍历文件夹下的所有文件
    :param file:
    :return:
    """
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            print(os.path.abspath(f))

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.abspath(d))


def get_file_list(path: str, file_type: str = 'jpg', abs_path: bool = False) -> list:
    """
    返回目录中某种文件类型的所有文件列表
    :param abs_path: 是否返回绝对路径
    :param path:搜索路径
    :param file_type:文件类型
    :return:file_type 类型的文件列表
    """
    if abs_path:
        return glob.glob(os.path.abspath(os.path.join(path, '*.' + file_type)))

    return glob.glob(f'{path}/*.{file_type}', recursive=True)




if __name__ == '__main__':
    walk_file("../")
    # print(get_file_list(os.curdir, 'py', True))
