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


# Thompsons Construction.
class State:
    """A state and its arrows in Thompsons construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrows labels, arrows is a list of states 
           to point to, accept is a boolean if its an accept state."""
        self.label = label
        self.arrows = arrows
        self.accept = accept

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

def compileNFA(infix):
    """Compile NFA function -> Construct an NFA from the infix expression
        and return the NFA."""
    # Convert infix param to postfix.
    # Create a stack for NFAs.
    postfix, stack = shunt(infix), []
    # Loop through the postfix r.e left to right.
    for c in postfix:
        # Concatenation. Match single characters
        if c == '.': 
            # Do stuff
        # Or operator. Expressions A or B
        elif c == '|': 
            # Do stuff
        # Kleene star. Concatenate zero or more strings
        elif c == '*': 
            # Do stuff
        else:
            # Create an NFA for non-specail characters in c.
            # create start and end state.
            end, start = State(None, [], True), State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Append the NFA to the NFA stack.
            stack.append(NFA(start,end))
        # The NFA stack should only have one NFA on the stack.
        if len(stack) != 1:
            return None
        else:
            return stack[0]
