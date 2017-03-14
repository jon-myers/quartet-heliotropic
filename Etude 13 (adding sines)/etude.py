


from combo import *
from note_stream import *
from numpy import random
from tempo_sines import *


init_dur = 2.2

tot=8*60
# points of interest
poi0=[0,1/4,2/4,3/4,1,1/3,2/3]
poi0.sort()
# poi1=[0,1/6,2/6,3/6,4/6,5/6,1,1/4,3/4]
# poi1.sort()
# poi2=[0,1/8,2/8,3/8,4/8,5/8,6/8,7/8,1,1/5,2/5,3/5,4/5]
# poi2.sort()
# poi3=[0,1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,1]
# poi3.sort()

render=smooth_curve_exact_durtot
rend_times=render(10,30,tot)
rend_times=[sum(rend_times[:i+1]) for i in range(len(rend_times))]
rend_times=[rend_times[i]/tot for i in range(len(rend_times))]

poi0=[0]+rend_times
poi1=[0]+rend_times
poi2=[0]+rend_times
poi3=[0]+rend_times

vla_s=[renderer(init_dur/2**(tempo_0(poi0[i],1,1)+1),init_dur/2**(tempo_0(poi0[i+1],1,1)+1),tot*(poi0[i+1]-poi0[i])) for i in range(len(poi0)-1)]
z_vla=[i for i in itertools.chain.from_iterable(vla_s)]

vln_s=[renderer(init_dur/2**(tempo_1(poi1[i],1,1)+1),init_dur/2**(tempo_1(poi1[i+1],1,1)+1),tot*(poi1[i+1]-poi1[i])) for i in range(len(poi1)-1)]
z_vln=[i for i in itertools.chain.from_iterable(vln_s)]

cl_s=[renderer(init_dur/2**(tempo_2(poi2[i],1,1)+1),init_dur/2**(tempo_2(poi2[i+1],1,1)+1),tot*(poi2[i+1]-poi2[i])) for i in range(len(poi2)-1)]
z_cl=[i for i in itertools.chain.from_iterable(cl_s)]

fl_s=[renderer(init_dur/2**(tempo_3(poi3[i],1,1)+1),init_dur/2**(tempo_3(poi3[i+1],1,1)+1),tot*(poi3[i+1]-poi3[i])) for i in range(len(poi3)-1)]
z_fl=[i for i in itertools.chain.from_iterable(fl_s)]



durs=[0.5*(1/6)**(random.random_sample()) for i in range(9)]
durs.sort()
# durs=[1/16,1/13,1/11,1/9,1/7,1/5,1/4,1/3,1/2]
durs=[3*i for i in durs]

def gridder(grid_len):
    count=0
    while count< grid_len:
        count=0
        grid = [random.random_sample() for i in range(9)]
        grid.sort()
        grid=[0]+grid
        grid.append(1)
        for i in range(len(grid)-1):
            if grid[i+1]-grid[i]>0.05:
                count+=1
        if count==grid_len:
            return grid


grid=gridder(10)

durs_fl=[[grid[0],durs[7]*2/6],[grid[2],durs[2]],[grid[3],durs[0]],[grid[4],durs[2]],[grid[7],durs[3]],[grid[10],durs[8]*2/6]]
durs_cl=[[grid[0],durs[7]*2/5],[grid[1],durs[4]],[grid[2],durs[2]],[grid[3],durs[5]],[grid[4],durs[2]],[grid[5],durs[4]],[grid[7],durs[3]],[grid[9],durs[4]],[grid[10],durs[8]*2/5]]
durs_vln=[[grid[0],durs[7]/2],[grid[1],durs[4]],[grid[3],durs[5]],[grid[5],durs[4]],[grid[6],durs[6]],[grid[7],durs[3]],[grid[8],durs[6]],[grid[9],durs[4]],[grid[10],durs[8]/2]]
durs_vla=[[grid[0],durs[7]],[grid[3],durs[5]],[grid[6],durs[6]],[grid[7],durs[8]],[grid[8],durs[6]],[grid[10],durs[8]]]




# fl1=[renderer(durs_fl[i][1],durs_fl[i+1][1],(durs_fl[i+1][0]-durs_fl[i][0])*tot) for i in range(len(durs_fl)-1)]
# z_fl=[i for i in itertools.chain.from_iterable(fl1)]

