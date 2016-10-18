import sys
sys.path.append('../')

##### Class definitions #####
class Tree():
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.__str__()

class TreeNode():
    def __init__(self, data=None, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        children = self.children
        tree_string = "\t"*level + self.data + "\n"
        for child in children:
            tree_string += child.__str__(level+1)
        return tree_string

##### Testing #####
def tree_test():
    print("=====Tree Testing=====")
    root = TreeNode("a")
    root.children = [TreeNode("b"), TreeNode("c")]
    root.children[0].children = [TreeNode("d"), TreeNode("e")]
    root.children[1].children = [TreeNode("f"), TreeNode("g")]
    tree = Tree(root)
    print(tree)