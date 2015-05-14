import datagen
import index
import query
import time
from matplotlib.pylab import *

name = "hist"

N = 100000
option = dict(fanOut=3, leafFanOut=5, height=8, overlap=0.2)
tree = datagen.buildTree(option, 0, N)

print "Building the tree index"
index.buildIndex(tree, dict(capacity=N, error_rate=0.1))

def oneRound(density, lookfor):
    print "density = %.2f" % density
    obs = []
    index.sparsify(tree, density)
    for pt in range(0, N, N/100):
        start = time.time()
        result = dict()
        lookfor(tree, pt, result)
        dur = time.time() - start
        obs.append(dict(dur = dur, visited = result['visited']))
    return obs

# fastLookfor versus lookfor

fastObs = oneRound(1.0, query.fastLookfor)
obs     = oneRound(1.0, query.lookfor)

# Plots

fastDur = [x["dur"] for x in fastObs]
dur     = [x["dur"] for x in obs]

figure(1)
hist(fastDur + dur, bins=100)
savefig("%s_1.png" % name)

figure(2)
hist(dur)
savefig("%s_2.png" % name)

