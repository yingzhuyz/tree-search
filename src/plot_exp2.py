from matplotlib.pylab import *
import json
import math
import random

data = json.load(open('exp2.json'))

t_fastin = [x['dur'] * 1000 for x in data['fastIn']]
t_fastout = [x['dur'] * 1000 for x in data['fastOut']]
t_naive = [x['dur'] * 1000 for x in data['naive']]

def mix(p_out):
    n = len(t_fastin)
    n_out = int(p_out * n)
    n_in = n - n_out
    return t_fastin[:n_in] + t_fastout[:n_out]

def average(t):
    return sum(t) / len(t)

figure(1)
hist(mix(0), bins=5)
hist(t_naive, alpha=.5)
title('Query time distributions: Bloom filter vs Naive')
xlabel('Query time (ms)')
legend(['With Bloom filter', 'Naive'])
savefig('hist.pdf')


figure(2)
p_out = [0.1 * i for i in range(11)]
T = [average(mix(p)) for p in p_out]
T_naive = [average(t_naive) for p in p_out]
plot(p_out, T, '-o')
title('Effect of query misses on performance')
xlabel('Ratio of miss-queries in workload')
ylabel('Query time (ms)')
savefig('miss-query.pdf')

