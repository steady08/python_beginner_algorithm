class Postfix:
    def __init__(self):
        pass

    def is_operator(self, ch):
        if ch == '*' or ch == '/' or ch == '+' or ch == '-':
            return True
        else:
            return False

    def precedence(self, op):
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 3

    def do_postfix(self, source):
        dst = []
        stack = []
        for i in source:
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
            elif '0' <= i <= '9':
                dst.append(i)

        while len(stack) != 0:
            t = stack.pop()
            dst.append(t)

        return(dst)

#main() function
if __name__ == "__main__":
    source = input("Please input -> ")
    postfix = Postfix()
    contents = postfix.do_postfix(source)
    print(contents)
