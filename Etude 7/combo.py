from maximally_smooth import smooth_curve_exact_durtot as optcurve


#generate midi rendering of just rhythym
#set whole note = 60 bpm, so 128th notes = 1/128 s = 0.0078125

def renderer(dur1,dur2,durtot):
    a= optcurve(dur1,dur2,durtot)
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
                else:
                    track.append(Message('note_on', note=track[-1].__dict__['note'],velocity=0,time=chain))
                    track.append(Message('note_on', note=q[i],velocity=63,time=0))
                    chain=z[i]
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

