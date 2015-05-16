import datagen
import index
import query
import time
from matplotlib.pylab import *
import json

"""
Vary the density and observe the performance, and storage.
"""

name = "exp3"

N = 100000

def average(coll, key):
    total = sum(x.get(key, 0) for x in coll)
    return float(total) / len(coll)

def oneRound(option, tree=None):
    obs = []
    density = option['density']

    if tree is None:
        tree = datagen.buildTree(option, 0, N)
        index.buildIndex(tree, dict(capacity=N, error_rate=0.1))

    index.sparsify(tree, density)
    n = datagen.treeSize(tree)
    n_idx = datagen.bfSize(tree)

    print "oneRound: ", density, n_idx, n

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
            n=n,
            n_idx=n_idx,
            density=density)

opt = dict(
        fanOut=7,
        leafFanOut=5,
        height=5,
        overlap=0.2,
        density=1.0)

tree = datagen.buildTree(opt, 0, N)
index.buildIndex(tree, dict(capacity=N, error_rate=0.1))

fast  = []
naive = []
obs   = []

for d in [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
    opt['density'] = d
    obs.append(oneRound(opt, tree))

import pprint
pprint.pprint(obs)

with open("%s.json" % name, "w") as f:
    print >>f, json.dumps(obs, indent=True);

print "All done"
