import numpy as np
def t_sine_(freq,x):
    return (np.sin(-1*np.pi/2+x*2*np.pi*freq)+1)/2

def tempo_0(x,oct,shift):
    a=oct*t_sine_(2,x)/(x+1)+x*shift-(oct/2)*t_sine_(1,x)/(x+1)
    a=np.asscalar(a)
    return a

def tempo_1(x,oct,shift):
    a=oct*t_sine_(3,x)/(x+1)+tempo_0(x,oct,shift)
    a = np.asscalar(a)
    return a

def tempo_2(x,oct,shift):
    a= oct*t_sine_(4,x)/(x+1)+tempo_1(x,oct,shift)
    a = np.asscalar(a)
    return a

def tempo_3(x,oct,shift):
    a= oct*t_sine_(5,x)/(x+1)+tempo_2(x,oct,shift)
    a = np.asscalar(a)
    return a

# from matplotlib import pyplot as plt
#
# a=[tempo_0(i/100,1,1)+2 for i in range(101)]
# b=[tempo_1(i/100,1,1)+2 for i in range(101)]
# c=[tempo_2(i/100,1,1)+2 for i in range(101)]
# d=[tempo_3(i/100,1,1)+2 for i in range(101)]
#
#
#
#
# # plt.xlim(-1,101)
# # plt.ylim(-0.5,5)
# plt.plot([i for i in range(len(a))],a,'co')
# plt.plot([i for i in range(len(b))],b,'o')
# plt.plot([i for i in range(len(c))],c,'yo')
# plt.plot([i for i in range(len(d))],d,'go')
#
# # points of interest
# poi0=[0,1/4,2/4,3/4,1,1/3,2/3]
# poi1=[0,1/6,2/6,3/6,4/6,5/6,1,1/4,3/4]
# poi2=[0,1/8,2/8,3/8,4/8,5/8,6/8,7/8,1,1/5,2/5,3/5,4/5]
# poi3=[0,1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10]



