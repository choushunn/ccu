# -*- coding: utf-8 -*-
"""
@Time       : 2022/04/19 10:24
@Author     : Spring
@FileName   : init_env.py
@Description: 初始化环境
"""
import json
import os
import platform


def init_pip(mirror_url="mirrors.aliyun.com"):
    """
    初始化pip.ini
    :param mirror_url:镜像源url
    :return:
    """
    # 判断操作系统是否为 windows
    if platform.system() == "Windows":
        pip_ini = os.path.expanduser('~/pip/pip.ini')
        print("当前系统为 Windows")
    elif platform.system() == "Linux":
        pip_ini = os.path.expanduser('~/.pip/pip.conf')
        print("当前系统为 Linux")
    else:
        print("暂不支持该操作系统")
        return

    # 判断pip文件夹是否存在
    if not os.path.exists(pip_ini):
        os.makedirs(os.path.dirname(pip_ini), exist_ok=True)

    # 向 pip.ini写入镜像配置
    with open(pip_ini, 'w') as f:
        f.write("[global]\n")
        f.write(f"index-url = https://{mirror_url}/pypi/simple/\n")
        f.write("[install]\n")
        f.write(f"trusted-host = {mirror_url}\n")
        print("pip.ini 初始化完成")


def init_condarc(mirror_url="mirrors.bfsu.edu.cn", set_env_dir=False):
    """
    初始化 condarc
    :param mirror_url:镜像源url
    :param set_env_dir:是否设置环境目录
    :return:
    """
    condarc = os.path.expanduser('~/.condarc')
    # 向 condarc 写入镜像配置
    with open(condarc, 'w') as f:
        if set_env_dir:
            f.write("envs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\envs\n")
            f.write("pkgs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\pkgs\n")
        f.write("channels:\n")
        f.write("  - defaults\n")
        f.write("show_channel_urls: true\n")
        f.write("default_channels:\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/main\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/r\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/msys2\n")
        f.write("custom_channels:\n")
        f.write(f"  conda-forge: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  msys2: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  bioconda: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  menpo: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch-lts: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  simpleitk: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  paddle: https://{mirror_url}/anaconda/cloud\n")
        f.write("ssl_verify: true\n")
        print("condarc 初始化完成")


def init_kaggle(username, key):
    """
    初始化kaggle
    :param username:用户名
    :param key:密钥
    :return:
    """
    kaggle_file = os.path.expanduser('~/.kaggle/kaggle.json')
    # 判断文件夹是否存在
    if not os.path.exists(kaggle_file):
        os.makedirs(os.path.dirname(kaggle_file), exist_ok=True)
    json_data = {"username": username, "key": key}
    with open(kaggle_file, 'w') as f:
        json.dump(json_data, f)
    print("kaggle 初始化完成")


if __name__ == '__main__':
    init_pip()
    init_condarc()
    # init_kaggle("choushunn", "b8ab8a9b3b872bce7e1669808eb91159")
