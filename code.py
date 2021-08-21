# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 05:19:15 2021

@author: AliRaza
"""
import math


print("\n\n\nMean,Median,Mode,Variance,Standard Deviation for Grouped data\n\n")


# L_limit1=List Lower Limit of class interval
L_limit1=[]
# U_limit1=List of Upper Limit of class interval
U_limit1=[]
# f1=list of frequency
f1=[]
# lcb=List of lower class boundaries
lcb=[]
# ucb=List of Upper class boundaires
ucb=[]
# x=Midpoint of class intervals
x=[]
# fx=product of f and x
fx=[]
bar=[]
bar_square=[]

from bisect import bisect_left

def takeClosest(myList, myNumber):
    
    if (myNumber > myList[-1] or myNumber < myList[0]):
        return False
    pos = bisect_left(myList, myNumber)
    if pos == 0:
            return myList[0]
    if pos == len(myList):
            return myList[-1]
    before = myList[pos - 1]
    after = myList[pos - 1]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before
# Took maximum value of lists and also apply condition for variable to not take values other than integer
while True:
        try: 
            value=int(input("Enter the number of classes(intervals)= "))
            break
        except:
            print("This is not an integer please enter valid integer")
# loop to iterate store data into the lists 
# first take input from and user
# Then store than one by one

for i in range(0,value):
    while True:
        try:
            L_limit=int(input("Enter lower limit value=  "))
            U_limit=int(input("Enter Upper limit value=  "))
            f=int(input("Enter the frequency in this limit=  "))
            break
        except:
            print("This is not an integer please enter valid integer")
# insert each input element of each list into their repective list
    L_limit1.insert(i,L_limit)
    U_limit1.insert(i,U_limit)
    f1.insert(i,f)
    lcb.insert(i,L_limit1[i]-0.5)
    ucb.insert(i,U_limit1[i]+0.5)
    x.insert(i,(L_limit1[i]+U_limit1[i])/2)
    fx.insert(i,f1[i]*x[i])
# Find the group width
    h=ucb[i]-lcb[i]
# find the commulative frequency
v = 0
cumsum = [v := v + n for n in f1]
# find the median or modal class
mid_number=sum(f1)/2
median_class_index=(cumsum.index(takeClosest(cumsum,mid_number)))+1

print(median_class_index)

    
print("  lower limit\t","Upper limit\t","L.C.B\t","U.C.B\t","Frequency\t")
# loops to iterate over each list and display their data in a table
for i in range(0,value):
    print("\t",L_limit1[i],"\t\t   ",U_limit1[i],"\t\t\t",lcb[i],"\t",ucb[i],"\t\t",f1[i])
    
print("Midpoint(X)","  \tfx","\t\t\tcf") 

for i in range(0,value):
    print("\t",x[i],"\t\t",fx[i],"\t\t",cumsum[i])

summation_of_fx=sum(fx)

summation_of_x=sum(f1) 

# find mean of the data using formula

Mean=summation_of_fx/summation_of_x


for i in range(0,value):
    xbar=x[i]-Mean
    bar.insert(i,xbar)
    xbarsquare=xbar*xbar
    bar_square.insert(i,xbarsquare)

summation_of_bar=sum(bar)
summation_of_bar_square=sum(bar_square)

print("\tX-Xbar","\t\t\t\t\tX-Xbar_Square") 

for i in range(0,value):
    print(bar[i],"\t\t",bar_square[i])
    
print("Mean of the data is =  ",Mean)
# find median of the data using formula

Median=lcb[median_class_index]+((mid_number-cumsum[median_class_index-1])/f1[median_class_index])*h

print("Median of the data is =  ",Median)

# find mode of the data using formula

Mode=lcb[median_class_index]+((f1[median_class_index]-f1[median_class_index-1])/((f1[median_class_index]-f1[median_class_index-1])+(f1[median_class_index]-f1[median_class_index+1])))*h

print("Mode of the data is =  ",Mode)


Variance=summation_of_bar_square/summation_of_x

print("Variance of the data is = ",Variance)

print("Standard Deviation of the data is = ",math.sqrt(Variance))


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

print("\n\n\t\t\t\tEngr. Ali Raza\n\n")
