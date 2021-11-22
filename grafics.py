import matplotlib.pyplot as plt
import numpy as np

t = []
v = []
r = []

def graphic(satellite_v, satellite_r,  time):
    t.append(time)
    v.append(satellite_v)
    r.append(satellite_r)

with open("stats.txt", 'r') as input_file:
    for line in input_file:
        data = line.split()
        velocity = (data[7]**2 + data[8]**2)**0.5
        graphic(velocity, data[2], data[0])
        # Timer, obj.obj.type, obj.obj.R, obj.obj.color, obj.obj.m, obj.obj.x, obj.obj.y, obj.obj.Vx, obj.obj.Vy

def draw_garphic():

    plt.subplots(2,2, figsize=(10,10))

    #subplot 1
    sp = plt.subplot(221)
    plt.plot(r, v)
    plt.title('v(r)')
    plt.xlabel('r, m')
    plt.ylabel('v, m/s')

    #subplot 2
    sp = plt.subplot(222)
    plt.plot(t, v)
    plt.title('v(t)')
    plt.xlabel('t, s')
    plt.ylabel('v, m/s')

    #subplot 3
    sp = plt.subplot(223)
    plt.plot(t, r)
    plt.title('r(t)')
    plt.xlabel('t, s')
    plt.ylabel('r, m')

    plt.show()