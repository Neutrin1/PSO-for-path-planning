#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   road.py
@Time    :   2024/02/27 09:58:20
@Author  :   Neutrin 
'''

# here put the import lib
import numpy as np
import math
import parameter
import map
import displayFit


"""
    用粒子群算法解决路径规划问题
    以下是算法的参数
"""
N = 200; #粒子群数量 
D = 2; #搜索空间维度
T = 50; #迭代次数
c1 = c2 = 1.5; #学习因子
w_max = 0.8; w_min = 0.4; #惯性权重
x_max = 600; x_min = 0; #搜索空间范围
v_max = 50; v_min = 10; #速度范围
history_p= np.empty([])   #用于存储最优的粒子历史
#主体
class pso:
    pass
    def __init__(self,start,target): 
        self.start = start
        self.target = target
    
    def pso(self):
        pass 
        #适应度函数
        def fitness(p): #将当前个体位置传进来
            x,y = p
            if math.dist(p,parameter.OB_dot[0])>=50 and math.dist(p,parameter.OB_dot[1])>=50 and math.dist(p,parameter.OB_dot[2])>=50 and math.dist(p,parameter.OB_dot[3])>=50:
                distance = np.sqrt((x - self.target[0])**2 + (y - self.target[1])**2)
                return distance 
            else :
                return 1e6
        #路径
        fitness_history = []  #历史最优适应度 空列表
        p = np.tile(self.start,(200,1)) #个体值复制200份方便映射处理
        v = np.random.uniform(v_min, v_max, size=(N, D))    #初始化速度 随机值 200*2
        #初始化全局最优个体与全局适应度
        global_best_p = p[0] 
        history_p = p[0]
        global_fitness = fitness(global_best_p)
        #初始化个体最优解
        per_best_p = p.copy()
        per_best_fitness = np.array([fitness(x) for x in per_best_p])
        for t in range(T):
        #更新
            r1, r2 = np.random.random(size=(2, N, D))                                   #随机参数    
            v = w_max * v + c1 * r1 *(per_best_p - p) + c2 * r2 * (global_best_p - p) #速度更新
            v = np.clip(v,v_min,v_max)                                                  #限制在区间内
            p = p + v                                                                 #粒子位置更新
            p = np.clip(p,x_min,x_max)                                                #限制在区间内 
        
        #更新个体位置和适应度
            now_fitness = np.array([fitness(x) for x in p])    #更新现在的适应度数组
            verdict = now_fitness < per_best_fitness            #如果现在的适应度小就赋值给个体最优位置
            per_best_p[verdict] = p[verdict] 
            per_best_fitness[verdict] = now_fitness[verdict]    #个体最好适应度的更新
            #re golobal 
            best_idx = np.argmin(per_best_fitness)              #找到最小的适应度的索引
            if per_best_fitness[best_idx]<global_fitness:
                global_best_p = per_best_p[best_idx]
                global_fitness = per_best_fitness[best_idx]
            history_p = np.vstack((history_p, global_best_p))
            fitness_history.append(global_fitness)  
            
        print(history_p)                 
        print(len(history_p))
        print(type(history_p))
        
        for i in range(len(history_p)):
            map.Map.roadDisplay(history_p[i]) #画点

        map.Map.lineDisplay(history_p) #画线
        displayFit.fitnessDisplay(fitness_history)  #画适应度

       
            
if __name__ == '__main__':
    pso(parameter.start_array,parameter.target_array).pso()
    # map.Map(parameter.start_array,parameter.target_array).display_1()
    