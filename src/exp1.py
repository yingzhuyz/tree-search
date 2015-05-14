import datagen
import index
import query
import time
from matplotlib.pylab import *
import json

"""
Vary tree size, and observe the naive versus BF
"""

name = "exp1"

N = 100000
density = 1.0

def average(coll, key):
    total = sum(x.get(key, 0) for x in coll)
    return float(total) / len(coll)

def oneRound(option):
    obs = []
    tree = datagen.buildTree(option, 0, N)
    n = datagen.treeSize(tree)
    index.buildIndex(tree, dict(capacity=N, error_rate=0.1))
    index.sparsify(tree, density)

    print "oneRound: ", n

    for q in range(0, N, N/100):
        result = dict()
        start = time.time()
        query.lookfor(tree, q, result)
        t1 = time.time() - start
        n1 = result['visited']

        result = dict()
        start = time.time()
        query.fastLookfor(tree, q, result)
        t2 = time.time() - start
        n2 = result['visited']

        obs.append(dict(
            t_naive=t1,
            v_naive=n1,
            t_fast=t2,
            v_fast=n2))


    return dict(
            t_naive=average(obs, "t_naive"),
            v_naive=average(obs, "v_naive"),
            t_fast=average(obs, "t_fast"),
            v_fast=average(obs, "v_fast"),
            n=n)

opt = dict(
        fanOut=7,
        leafFanOut=5,
        height=5,
        overlap=0.2)

fast = []
naive = []

obs = []
for x in [3, 4, 5, 6, 7, 8, 9, 10]:
    opt['leafFanOut'] = x
    obs.append(oneRound(opt))


import pprint
pprint.pprint(obs)

with open("%s.json" % name, "w") as f:
    print >>f, json.dumps(obs, indent=True);

print "All done"
