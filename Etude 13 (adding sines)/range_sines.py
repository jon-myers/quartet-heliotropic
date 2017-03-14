import numpy as np
import math

def sine_(freq,x,phase):
    return (np.sin(phase*2*np.pi+x*2*np.pi*freq)+1)/2

def range_0(x,oct,shift):
    a=-oct*sine_(2,x,0)+x*shift
    a=np.asscalar(a)
    return a

def range_1(x,oct,shift):
    a=oct*sine_(3,x,0)+range_0(x,oct,shift)
    a = np.asscalar(a)
    return a

def range_2(x,oct,shift):
    a= oct*sine_(4,x,0)+range_1(x,oct,shift)
    a = np.asscalar(a)
    return a

def range_3(x,oct,shift):
    a= oct*sine_(5,x,0)+range_2(x,oct,shift)
    a = np.asscalar(a)
    return a

def range_4(x,oct,shift):
    a= oct*sine_(6,x,0)+range_3(x,oct,shift)
    a = np.asscalar(a)
    return a

def ranger_2(x,inst):
    a=range_0(x,7,0)+11
    b=range_1(x,7.5,0)+11+8
    c=range_2(x,8,0)+11+15
    d=range_3(x,8.5,0)+11+22
    e=range_4(x,9,0)+11+29
    if inst=='fl': return [math.floor(d),math.ceil(e)]
    if inst=='cl': return [math.floor(c),math.ceil(d)]
    if inst=='vln': return [math.floor(b),math.ceil(c)]
    if inst=='vla': return [math.floor(a),math.ceil(b)]


#
# plt.xlim(-1,101)
# # plt.ylim(-0.5,5)
# #
#
# a=[range_0(i/100,7,0)+11 for i in range(101)]
# b=[range_1(i/100,7.5,0)+11+7 for i in range(101)]
# c=[range_2(i/100,8,0)+11+14 for i in range(101)]
# d=[range_3(i/100,8.5,0)+11+21 for i in range(101)]
# e=[range_4(i/100,9,0)+11+28 for i in range(101)]
#
# plt.plot([i for i in range(len(a))],a,'co')
# plt.plot([i for i in range(len(b))],b,'o')
# plt.plot([i for i in range(len(c))],c,'yo')
# plt.plot([i for i in range(len(d))],d,'go')
# plt.plot([i for i in range(len(e))],e,'bo')
#
