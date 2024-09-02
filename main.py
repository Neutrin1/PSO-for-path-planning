#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2024/02/25 14:14:05
@Author  :   Neutrin 
'''

# here put the import lib
import numpy as np
import map
import pso
import parameter
from matplotlib.font_manager import FontProperties
"""
    以下是主程序
"""
pso.pso(parameter.start_array[0],parameter.target_array[0]).pso()
# pso.pso(parameter.start_array[1],parameter.target_array[1]).pso()
# pso.pso(parameter.start_array[2],parameter.target_array[2]).pso()
map.Map(parameter.start_array,parameter.target_array,parameter.OB_dot).display_1()


