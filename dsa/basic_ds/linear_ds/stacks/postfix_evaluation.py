from stack import Stack2


def postfix_eval(postfix_expr):
    operand_stack = Stack2()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in [str(i) for i in range(100000)]:
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
