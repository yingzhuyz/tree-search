from matplotlib.pylab import *
import json

obs = json.load(open('exp1.json'))

x = [u['n'] for u in obs]
t_fast = [u['t_fast'] for u in obs]
t_naive = [u['t_naive'] for u in obs]
v_fast = [u['v_fast'] for u in obs]
v_naive = [u['v_naive'] for u in obs]

print x
print t_fast
print t_naive

figure(1)
plot(x, t_fast, '-*', x, t_naive, '-o')
show(1)

figure(2)
plot(x, v_fast, x, v_naive, '-o')
show(2)
