from maximally_smooth import smooth_curve_exact_durtot
import numpy as np
from numpy.random import choice


def next_note(pitchset,probs,alpha):
    if sum(probs) != 0:
        probs=[i**alpha for i in probs]
        probs=[i/sum(probs) for i in probs]
    else:
        probs=[1 for i in probs]
        probs=[i/sum(probs) for i in probs]
    q=choice(pitchset,1,p=probs).tolist()
    return q[0]

def note_stream(pitchset,probs,num,alpha):
    ns=[]
    count=0
    while count < num:
        z=next_note(pitchset,probs,alpha)
        ns.append(z)
        probs=[i+1 for i in probs]
        probs[pitchset.index(z)] = 0
        count += 1
    return [ns,probs]

#generate midi rendering of just rhythym
#set whole note = 60 bpm, so 128th notes = 1/128 s = 0.0078125

def renderer(dur1,dur2,durtot):
    a= smooth_curve_exact_durtot(dur1,dur2,durtot)
    b=[sum(a[:i+1]) for i in range(len(a))]
    b=[round(960*i) for i in b]
    c=[]
    for i in range(len(b)):
        if i == 0: c.append(b[i])
        else:
            c.append(b[i]-b[i-1])
    return c


def midier(z,q,instnum,inst,setting):
    from mido import MidiFile,MidiTrack, Message
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change',program=instnum, time=0))
    track.append(Message('control_change', control=7, value=100 ))

    if setting == 'rests':
        chain=0
        for i in range(len(z)):
            if q[i]=='r':
                chain += z[i]
                if i==len(z)-1:
                    track.append(Message('note_on',note=60,velocity=0,time=chain))
            else:
                track.append(Message('note_on', note=q[i], velocity=63, time=chain))
                track.append(Message('note_on', note=q[i], velocity=0, time=z[i]))
                chain=0
        mid.save(''.join([inst,'.mid']))
    else:
        chain=0
        for i in range(len(z)):
            if q[i]=='r':
                chain += z[i]
                if i==len(z)-1:
                    track.append(Message('note_on',note=track[-1].__dict__['note'],velocity=0,time=chain))
            else:
                if i == 0:
                    track.append(Message('note_on', note = q[i], velocity=63, time = 0))
                    chain=z[i]
                else:
                    track.append(Message('note_on', note=track[-1].__dict__['note'],velocity=0,time=chain))
                    track.append(Message('note_on', note=q[i],velocity=63,time=0))
                    chain=z[i]
                if i == len(z)-1:
                    track.append(Message('note_on', note=track[-1].__dict__['note'],velocity=0,time=chain))
        mid.save(''.join([inst,'.mid']))

def ranger(z,min_array,max_array,want_round):
    import math
    for i in range(len(min_array)-1):
        if z >= min_array[i][0] and z < min_array[i+1][0]:
            min_ = min_array[i][1]+(z-min_array[i][0])*((min_array[i+1][1]-min_array[i][1])/(min_array[i+1][0]-min_array[i][0]))
    if z== min_array[-1][0]:min_ = min_array[-1][1]

    for i in range(len(max_array)-1):
        if z >= max_array[i][0] and z < max_array[i+1][0]:
            max_ = max_array[i][1]+(z-max_array[i][0])*((max_array[i+1][1]-max_array[i][1])/(max_array[i+1][0]-max_array[i][0]))
    if z >= max_array[-1][0]:max_=max_array[-1][1]
    if want_round == 'yes':
        return (math.ceil(min_),math.floor(max_))
    else: return (min_,max_)


##array looks like [(0,0),(0.5,4),(1,8)]

def rester(z,array):
    import math
    for i in range(len(array)-1):
        if z >= array[i][0] and z < array[i+1][0]:
            rest_=array[i][1]+(z-array[i][0])*((array[i+1][1]-array[i][1])/(array[i+1][0]-array[i][0]))
    if z==array[-1][0]: rest_=array[-1][1]
    return rest_

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
    while sum(klang_nums) < len(z_):
        x=sum(klang_nums)/len(z_)
        min_=math.floor(k_range_min(x,2,3,2))
        max_=math.ceil(k_range_max(x,2,3,2))
        set=[i for i in range(min_,max_)]
        klang_nums.append(next_note([i for i in set],[probs[i] for i in set],3))
        probs=[i+1 for i in probs]
        probs[klang_nums[-1]] = 0
    return klang_nums