# Make parse tree & traverse with non recursive function
class Node:
    def __init__(self, key=-1):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.left = self.tail
        self.head.right = self.tail
        self.tail.left = self.tail
        self.tail.right = self.tail

    @staticmethod
    def is_operator(op):
        if op == '+' or op == '-' or op == '*' or op == '/':
            return True
        else:
            return False

    def make_parse_tree(self, equation):
        stack = []
        while len(equation) != 0:
            while equation[0] == ' ':
                del equation[0]
            node = Node()
            node.key = equation[0]
            node.left = self.tail
            node.right = self.tail
            if self.is_operator(equation[0]):
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
            del equation[0]
        self.head.right = stack.pop()

    @staticmethod
    def visit(n):
        print(n.key, end=" ")

    def preorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.visit(node)
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    def preorder_traverse_nr(self, n):
        stack = []
        node = n
        stack.append(node)
        while len(stack) != 0:
            node = stack.pop()
            if node != self.tail:
                self.visit(node)
                stack.append(node.right)
                stack.append(node.left)

    def inorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.inorder_traverse(node.left)
            self.visit(node)
            self.inorder_traverse(node.right)

    def inorder_traverse_nr(self, n):
        stack = []
        node = n
        done = 0
        while done == 0:
            while node != self.tail:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                self.visit(node)
                node = node.right
            else:
                done = 1

    def postorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            self.visit(node)

    def postorder_traverse_nr(self, n):
        stack = []
        node = n
        done = 0
        while done == 0:
            while node != self.tail:
                stack.append(node)
                node = node.left
            while len(stack) != 0:
                t = node
                node = stack.pop()
                if node.right != self.tail:
                    if node.right == t:
                        self.visit(node)
                    else:
                        stack.append(node)
                        node = node.right
                        break
                else:
                    self.visit(node)
            if len(stack) == 0:
                done = 1


# main() function
if __name__ == "__main__":
    # Change infix notation to postfix notation
    source = ['A', 'B', '+', 'C', 'D', '-', '*', 'E', '/', 'F', 'G', '*', '+']

    tree = Tree()
    tree.make_parse_tree(source)

    print("[Preorder]")
    print("    Recursive : ", end=' ')
    tree.preorder_traverse(tree.head.right)
    print()
    print("Non Recursive : ", end=' ')
    tree.preorder_traverse_nr(tree.head.right)
    print()

    print("[Inorder]")
    print("    Recursive : ", end=' ')
    tree.inorder_traverse(tree.head.right)
    print()
    print("Non Recursive : ", end=' ')
    tree.inorder_traverse_nr(tree.head.right)
    print()

    print("[Postorder]")
    print("    Recursive : ", end=' ')
    tree.postorder_traverse(tree.head.right)
    print()
    print("Non Recursive : ", end=' ')
    tree.postorder_traverse_nr(tree.head.right)
    print()