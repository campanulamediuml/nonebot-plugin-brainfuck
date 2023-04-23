# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import codecs
import os

from setuptools import setup, find_packages


def read_file(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
        # 以下为必需参数
        name='nonebot-plugin-brainfuck',  # 模块名
        version='1.0.4',  # 当前版本
        description='a brainfuck interpreter for nonebot',
        # 简短描述
        license='MIT',
        long_description='a brainfuck interpreter for nonebot',
        author='campanula',
        author_email='campanulamediuml@gmail.com',
        platforms='any',
        keywords="brainfuck",
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
        ],
        url='https://github.com/campanulamediuml/nonebot-plugin-brainfuck',
        install_requires=[
            'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
            'nonebot2>=2.0.0-beta.1,<3.0.0'
        ],
        include_package_data=True,
        zip_safe=True,
        packages=find_packages(),
        python_requires='>=3.6',
    )


