# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    l_nodes = pre_order(node.left)
    r_nodes = pre_order(node.right)
    return [node.data] + l_nodes + r_nodes

# In-order traversal
def in_order(node):
    if not node:
        return []
    l_nodes = in_order(node.left)
    r_nodes = in_order(node.right)
    return l_nodes + [node.data] + r_nodes

# Post-order traversal
def post_order(node):
    if not node:
        return []
    l_nodes = post_order(node.left)
    r_nodes = post_order(node.right)
    return l_nodes + r_nodes + [node.data]
    