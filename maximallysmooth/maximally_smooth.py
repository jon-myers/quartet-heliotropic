from math import sin, pi

# given start duration, end duration, number of beats, generates a smooth curve

def smooth_curve(dur1,dur2,bts):
    x=(dur2/dur1)**(1/(bts-1))
    set=[dur1*(x**i) for i in range(bts)]
    return set

# given start dur, end dur, and total duration, generates smooth curve with as close as possible approximation of desired total duration

def smooth_curve_approximate_durtot(dur1,dur2,durtot):
    duravg=(dur1+dur2)/2
    btguess=round(durtot/duravg)
    btrange=[i for i in range(round(btguess/2),round(btguess*2))]
    q=sorted([[abs(durtot-sum(smooth_curve(dur1,dur2,i))),smooth_curve(dur1,dur2,i)] for i in btrange])
    return q[0][1]

# given array and exact total duration, fudges  array to fit it to exact desired time
# fudging uses cosine function to shift items toward the middle of the array more than on the ends, so start dur and end dur aren't effected
def shifter(array,idealdur):
    stepsize=(pi/(len(array)-1))
    shift=idealdur-sum(array)
    set=[array[i]*sin(i*stepsize) for i in range(len(array))]
    newset=[(shift/sum(set))*i for i in set]
    finset=[array[i] + newset[i] for i in range(len(array))]
    return finset

# given start dur, end dur, and total time, generates maximally smooth curve that exactly fits desired total duration
def smooth_curve_exact_durtot(dur1,dur2,durtot):
    set=smooth_curve_approximate_durtot(dur1,dur2,durtot)
    nset=shifter(set,durtot)
    return nset

# given start dur, end dur, total beats, and total duration, generates maximally smooth curve over given # of beats that exactly fits desired duration
# this one can be a bit wonky if the given parameters don't make sense

def smooth_curve_beats_exact_durtot(dur1,dur2,bts,durtot):
    set=smooth_curve(dur1,dur2,bts)
    nset=shifter(set,durtot)
    return nset

from matplotlib import pyplot as plt
