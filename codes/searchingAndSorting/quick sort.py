# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:51:31 2021

@author: SouLs-TaKeR
"""

def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot=list1.pop()
    lesser_list=[]
    greater_list=[]
    for items in list1:
        if items < pivot:
            lesser_list.append(items)
        else:
            greater_list.append(items)

    print(lesser_list, greater_list)
    value = quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)
    # print(value)
    return value

def list_input():
    val = [23, 34, 8, 1, 45, 92, 60, 71, 44, 9, 59]
    # val = []
    # n=int(input("enter no. of elements : "))
    # for i in range(n):
    #     element=int(input("enter numbers : "))
    #     val.append(element)
    print(val)
    print(quick_sort(val))
    

list_input()