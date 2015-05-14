Tasks:

1. Generate a random tree

    - control the overlap between adjacent siblings
    - randomize data
    - fix fanout for interior nodes, and larger fanout for leaf-level, 
      and control the depth of the tree

2. Compute the bloom filters at *each* node

3. Run search query

Evaluation:

    Parameters:

    - tree size
        - fan-out
        - height
        - number of leafs

    - overlap
    - capacity of BF
    - density of BF

    - space
    - query time
    - index time
        - incremental update
        - initial index time

    Experiments:

    - hist(bfTime, naiveTime, :fixed others)
    - plot(treeSize, bfTime, naiveTime, :fix others)
    - plot(density, bfTime)
    - plot(overlap, bfTime)
    - plot(treeSize, incrementalIndex)
    - plot(treeSize, indexTime)
