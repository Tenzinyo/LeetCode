def bst(root):
    # return [[]]
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        sublist = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                sublist.append(node.val)
                q.append(node.left)
                q.append(node.child)
        if sublist:
            res.append(sublist)
    return res