# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:03:46 2018

@author: asus1
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
radar_labels = np.array(['力量','经验','防守','发球','技术','速度'])
nAttr = 6
data = np.array([[5,5,5,5,5,5],
                 [4,5,5,5,5,5],
                 [5,5,5,5,5,4],
                 [5,5,4,5,5,4],
                 [5,5,4,4,5,5],
                 [5,5,4,4,5,5]]) #数据值

data_labels = ('马龙','张继科','许昕','丁宁','刘诗雯','朱雨玲')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
#plt.plot(angles,data,'bo-',color ='gray',linewidth=1,alpha=0.2)
plt.plot(angles,data,'o-', linewidth=1.5, alpha=0.2)
plt.fill(angles,data, alpha=0.25)
plt.thetagrids(angles*180/np.pi, radar_labels,frac = 1.2)
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
plt.grid(True)
plt.show()

