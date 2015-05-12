import datagen

def lookfor(node, point, result):
    if 'visited' not in result:
        result['visited'] = 0
    if 'found' not in result:
        result['found'] = []

    result['visited'] += 1

    if node.data:
        if node.data[0] <= point <= node.data[1]:
            result['found'].append(node)
            return

    for c in node.children:
        lookfor(c, point, result)

def fastLookfor(node, point, result):
    if 'visited' not in result:
        result['visited'] = 0
    if 'found' not in result:
        result['found'] = []

    result['visited'] += 1

    if node.useBF:
        if point in node.bf:
            if node.data:
                result['found'].append(node)
            else:
                for c in node.children:
                    fastLookfor(c, point, result)
    else:
        # no bf enabled, revert back to slow search
        if node.data:
            if node.data[0] <= point <= node.data[1]:
                result['found'].append(node)
        else:
            for c in node.children:
                fastLookfor(c, point, result)