# cl1=[renderer(durs_cl[i][1],durs_cl[i+1][1],(durs_cl[i+1][0]-durs_cl[i][0])*tot) for i in range(len(durs_cl)-1)]
# z_cl=[i for i in itertools.chain.from_iterable(cl1)]
#
# vln1=[renderer(durs_vln[i][1],durs_vln[i+1][1],(durs_vln[i+1][0]-durs_vln[i][0])*tot) for i in range(len(durs_vln)-1)]
# z_vln=[i for i in itertools.chain.from_iterable(vln1)]
#
# vla1=[renderer(durs_vla[i][1],durs_vla[i+1][1],(durs_vla[i+1][0]-durs_vla[i][0])*tot) for i in range(len(durs_vla)-1)]
# z_vla=[i for i in itertools.chain.from_iterable(vla1)]
#
# z_fl=renderer(3/6.5,3/6.5,tot)
# z_cl=renderer(3/5.5,3/5.5,tot)
# z_vln=renderer(3/4.5,3/4.5,tot)
# z_vla=renderer(3/3.5,3/3.5,tot)

env_fl=([(0,13),(1,13)],[(0,24),(1,24)])
env_cl=([(0,14),(1,14)],[(0,25),(1,25)])
env_vln=([(0,15),(1,15)],[(0,26),(1,26)])
env_vla=([(0,4),(1,4)],[(0,15),(1,15)])
#
# env_fl=([(grid[0],13),(grid[1],13),(grid[2],7),(grid[3],13),(grid[10],13)],\
#     [(grid[0],24),(grid[1],24),(grid[2],19),(grid[3],24),(grid[4],19),(grid[5],24),(grid[6],24),(grid[7],17),(grid[8],24),(grid[10],24)])
# # env_fl=([(0,25),(0.25,25),(0.5,25),(1,25)],[(0,36),(0.25,36),(0.5,36),(1,36)])
#
# env_cl=([(grid[0],14),(grid[1],14),(grid[2],19),(grid[3],15),(grid[4],19),(grid[5],14),(grid[6],14),(grid[7],17),(grid[8],14),(grid[10],14)],\
#     [(grid[0],25),(grid[1],20),(grid[2],25),(grid[3],19),(grid[4],25),(grid[5],20),(grid[6],25),(grid[7],21),(grid[8],25),(grid[9],20),(grid[10],25)])
#
# env_vln=([(grid[0],15),(grid[1],20),(grid[2],15),(grid[3],19),(grid[4],15),(grid[5],20),(grid[6],15),(grid[7],21),(grid[8],15),(grid[9],20),(grid[10],15)],\
#     [(grid[0],26),(grid[2],26),(grid[3],23),(grid[4],26),(grid[5],26),(grid[6],21),(grid[7],25),(grid[8],21),(grid[9],26),(grid[10],26)])
#
# env_vla=([(grid[0],4),(grid[2],4),(grid[3],11),(grid[4],4),(grid[5],4),(grid[6],9),(grid[7],4),(grid[8],9),(grid[9],4),(grid[10],4)],\
#     [(grid[0],15),(grid[6],15),(grid[7],21),(grid[8],15),(grid[10],15)])


r_env_fl=[(0,0),(1,.3)]
r_env_cl=[(0,0),(1,.3)]
r_env_vln=[(0,0),(1,.3)]
r_env_vla=[(0,0),(1,.3)]


# q_fl=concater_rester(cloner(z_fl,env_fl,4,[7,12],800,2,'fl'),36,z_fl,r_env_fl)[:len(z_fl)]
# q_cl=concater_rester(cloner(z_cl,env_cl,4,[7,12],600,2,'cl'),36,z_cl,r_env_cl)[:len(z_cl)]
# q_vln=concater_rester(cloner(z_vln,env_vln,4,[7,12],600,2,'vln'),36,z_vln,r_env_vln)[:len(z_vln)]
q_vla=concater_rester(cloner(z_vla,env_vla,4,[7,12],600,2,'vla'),36,z_vla,r_env_vla)[:len(z_vla)]

# midier(z_fl,q_fl,74,'flute','not rests')
# midier(z_cl,q_cl,72,'clarinet','not rests')
# midier(z_vln,q_vln,74,'violin','not rests')
midier(z_vla,q_vla,72,'viola','not rests')
#
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