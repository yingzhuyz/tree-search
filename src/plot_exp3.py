from matplotlib.pylab import *
import json

obs = json.load(open('exp3.json'))

x       = [u['density'] for u in obs]
t_fast  = [u['t_fast'] * 1000 for u in obs]
t_naive = [u['t_naive'] * 1000 for u in obs]
v_fast  = [u['v_fast'] for u in obs]
v_naive = [u['v_naive'] for u in obs]

figure(1)
plot(x, t_fast, '-o', x, t_naive, '-x', ms=8)
title('DENSITY VERSUS RUNTIME')
legend(['With Bloom filter', 'Naive'], loc="upper right")
xlabel('Density of nodes with index in tree')
ylabel('TIME (ms)')

savefig('density.pdf')
