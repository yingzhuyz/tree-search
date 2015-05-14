import random

nodeIdCounter = 0
class Node(object):
    def __init__(self, children=None, data=None):
        global nodeIdCounter
        self.children = children if children else []
        self.data = data
        self.id = nodeIdCounter
        self.bf = None
        self.useBF = True
        nodeIdCounter += 1

def buildTree(parameter, lower, upper, height=0):
    """requires a parameter describing the tree to built.
    Returns the root node of the tree.
    """

    if height == parameter['height']:
        data = (lower, upper)
        return Node(data=data)

    k = parameter['leafFanOut'] if height == parameter['height'] - 1  else parameter['fanOut']
    x = parameter['overlap']
    N = upper - lower
    if N < 0:
        raise Exception("Not enough data range: encountered negative count.")

    # build the data ranges for each child
    def start(i):
        return (i * N/k + lower)
    def end(i):
        return (i+1+x) * N/k + lower

    node = Node()
    if parameter.get('max') and node.id > parameter.get('max'):
        node.children = []
    else:
        dataRanges = [(start(i), end(i)) for i in range(k)]
        node.children = [buildTree(parameter, r[0], r[1], height+1) for r in dataRanges]
    
    return node

def printTree(node, indent=None):
    "Prints a tree nicely"
    indent = indent or ""

    id = "%.5d" % node.id
    data = repr(node.data) if node.data else "(No data)"
    filter = "(Bits: %d / Count: %d)" % (
            node.bf.num_bits,
            node.bf.bitarray.count()) if node.bf is not None else "(No filter)"

    print indent, id, data, filter

    if node.children:
        for c in node.children:
            printTree(c, indent=indent + "| ")

def treeSize(node):
    if len(node.children) == 0:
        return 1
    else:
        return sum(treeSize(c) for c in node.children) + 1
