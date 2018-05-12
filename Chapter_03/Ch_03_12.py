# Evaluate expression
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
        is_num = 0
        for i in source:
            # To handle not only single digit but also more than 10
            if '0' <= i <= '9':
                if is_num == 1:
                    dst[-1] = i
                else:
                    dst.append(i)
                dst.append(' ')
                is_num = 1
                continue

            is_num = 0

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

        while len(stack) != 0:
            t = stack.pop()
            dst.append(t)

        return(dst)

    def do_calc(self, src):
        stack = []
        i = 0
        while i < len(src):
            ch = src[i]
            if '0' <= ch <= '9':
                t = 0
                while True:
                    t = t * 10 + int(ch)
                    if '0' <= src[i+1] <= '9':
                        i += 1
                        ch = src[i]
                    else:
                        break
                stack.append(t)
            elif ch == '+':
                t = stack.pop() + stack.pop()
                stack.append(t)
            elif ch == '*':
                t = stack.pop() * stack.pop()
                stack.append(t)
            elif ch == '-':
                t = stack.pop()
                t = stack.pop() - t
                stack.append(t)
            elif ch == '/':
                t = stack.pop()
                t = stack.pop() / t
                stack.append(t)
            i += 1

        # Return results which is in stack
        return (stack.pop())


# main() function
if __name__ == "__main__":
    source = input("Please input -> ")
    postfix = Postfix()
    # Change infix notation to postfix notation
    contents = postfix.do_postfix(source)
    # Evaluate expression
    results = postfix.do_calc(contents)
    # Print results
    print(results)
