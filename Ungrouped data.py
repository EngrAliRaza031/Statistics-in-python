# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:53:43 2021

@author: AliRaza
"""
import math

print("\n\n\nMean,Median,Mode,Variance,Standard Deviation for Ungrouped data\n")

import numpy
from scipy import stats
list1=[]
bar1=[]
bar_square1=[]
while True:
        try:
            max_index=int(input("Enter maximum length of the list "))
            break
        except:
            print("This is not an integer please enter valid number")

for i in range(0,max_index):
    while True:
        try:
            elements=int(input("Enter elements of list= "))
            break
        except:
            print("This is not an integer please enter valid number")
    list1.insert(i,elements)

mean = numpy.mean(list1)

for i in range(0,max_index):
    xbar1=list1[i]-mean
    bar1.insert(i,xbar1)
    xbar_square1=xbar1*xbar1
    bar_square1.insert(i,xbar_square1)
summation_of_x1=sum(list1)   
summation_of_bar_square1=sum(bar_square1)
print("\tX-Xbar","\t\tX-Xbar_Square") 

for i in range(0,max_index):
    print("\t",bar1[i],"\t\t",bar_square1[i])

print("\nMean of the data is = ",mean)
median = numpy.median(list1)
print("\nMedian of the data is = ",median)
mode = stats.mode(list1)
print("\nMode of the data is = ",mode)

Variance1=summation_of_bar_square1/max_index
Variance2=summation_of_bar_square1/((max_index)-1)
print("\nVariance of the (Population) data is = ",Variance1)

print("\nVariance of the (sample) data is = ",Variance2)

print("\nStandard Deviation of the (Population) data is = ",math.sqrt(Variance1))

print("\nStandard Deviation of the (Sample) data is = ",math.sqrt(Variance2))

print("\n\n\t\t\t\tEngr. Ali Raza.Class:BDA. Assignment No 1\n\n")