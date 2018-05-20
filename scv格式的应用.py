# -*- coding: utf-8 -*-
"""
Created on Sun May 20 09:45:19 2018

@author: asus1
"""
fo = open("score.csv","r")#打开一个文件
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()

className = ls[0][1:] 
min_grade = [100,100,100]
max_grade = [0,0,0]
ave_grade =[0,0,0]
for s in ls[1:]: 
    for i in range(3):#求出每个科目的最高分与最低分
        grade = float(s[i+1])
        if grade > max_grade[i]:
            max_grade[i] = grade
        elif grade < min_grade[i]:
            min_grade[i] = grade
        ave_grade[i] += grade#计算每个科目的总分
for i in range(3):
    ave_grade[i] = ave_grade[i]/( len(ls) - 1)  #计算平均数
    
           
for i in range(3):
    print("{}的最高分是： {}，最低分是：{},平均分是{}".format(className[i], max_score[i], min_score[i],ave_grade[i])) #输出成绩

ls[0].append("总分")#求每个人的总分
for i in range(1, len(ls)):
    sum = 0
    for j in range(1, len(ls[i])):
        sum += int(ls[i][j])
    ls[i].append(str(sum))
    
fy = open("newscore.csv","w")#创建一个新的文件
for row in ls:
    fy.write(",".join(row) + "\n")
print(ls)
fy.close()



        