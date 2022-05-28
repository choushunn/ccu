# -*- coding: utf-8 -*-
"""
@Time       : 2022/05/14 20:14
@Author     : Spring
@FileName   : setup.py
@Description: 
"""
from setuptools import setup, find_packages, find_namespace_packages


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


requirements = [

]

setup(
    # 应用名
    name='ccu',
    # 版本号
    version='0.0.1',
    # 作者
    author='choushunn',
    # 作者邮箱
    author_email='choushunn@163.com',
    # 项目描述
    description='Common Utils',
    # 长文描述
    long_description=readme(),
    # 长文描述的文本格式
    long_description_content_type='text/markdown',
    # 包含所有 src 中的包
    packages=find_namespace_packages(include=['ccu.*']),
    # 项目依赖的 Python 库，使用 pip 安装本项目时会自动检查和安装依赖
    install_requires=requirements,
    # 指定项目依赖的 Python 版本。
    python_requires='>=3.7',
)

