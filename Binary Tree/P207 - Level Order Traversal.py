def getLevelOrder(root):
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

    return res
