import datagen
import index
import query
import time
import json

name = "hist"

N = 100000
option = dict(fanOut=3, leafFanOut=5, height=8, overlap=0.2)
tree = datagen.buildTree(option, 0, N)

print "Building the tree index"
index.buildIndex(tree, dict(capacity=N, error_rate=0.1))

def oneRound(density, lookfor, rng):
    print "density = %.2f" % density
    obs = []
    index.sparsify(tree, density)
    print "range:", rng

    for pt in range(rng[0], rng[1], (rng[1]-rng[0])/100):
        start = time.time()
        result = dict()
        lookfor(tree, pt, result)
        dur = time.time() - start
        obs.append(dict(dur = dur, visited = result['visited']))
    return obs

# fastLookfor versus lookfor

fastObsIn = oneRound(1.0, query.fastLookfor, (0, N))
fastObsOut = oneRound(1.0, query.fastLookfor, (N+1, 2*N+1))
obs     = oneRound(1.0, query.lookfor, (0, N))

with open('exp2.json', 'w') as f:
    json.dump(
        dict(fastIn=fastObsIn, fastOut=fastObsOut, naive=obs),
        f,
        indent=True)

print "All done"

# Plots

#fastDur = [x["dur"] * 1000 for x in fastObs]
#dur     = [x["dur"] * 1000 for x in obs]

#figure(1)
#fig = hist(fastDur + dur, bins=100)
#title("Distribution of query performance")
#xlabel("Query time (ms)")
#savefig("%s_1.png" % name)

# figure(2)
# hist(dur)
# savefig("%s_2.png" % name)

