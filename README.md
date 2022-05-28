# Python 打包分发流程

## 1. 安装

```
pip install setuptools

pip install wheel
```

## 2. 编写代码

```python
# setup.py

from setuptools import setup, find_packages

setup(
    # 应用名
    name='App',
    # 版本号
    version='0.0.1',
    # 包含所有src中的包
    packages=find_packages('src'),
    # 项目描述
    description='My first Python project',
    # 告诉 distutils 包都在src下
    package_dir={'': 'src'},
    # 打包时需要打包的数据文件，如图片，配置文件等
    package_data={
        # 任何包中含有.txt文件，都包含它
        '': ['*.xml'],
    },
    # 项目依赖的 Python 库，使用 pip 安装本项目时会自动检查和安装依赖
    install_requires=['numpy'],
    # 指定项目依赖的 Python 版本。
    python_requires='>=3.7',
    # 是否使用静态文件，为true时静态文件生效，否则不起作用
    include_package_data=True,
    # 此项需要，否则卸载时报windows error
    zip_safe=False,
    setup_cfg=True
)
```

## 3. 打包方式

### 3.1 Source distribution

> 使用 sdist 可以打包成 source distribution，支持的压缩格式有：

| Format | Description                  | Notes        |
| ------ | ---------------------------- | ------------ |
| zip    | zip file (.zip)              | Windows 默认 |
| gztar  | gzip’ed tar file (.tar.gz)   | Unix 默认    |
| bztar  | bzip2’ed tar file (.tar.bz2) |              |
| xztar  | xz’ed tar file (.tar.xz)     |              |
| ztar   | compressed tar file (.tar.Z) |              |
| tar    | tar file (.tar)              |              |

```sh
# 打源码包
python setup.py sdist --formats=gztar,zip

# 安装
python setup.py install

# pip 安装
pip install xxx.zip

# 开发模式安装
pip install -e .

python setup.py develop
```

### 3.2 Built distribution

> 使用 bdist 可以打出 built distribution，和源码包相比，由于预先构建好，所以安装更快：

| Format  | Description                          | Notes        |
| ------- | ------------------------------------ | ------------ |
| gztar   | gzipped tar file (.tar.gz)           | Unix 默认    |
| bztar   | bzipped tar file (.tar.bz2)          |              |
| xztar   | xzipped tar file (.tar.xz)           |              |
| ztar    | compressed tar file (.tar.Z)         |              |
| tar     | tar file (.tar)                      |              |
| zip     | zip file (.zip)                      | Windows 默认 |
| rpm     | RPM                                  |              |
| pkgtool | Solaris pkgtool                      |              |
| sdux    | HP-UX swinstall                      |              |
| wininst | self-extracting ZIP file for Windows |              |
| msi     | Microsoft Installer.                 |              |

```sh
# 打包二进制包
python setup.py bdist --formats=gztar,zip

python setup.py bdist_wheel

# 安装
pip install dist/cc_utils-0.0.1-py3-none-any.whl
```

## 4. 上传到 PyPI

### 4.1 注册 PyPI 账号

> https://pypi.org/

### 4.2 上传

```shell
pip install twine

twine upload dist/*
```

### 4.3 配置 .pypirc 文件

> Home 目录下创建

```
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
username: 
password: 

[pypitest]
repository: https://test.pypi.org/legacy/
username: 
password: 
```

## 其他

> 清除 .idea 的 git 缓存

```
git rm -r --cached .idea
```