import datagen
import index
import query
import time
import json

"""
Vary tree height, and observe the naive versus BF
"""

N = 100000
density = 1.0

def oneRound(option):
    pass


fast = []
naive = []

opt = dict(
        fanOut=3,
        leafFanOut=3,
        height=2,
        overlap=0.2)

obs = []
for height in reversed([2, 4, 6, 8, 10]):
    print "height = ", height

    opt['height'] = height
    tree = datagen.buildTree(opt, 0, N)
    index.buildIndex(tree, dict(capacity=N, error_rate=0.1))
    index.sparsify(tree, density)

    t_fast = []
    t_naive = []
    for q in range(0, N, N/100):
        result = {}
        start = time.time()
        query.fastLookfor(tree, q, result)
        t1 = time.time() - start

        result = {}
        start = time.time()
        query.lookfor(tree, q, result)
        t2 = time.time() - start

        t_fast.append(t1)
        t_naive.append(t2)

    # save the result
    obs.append(dict(
        height=height,
        t_fast=sum(t_fast)/len(t_fast),
        t_naive=sum(t_naive)/len(t_naive)))

with open('exp4.json', 'w') as f:
    json.dump(obs, f)



