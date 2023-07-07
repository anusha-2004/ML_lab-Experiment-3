#!/usr/bin/env python
# coding: utf-8

# # Write a program to find mean,median,mode and standard deviation

# In[1]:


def mean_vec(arr):
    avg=sum(arr)/len(arr)
    return avg
def med_vec(arr):
    if(len(arr)%2==0):
        return (sorted(arr)[(len(arr)//2)-1]/2)+(sorted(arr)[len(arr)//2]/2)
    return sorted(arr)[len(arr)//2]
def mode_arr(arr):
    max_count = 0
    mode = 0
    for i in arr:
        if arr.count(i) > max_count:
            max_count = arr.count(i)
            mode = i
    return mode
def standarddev_vec(arr):
    avg=sum(arr)/len(arr)
    var=sum([((x-avg)**2) for x in arr])/len(arr)
    return var**(1/2)
arr=[15,25,36,26,26,26,21,8,3,5,12,21]
print(arr)
print("Mean of the array:",mean_vec(arr))
print("Median of the array:",med_vec(arr))
print("Mode of the array:",mode_arr(arr))
print("Standard deviation of the array:",standarddev_vec(arr))


# In[2]:


import numpy as np
import statistics
arr=[15,25,36,26,26,26,21,8,3,5,12,21]
print(np.mean(arr))
print(np.median(arr))
print(statistics.mode(arr))
print(np.std(arr))

