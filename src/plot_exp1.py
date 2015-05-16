from matplotlib.pylab import *
import json
import math

obs = json.load(open('exp1.json'))

x       = [u['n'] / 1000.0 for u in obs]
t_fast  = [math.log10(u['t_fast']  * 1000) for u in obs]
t_naive = [math.log10(u['t_naive'] * 1000) for u in obs]
v_fast  = [u['v_fast'] for u in obs]
v_naive = [u['v_naive'] for u in obs]

figure(1)
plot(x, t_fast, '-o', x, t_naive, '-x', ms=8)
title('LOG plot of query time versus tree size')
xlabel('Number of nodes (thousands)')
ylabel('Query time (log10 ms)')
legend(['With Bloom filter', 'Naive'], loc='upper left')

savefig('tree-size.pdf')

# figure(2)
# plot(x, v_fast, x, v_naive, '-o')
# show(2)
