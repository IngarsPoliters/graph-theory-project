# Graph Theory Project 
# Ingars Politers - G00374677

# Shunting Yard Algorithm @ https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def shunt(infix):
    """Shunt Function - Convert Infix expression to Postfix"""
    # postfix - The eventual output.
    # stack - The shunting yard operator stack.
    postfix, stack = ""
    # The operator precedence.
    precedence = {'*': 100, '.': 90, '|': 80}
    # Loop through thei input a character at a time.
    for c in infix:
        # c is an operator
        if c in {'*','.','|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and precedence[stack[-1]] >= precedence[c]:
                # Append the operator at top of stack to the output.
                # Remove operator from stack.
                postfix, stack = postfix + stack[-1], stack[:-1] 
            # Push c to stack.
            stack += c
        elif c == '(':
            # Push c to stack.
            stack += c
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of stack to output.
                # Remove operator from stack.
                postfix, stack = postfix + stack[-1], stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
        else:
            # Push it to the output.
            postfix += c
    # Empty the operator stack.
    while len(stack) != 0:
        # Append operator at top of stack to output.
        # Remove operator from stack.
        postfix, stack = postfix + stack[-1], stack[:-1]
    # Return the postfix converted from infix
    return postfix