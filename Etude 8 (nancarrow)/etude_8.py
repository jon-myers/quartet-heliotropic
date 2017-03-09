from combo import *
from note_stream_three_octaves import *
from numpy import random

durs=[0.5*(1/6)**(random.random_sample()) for i in range(9)]
durs.sort()
# durs=[1/16,1/13,1/11,1/9,1/7,1/5,1/4,1/3,1/2]
durs=[i*4 for i in durs]

def gridder(grid_len):
    count=0
    while count< grid_len:
        count=0
        grid = [random.random_sample() for i in range(10)]
        grid.sort()
        grid.append(1)
        for i in range(len(grid)-1):
            if grid[i+1]-grid[i]>0.05:
                count+=1
        if count==grid_len-1:
            return grid


grid=gridder(11)

durs_fl=[[grid[0],durs[1]],[grid[2],durs[2]],[grid[3],durs[0]],[grid[4],durs[2]],[grid[7],durs[3]],[grid[10],durs[1]]]
durs_cl=[[grid[0],durs[3]],[grid[1],durs[4]],[grid[2],durs[2]],[grid[3],durs[5]],[grid[4],durs[2]],[grid[5],durs[4]],[grid[7],durs[3]],[grid[9],durs[4]],[grid[10],durs[3]]]
durs_vln=[[grid[0],durs[5]],[grid[1],durs[4]],[grid[3],durs[5]],[grid[5],durs[4]],[grid[6],durs[6]],[grid[7],durs[3]],[grid[8],durs[6]],[grid[9],durs[4]],[grid[10],durs[5]]]
durs_vla=[[grid[0],durs[7]],[grid[3],durs[5]],[grid[6],durs[6]],[grid[7],durs[8]],[grid[8],durs[6]],[grid[10],durs[7]]]

tot=240


# fl1=[renderer(durs_fl[i][1],durs_fl[i+1][1],(durs_fl[i+1][0]-durs_fl[i][0])*tot) for i in range(len(durs_fl)-1)]
# z_fl=[i for i in itertools.chain.from_iterable(fl1)]
#
# # cl1=[renderer(durs_cl[i][1],durs_cl[i+1][1],(durs_cl[i+1][0]-durs_cl[i][0])*tot) for i in range(len(durs_cl)-1)]
# # z_cl=[i for i in itertools.chain.from_iterable(cl1)]
# #
# # vln1=[renderer(durs_vln[i][1],durs_vln[i+1][1],(durs_vln[i+1][0]-durs_vln[i][0])*tot) for i in range(len(durs_vln)-1)]
# # z_vln=[i for i in itertools.chain.from_iterable(vln1)]
#
# vla1=[renderer(durs_vla[i][1],durs_vla[i+1][1],(durs_vla[i+1][0]-durs_vla[i][0])*tot) for i in range(len(durs_vla)-1)]
# z_vla=[i for i in itertools.chain.from_iterable(vla1)]

z_fl=renderer(1/2,1/2,5)+renderer(1/2,1/3,31.6948)+renderer(1/3,1/3,5)
z_vla=renderer(1/4,1/4,5)+renderer(1/4,1/3,31.6948)+renderer(1/3,1/3,5)

# z_fl=renderer(2/6,8/30,30)+renderer(12/45,32/225,30)+renderer(32/225,1/2,30)
# z_cl=renderer(2/5,1,30)+renderer(1,2,30)+renderer(2,3,30)
# z_vln=renderer(2/4,4/12,30)+renderer(3/9,4/27,20)+renderer(4/27,.1,10)
# z_vla=renderer(2/2,2/4,30)+renderer(2/4,2/12,20)+renderer(2/12,.1,10)

env_fl=([(0,0),(0.5,0),(1,0)],[(0,23),(0.5,1),(1,23)])
# env_cl=([(0,12),(0.25,12),(.75,12),(1,12)],[(0,22),(0.25,22),(.5,22),(1,22)])
# env_vln=([(0,4),(0.25,4),(.75,4),(1,4)],[(0,14),(0.25,14),(.75,14),(1,14)])
env_vla=([(0,0),(0.5,0),(1,0)],[(0,23),(0.5,1),(1,23)])

q_fl=concater_rester(cloner(z_fl,env_fl,4,[4,10],300,3),84,0)[:len(z_fl)]
# q_cl=concater_rester(cloner(z_cl,env_cl,4,[4,10],300,2),58,0)[:len(z_cl)]
# q_vln=concater_rester(cloner(z_vln,env_vln,4,[4,10],300,2),55,0)[:len(z_vln)]
q_vla=concater_rester(cloner(z_vla,env_vla,4,[4,10],300,3),36,0)[:len(z_vla)]

midier(z_fl,q_fl,74,'piano 1')
# midier(z_cl,q_cl,72,'clarinet')
# midier(z_vln,q_vln,74,'violin')
midier(z_vla,q_vla,72,'piano 2')

# fl, d5-e6       74 - 88
# cl, f#4-A5      66 - 81
# vln, B3 - c5    59 - 72
# vla, c3 - e4    48 - 64

# 55,62,69,76
# 64,69,74,79

# flute, use: cowell, c4 - a6  : midi, 60 - 93 : range(34)   myers: c4  - g6   midi 60-91
# clarinet: d3-a#6,      : midi,                             myers: a#3 - f6   midi 58-89
# violin: use cowell, g3 - g6 : 55 - 91 : range(37)          myers: g3 -  d6   midi 55-86
# viola: use cowell, c3 - g5 : 48 - 79 : range(32)           myers: c3 -  g5   midi 48-79

# durs go less/more/less/more/less/more

# 1/7      10    1/14: 1/2
# 1/6     8     1/12: 1/2
# 1/5    6      1/10: 1/2
# 1/4    4      1/8: 1/2



# t_env_vla=([(0,4),(1,2)],[(0,4),(1,8)])
# import numpy as np
# xed=np.linspace(0,1,5)
# xed=[np.asscalar(xed[i]) for i in range(len(xed))]
# [ranger(i,t_env_vla[0],t_env_vla[1],'no') for i in xed]
# ranger()