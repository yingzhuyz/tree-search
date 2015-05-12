import pybloom
import datagen
import random

def buildIndex(node, option):
    """builds a Bloom filter on each interior node under the tree
    """

    node.bf = pybloom.BloomFilter(option['capacity'], option['error_rate'])

    if node.data:
        lower = round(node.data[0])
        upper = round(node.data[1])

        for x in range(int(lower), int(upper)):
            node.bf.add(x)

    if node.children:
        for child in node.children:
            node.bf = node.bf.union(buildIndex(child, option))

    return node.bf

def sparsify(node, density=0.5):
    "density given is the percentage of nodes with bf"
    if random.random() >= density:
        # remove the bf
        node.useBF = False
    else:
        node.useBF = True

    for c in node.children:
        sparsify(c, density)


