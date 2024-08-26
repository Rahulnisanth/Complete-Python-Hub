# POST ORDER TRAVERSAL IN N'ARY TREE :
def postorder(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        for child in node.children:
            stack.append(child)
    return result[::-1]