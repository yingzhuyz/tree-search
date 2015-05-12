import datagen
import index
import query
import time

N = 10000
p = dict(fanOut=3, leafFanOut=5, height=8, overlap=0.2)
tree = datagen.buildTree(p, 0, N)
index.buildIndex(tree, dict(capacity=2*N, error_rate=0.1))
index.sparsify(tree, 0.5)
datagen.printTree(tree)

def report(tree, point, lookfor):
    print "=" * 20
    result = dict()
    start = time.time()
    lookfor(tree, point, result)
    duration = time.time() - start
    print "Found: %d matches in %.5f seconds visiting %d nodes." % (
            len(result['found']), duration, result['visited'])

    for n in result['found']:
        datagen.printTree(n)

point = 11096
report(tree, point, query.lookfor)
report(tree, point, query.fastLookfor)
