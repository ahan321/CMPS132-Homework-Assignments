@property
def printInorder(self):
    self._inorderHelper(self.root)

def _inorderHelper(self, node):
    if node is not None:
       self._inorderHelper(node.left)
       print(node.value, end=' : ')
       self._inorderHelper(node.right)

