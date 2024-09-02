#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   parameter.py
@Time    :   2024/02/27 09:56:08
@Author  :   Neutrin 
'''

# here put the import lib
import numpy as np
"""
    以下是全局变量
    1. 定义全局变量起点和目标点
    2. 定义全局变量地图参数
    3. 定义障碍物参数
"""
start_array = np.array([[100,100],[100,120],[120,100]])
target_array = np.array([[450,450],[500,470],[500,550]])  
OB_dot= np.array([[150,200],[300,300],[400,400],[400,500]]) #障碍物坐标

# print(start_list[0][0] )