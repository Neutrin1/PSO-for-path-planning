#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   map.py
@Time    :   2024/02/26 15:49:36
@Author  :   Neutrin 
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt
import parameter 
import pso
#添加一张画布
fig,ax = plt.subplots(tight_layout=True)
obstacle = []
"""
    以下是一个地图类，所有画图的操作都在这个类中
"""
class Map():
    pass
    def __init__(self,start_array,target_array,ob_dot):
        self.start_array = start_array
        self.target_array = target_array
        self.ob_dot = ob_dot
        self.background_x = np.linspace(0, 500, 500)
        self.background_y = np.linspace(0, 500, 500)
        
    
    def display_1(self):
        background_x, background_y = np.meshgrid(self.background_x, self.background_y)
        #画出出发点和目标点
        for i in range(len(self.start_array)):
            ax.scatter(self.start_array[i][0],self.start_array[i][1],color='r')
            ax.scatter(self.target_array[i][0],self.target_array[i][1],color='b')
        ax.set_xlim(0,600)
        ax.set_ylim(0,600)
        ax.set_xlabel('X(km)')
        ax.set_ylabel('Y(km)')
        #画障碍区域
        for i in range(4):
            ob = plt.Circle((self.ob_dot[i][0],self.ob_dot[i][1]),40,color = 'g')
            obstacle.append(ob)
            ax.add_patch(obstacle[i])
        ax.set_aspect('equal')    
        plt.show()

    def roadDisplay(point):
        ax.scatter(point[0],point[1],color='black',s = 0.01)
    
    def lineDisplay(history_p):
        for i in range(len(history_p)-1):
            ax.plot([history_p[i][0],history_p[i+1][0]],[history_p[i][1],history_p[i+1][1]],color = 'black')
        ax.set_title('path')
if __name__ == '__main__':
    Map(parameter.start_array,parameter.target_array,parameter.OB_dot).display_1()
    