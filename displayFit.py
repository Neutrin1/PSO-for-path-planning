#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   displayFit.py
@Time    :   2024/02/28 17:06:02
@Author  :   Neutrin 
'''

# here put the import lib

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # simsun是宋体
def fitnessDisplay(fitness):
        fig,ax1 = plt.subplots()
        ax1.plot(fitness)
        ax1.set_title('fitness')