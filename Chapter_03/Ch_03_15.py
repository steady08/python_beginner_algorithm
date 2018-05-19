# Make parse tree & treaverse
import queue


# To change infix notation to postfix notation
class Postfix:
    def __init__(self):
        pass

    @staticmethod
    def is_operator(ch):
        if ch == '*' or ch == '/' or ch == '+' or ch == '-':
            return True
        else:
            return False

    @staticmethod
    def precedence(op):
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 3

    def do_postfix(self, src):
        dst = []
        stack = []
        for i in src:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    t = stack.pop()
                    dst.append(t)
                stack.pop()
            elif self.is_operator(i):
                while len(stack) != 0 and self.precedence(stack[-1]) >= self.precedence(i):
                    dst.append(stack.pop())
                stack.append(i)
            # Change only below line for this example
            elif 'A' <= i <= 'G':
                dst.append(i)

        while len(stack) != 0:
            t = stack.pop()
            dst.append(t)

        return dst


class Node:
    def __init__(self, key=-1):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.stack = []
        self.queue = queue.Queue()
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

    def is_legal(self, equation):
        num_of_operator = 0
        size = len(equation)
        step = 0
        while size != step:
            while equation[step] == ' ':
                step += 1
            if self.is_operator(equation[step]):
                num_of_operator -= 1
            else:
                num_of_operator += 1
            if num_of_operator < 1:
                break
            step += 1

        if num_of_operator == 1:
            return True
        else:
            return False

    def make_parse_tree(self, equation):
        while len(equation) != 0:
            while equation[0] == ' ':
                del equation[0]
            node = Node()
            node.key = equation[0]
            node.left = self.tail
            node.right = self.tail
            if self.is_operator(equation[0]):
                node.right = self.stack.pop()
                node.left = self.stack.pop()
            self.stack.append(node)
            del equation[0]
        self.head.right = self.stack.pop()

    @staticmethod
    def visit(n):
        print(n.key, end=" ")

    def preorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.visit(node)
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    def inorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.inorder_traverse(node.left)
            self.visit(node)
            self.inorder_traverse(node.right)

    def postorder_traverse(self, n):
        node = n
        if node != self.tail:
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            self.visit(node)

    def levelorder_traverse(self, n):
        node = n
        self.queue.put(node)
        while self.queue.qsize() != 0:
            node = self.queue.get()
            self.visit(node)
            if node.left != self.tail:
                self.queue.put(node.left)
            if node.right != self.tail:
                self.queue.put(node.right)


# main() function
if __name__ == "__main__":
    # Change infix notation to postfix notation
    source = "((((A+B)*(C-D))/E)+(F*G))"#input("Please input -> ")
    postfix = Postfix()
    contents = postfix.do_postfix(source)
    print(contents)
    #
    tree = Tree()
    if tree.is_legal(contents) is not True:
        print ("Expression is not legal")
    else:
        tree.make_parse_tree(contents)
        tree.preorder_traverse(tree.head.right)
        print()
        tree.inorder_traverse(tree.head.right)
        print()
        tree.postorder_traverse(tree.head.right)
        print()
        tree.levelorder_traverse(tree.head.right)
        print()