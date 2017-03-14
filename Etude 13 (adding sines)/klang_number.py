import numpy as np
from note_stream import next_note

def k_sine_(freq,x):
    return (np.sin(-1*np.pi/2+x*2*np.pi*freq)+1)/2

def klang_0(x,oct,shift,add):
    a=oct*k_sine_(2,x)+x*shift+add
    a = np.asscalar(a)
    return a

def klang_1(x,oct,shift,add):
    a=oct*k_sine_(2.5,x)+klang_0(x,oct,shift,add)+add
    a = np.asscalar(a)
    return a

def klang_2(x,oct,shift,add):
    a=oct*k_sine_(3,x)+klang_1(x,oct,shift,add)+add
    a=np.asscalar(a)
    return a


from matplotlib import pyplot as plt
#
# a=[klang_0(i/100,2,3,2) for i in range(101)]
# b=[klang_1(i/100,2,3,3) for i in range(101)]
# # c=[klang_2(i/100,1,0) for i in range(101)]
# # d=[tempo_3(i/100,1,-1)+2 for i in range(101)]
#
#
# # plt.xlim(-1,101)
# # plt.ylim(-0.5,5)
# plt.plot([i for i in range(len(a))],a,'co')
# plt.plot([i for i in range(len(b))],b,'o')
# plt.plot([i for i in range(len(c))],c,'yo')
# plt.plot([i for i in range(len(d))],d,'go')

import math


def klang_numberer(z_,inst):
    probs=[1 for i in range(30)]
    if inst == 'vla':
        k_range_min=klang_0
        k_range_max=klang_1
    elif inst == 'vln':
        k_range_min=klang_0
        k_range_max=klang_1
    else:
        k_range_min = klang_0
        k_range_max = klang_1
    klang_nums=[]
    while sum(klang_nums) < len(z_)+1:
        x=sum(klang_nums)/len(z_)
        min_=math.floor(k_range_min(x,2,3,2))
        max_=math.ceil(k_range_max(x,2,3,3))
        set=[i for i in range(min_,max_)]
        klang_nums.append(next_note([i for i in set],[probs[i] for i in set],3))
        probs=[i+1 for i in probs]
        probs[klang_nums[-1]] = 0
    return klang_nums

# klang_numberer([i for i in range(100)],'vla')