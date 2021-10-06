# -*- coding: utf-8 -*-
"""

Created on Wed Oct  6 12:24:57 2021

@author: Travis J Czechorski

Github: https://github.com/tjczec01

Email:   travis.czechorski@maine.edu
         tjczec01@gmail.com
        
Advisor: thomas.schwartz@maine.edu
       
Github:  https://github.com/tjczec01 
         https://github.com/TravisCzechorskiUMaine

"""

def hcmass(C, H, O):
    cm = 12.0107
    om = 15.999 
    hm = 1.00784
    
    totmass = (cm * C) + (om * O) + (hm * H)
    return totmass

# Question 2

xylose = hcmass(5, 10, 5)
propp = hcmass(3, 8, 0)
myy = propp/xylose
mass = 0.293333333333333
xy = 50.2
prop = 15.7
hvvy = (xy*myy)/prop
print("Question 2\n")
print("Mass Yeild: {:.3}, {:.3} %".format(myy, 100 * myy))
print("Energy Yeild: {:.3}, {:.3} %\n\n".format(hvvy, 100 * hvvy))
c2 = (xy*mass)/prop

# Question 3

print("Question 3\n")
d = [3.0, 4.0, 5.0]
a = []
for i in d:
    pi = 3.141592653589793
    r = i/2
    asc = pi*(r**2)
    a.append(pi*(r**2))
    print("Cross-sectional area: {:.3} nm^2 (D = {} nm)".format(asc, int(i)))

# Question 5

# 1 gallon = 3785 cm**3
cmtogal = 1 / 3785
galtocm = 3785
mton = 1000
kgwood = mton * 1000 # kg/day
water = 1500000  #  L
wkg = water * 1  #  kg
xylan = kgwood * 0.06  # kg
galactoglucomannan = kgwood * 0.16
gcc = galactoglucomannan  #  kg
sugars = xylan + gcc  #  kg
total = wkg + gcc + xylan  #  kg
aanswer = xylan/total
banswer = gcc/total
gcmass = 180.15
etohmass = 46.07
yy = (2 * etohmass) / gcmass
kgetoh = yy * gcc
getoh = kgetoh * 1000 #  g
cmetoh = getoh/0.789  #  cm^3
gallon = cmetoh * cmtogal
print("\n\nQuestion 5\n")
print("{:.3} kg_xylose / kg_solution".format(aanswer)) 
print("{:.3} kg_sugars / kg_solution".format(banswer)) 
print("Grams of Ethonal: {}\nCubic centimeters of Ethonal: {}".format(format(int(getoh), ","), format(int(cmetoh), ",")))
print("Mass yeild of Ethonal: {:.3}, {:.3} %\n{:.3} kg of Ethonal".format(yy, yy * 100, format(int(kgetoh), ",")))
print("Gallons of Ethonal: {}".format(format(int(gallon), ",")))
    
    
