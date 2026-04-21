from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    result = []
    queue = deque([node])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)
    return result    
