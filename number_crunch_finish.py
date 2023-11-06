# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:17:26 2023

@author: ethan.drover
"""

import random



tuple_data = (0,5,10,15,20,25,30,35,40,45,50)
totalsum = (sum(tuple_data))
avg = totalsum/len(tuple_data)
min_num = min(tuple_data)
max_num = max(tuple_data)

sorted_data = sorted(tuple_data)
n = len(sorted_data) // 2
if len(sorted_data) % 2 == 0:
    median = (sorted_data[n - 1] + sorted_data[n]) / 2
else:
     median = sorted_data[n]
    
duplicates = [item for item in tuple_data if tuple_data.count(item) > 1]
duplicates = list(set(duplicates))
           
print(f"Tuple Data = {tuple_data} \nAverage = {avg} Median = {median} Min = {min_num} Max = {max_num} Duplicates = {duplicates}")

rand_data = [random.randint(0,50) for num in range(0,12)]
avg_rand = ((sum),rand_data)

totalsum = (sum(rand_data))
avg = totalsum/len(rand_data)
min_num = min(rand_data)
max_num = max(rand_data)

sorted_data = sorted(rand_data)
n = len(rand_data) // 2
if len(rand_data) % 2 == 0:
    median = (rand_data[n - 1] + rand_data[n]) / 2
else:
     median = rand_data[n]
    
duplicates = [item for item in rand_data if rand_data.count(item) > 1]
duplicates = list(set(duplicates))

print(f"\nRandom Data = {rand_data} \nAverage = {avg} Median = {median} Min = {min_num} Max = {max_num} Duplicates = {duplicates}")