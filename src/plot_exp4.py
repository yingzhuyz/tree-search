from matplotlib.pylab import *
import json
import math

obs = json.load(open('exp4.json'))

x       = [u['height'] for u in obs]
t_fast  = [math.log10(u['t_fast'] * 1000) for u in obs]
t_naive = [math.log10(u['t_naive'] * 1000) for u in obs]

figure(1)
plot(x, t_fast, '-x', x, t_naive, '-o', ms=8.0)
title('LOG plot of query time versus tree height')
xlabel('Height of tree')
ylabel('TIME (log10 ms)')
legend(['With Bloom filter index', 'Naive'], loc = "upper left")

savefig('tree-height.pdf')
