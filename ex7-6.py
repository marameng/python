# -*- coding: utf-8 -*-
"""
Created on Fri May 18 20:29:24 2018

@author: asus1
"""
def Fundamentalfunction():
    print("\n请选择词典的基本功能")
    print("a:添加")
    print("b:查询")
    print("c:退出")
    print("请选择需要的词典功能：")
    return input()

def addword(worddict:dict):
    d = input("请输入你需要添加的单词：")
    if d in worddict():
        print("该单词已经添加到字典库")
    else:
        e = input("请输入中文释义：")
        print(d + '  ' + t + "\n")
    
def searchword(worddict:dict):
    f = ("请输入要查找的单词：")
    if f in worddict():
        print(worddict[f])
    else:
        print("字典库中未找到这个单词")
        
        
while True:     
    def sum():
        g = Fundamentalfunction()
        if g == 'a':
            addword(worddict)
        elif g == 'b':
            selectword(worddict())
        elif g == 'c':   
            break
        else:
            print("输入有误\n")
        
sum()
        
        