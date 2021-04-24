# Graph Theory Project 
# Ingars Politers - G00374677

# Shunting Yard Algorithm @ https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def shunt(infix):
    """Shunt Function - Convert Infix regular expression to Postfix"""
    # postfix - The eventual output.
    # stack - The shunting yard operator stack.
    postfix, stack = "", ""
    # The operator precedence.
    precedence = {'*': 100, '.': 90, '|': 80}
    # Loop through thei input a character at a time.
    for c in infix:
        # c is an operator
        if c in precedence:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and precedence[stack[-1]] >= precedence[c]:
                # Append the operator at top of stack to the output.
                # Remove operator from stack.
                postfix, stack = postfix + stack[-1], stack[:-1] 
            # Push c to stack.
            stack += c
            print(f'c = {c}  pofix1 ={postfix}  stack ={stack}')
        elif c == '(':
            # Push c to stack.
            stack += c
            print(f'c = {c}  pofix1 ={postfix} stack2 ={stack}')
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of stack to output.
                # Remove operator from stack.
                postfix, stack = postfix + stack[-1], stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
            print(f' c = {c}  pofix3 ={postfix} stack3 ={stack}')
        else:
            # Push it to the output.
            postfix += c
            print(f' c = {c}  pofix3 ={postfix} stack3 ={stack}')
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

    def followes(self):
        """The set of states that are gotten from following this state 
            and all its e (epsilon) arrows."""
        # Include this state in the returned set.
        states = {self}
        # If this tate has e arrows, i.e. label is None.
        if self.lable is None:
            # Loop through this state's arrows.
            for state in self.arrows:
                # Incorporate that state's e arrow states in states.
                states = (states | state.followes())
        # Returns the set of states.
        return states

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return True iff this NFA (instance) matches the string s."""
        # A list of previous states that we are still in.
        previous = self.start.followes()
        # Loop throug the string, a character at a time.
        for c in s:
            # Start with an empty set of curent states.
            current = set()
            # Loop through the previous states.
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c:
                    # Add followees for next state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current.
            previous = current
        # If the final state is in previous, then return True. False otherwise.
        return (self.end in previous)

def compileNFA(infix):
    """Compile NFA function -> Construct an NFA from the infix expression
        and return the NFA."""
    # Convert infix param to postfix.
    # Create a stack for NFAs.
    postfix, stack = shunt(infix), []
    # Loop through the postfix r.e left to right.
    for c in postfix:
        # Concatenation. Match single characters.
        if c == '.': 
            # Pop top NFA off stack.
            nfa2, stack = stack[-1], stack[:-1]
            # Pop the next NFA oof stack.
            nfa1, stack = stack[-1], stack[:-1]
            # Make accept state of NFA1 to non-accept.
            nfa1.end.accept = False
            # Make it point at start state of NFA2.
            nfa1.end.arrows.append(nfa2.start)
            # Push both NFAs to the stack.
            stack.append(NFA(nfa1.start, nfa2.end))

        # Or operator. Expressions A or B.
        elif c == '|': 
            # Pop top NFA off stack.
            nfa2, stack = stack[-1], stack[:-1]
            # Pop the next NFA off stack.
            nfa1, stack = stack[-1], stack[:-1]
            # Create new start and end states.
            start, end = State(None, [],False), State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept, nfa2.end.accept = False, False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Push new NFA to the stack.
            stack.append(NFA(start, end))

        # Kleene star. Concatenate zero or more strings.
        elif c == '*': 
            # Pop one NFA off stack.
            nfa1, stack = stack[-1], stack[:-1]
            # Create new start and end states.
            start, end = State(None, [],False), State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Push new NFA to the stack.
            stack.append(NFA(start, end))

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

# Test to see if Compile NFA function works as it should.
if __name__ == "__main__":
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1", "a|b"]:
        print(f'infix:      {infix}')
        print(f'postfix:    {shunt(infix)}')
        print(f'NFA:        {compileNFA(infix)}')
        print()