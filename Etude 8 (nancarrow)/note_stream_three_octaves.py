from numpy.random import choice,random_integers
import numpy as np
import itertools
from combo import *



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


def cloner(z_,env,alpha,range_,num_klangs,bw):
    pitchset=[i for i in range(32)]
    stream=[]
    probs=[1 for i in range(36)]
    count=0
    klang_lens=note_stream([i for i in range(range_[0],range_[1])],[1 for i in range(range_[0],range_[1])],num_klangs,4)[0]
    while count < num_klangs:
        if len(stream) == 0:
            ranged=ranger(sum(z_[:len(stream)])/sum(z_),env[0],env[1],'yes')
            temp_pitchset=pitchset[ranged[0]:ranged[1]]
            init_stream=note_stream(temp_pitchset,[1 for i in range(len(temp_pitchset))],klang_lens[count],alpha)
            stream.append(init_stream[0])
            probs = [i+len(init_stream[0]) for i in probs]
            probs[ranged[0]:ranged[1]] = init_stream[1]
            for i in probs[ranged[0]:ranged[1]]:
                if i < 12:
                    probs[i+12]=probs[i]
                    probs[i+24]=probs[i]
                elif i < 24:
                    probs[i-12]=probs[i]
                    probs[i+12]=probs[i]
                else:
                    probs[i-24]=probs[i]
                    probs[i-12]=probs[i]
            count += 1
        else:
            c=klang_lens[count]
            merged_stream=[i for i in itertools.chain.from_iterable(stream)]
            ranged = ranger(sum(z_[:len(merged_stream)]) / sum(z_), env[0], env[1],'yes')
            temp_pitchset = pitchset[ranged[0]:ranged[1]]
            if c > len(merged_stream): c = len(merged_stream)
            substream=merged_stream[-c:]
            substream=[substream[i]-substream[0] for i in range(len(substream))]
            if max(substream) - min(substream) >= len(temp_pitchset):
                for i in range(len(substream)):
                    if substream[i] - substream[0] >= len(temp_pitchset):
                        substream[i] = np.random.randint(len(temp_pitchset)) + min(substream)
            for i in range(len(substream)):
                if i == 0:
                    f=abs(min(substream))
                    g=len(temp_pitchset)-max(substream)
                    if g<=f:
                        z=next_note(temp_pitchset,probs[ranged[0]:ranged[1]],alpha)
                    else:
                        z=next_note(temp_pitchset[f:g],probs[ranged[0]+f:ranged[0]+g],alpha)
                    stre = [z]
                    probs=[j+1 for j in probs]
                    probs[pitchset.index(z)] = 0
                    if pitchset.index(z)<12:
                        probs[pitchset.index(z)+12] = 0
                        probs[pitchset.index(z) + 24] = 0
                    elif pitchset.index(z)<24:
                        probs[pitchset.index(z)-12] = 0
                        probs[pitchset.index(z)+12] = 0
                    else:
                        probs[pitchset.index(z) - 24] = 0
                        probs[pitchset.index(z) - 12] = 0
                else:
                    a=temp_pitchset.index(z)+substream[i]-bw
                    b=temp_pitchset.index(z)+substream[i]+bw
                    if a < 0: a=0
                    if b<0: b=0
                    if b > len(temp_pitchset): b= len(temp_pitchset)
                    if b-a >= len(temp_pitchset):
                        y = next_note(temp_pitchset, probs[ranged[0]:ranged[1]], alpha)
                    elif a==b:
                        y = next_note(temp_pitchset, probs[ranged[0]:ranged[1]], alpha)
                    else:
                        y=next_note(temp_pitchset[a:b],probs[ranged[0]+a:ranged[0]+b], alpha)
                    stre += [y]
                    probs=[j+1 for j in probs]
                    probs[pitchset.index(y)] = 0
                    if pitchset.index(y) < 12:
                        probs[pitchset.index(y)+12]=0
                        probs[pitchset.index(y)+24] = 0
                    elif pitchset.index(y) < 24:
                        probs[pitchset.index(y)-12]=0
                        probs[pitchset.index(y)+12]=0
                    else:
                        probs[pitchset.index(y) - 24] = 0
                        probs[pitchset.index(y) - 12] = 0
            stream.append(stre)
            count += 1
    return [stream,probs]


def concater_rester(stream,add,rest_nums):
    chain=[]
    for i in stream[0]:
        for j in range(len(i)):
            if j >= len(i)-rest_nums:
                chain.append('r')
            chain.append(i[j]+add)
    return chain



