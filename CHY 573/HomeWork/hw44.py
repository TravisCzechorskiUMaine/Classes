# -*- coding: utf-8 -*-
"""

Created on Sun Oct  3 16:00:56 2021

@author: Travis J Czechorski

Github: https://github.com/tjczec01

Email:   travis.czechorski@maine.edu
         tjczec01@gmail.com
        
Advisor: thomas.schwartz@maine.edu
       
Github:  https://github.com/tjczec01 
         https://github.com/TravisCzechorskiUMaine

"""

import pandas as pd
import math as mt
import statistics
import pprint as pp


first_value = -205.03321728960572
df = pd.read_excel(r'/home/travis/Desktop/CHE573/StandardDevLJ.xlsx')  # put your excel file path here
energy_list = df['{}'.format(first_value)].tolist()
energy_list.insert(0, first_value)

mean = sum(energy_list) / len(energy_list)
variance = sum([((x - mean) ** 2) for x in energy_list]) / len(energy_list)
res = variance ** 0.5

def std_dev(pop_list):
    N = len(pop_list)
    print("Number of values: {}".format(N))
    AVG = sum(pop_list)/(len(pop_list))
    print("Population Average: {}".format(AVG))
    subtracted_values = [(i - AVG)**2 for i in pop_list]
    numerator = sum(subtracted_values)
    final_value = mt.sqrt(numerator/N)
    return final_value

answer = std_dev(energy_list)

print("Standard deviation from sample code: {}".format(res))
print("Standard deviation from python statistics package: {}".format(statistics.stdev(energy_list)))
print("Standard deviation from self: {}".format(answer))
