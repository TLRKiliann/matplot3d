#!/usr/bin/python3
# -*-coding:utf-8-*-


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

# Autres paramètres possibles: bmh, grayscale, fivethirtyeight, ggplot, dark_background
style.use('bmh')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [2,3,4,5,6,7,8,9,10]
y = [4,4,4,4,4,6,7,3,7]
z = [2,3,4,5,6,7,8,9,10]

ax1.plot(x,y,z)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')


plt.show()