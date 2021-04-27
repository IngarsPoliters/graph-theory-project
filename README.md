# Project: Graph Theory 2021
**Name:** Ingars Politers

**Student ID:** G00374677
___
# Project Description
This is a program in Python to build an NFA (Non-deterministic Finite Automaton) from a regular expression. The NFA then can be used to check if the regular expression has matched any given string of text.
___
# Instructions
**Requirements:**
* [Python 3](https://www.python.org/downloads)
* [Git](https://git-scm.com/downloads)

### Clone the Repository:
**Open a Command-Line interface, navigate to any directory and enter:**
```
git clone https://github.com/IngarsPoliters/graph-theory-project.git
```
**Navigate to the project folder directory in Command-Line and enter:**
```
python3 gtProject.py
```
**Depending on your setup you may want to run this:**
```
python gtProject.py
```

# User Guide
**User Interface**

On running the program the user will be presented with a list of menu options to select:
![User Options](https://user-images.githubusercontent.com/48323426/116313356-92d7f100-a7a5-11eb-8f24-ebd04814e4b1.PNG)

**File Path**

To match the infix expression from a file:
1. Select Option 1
2. Enter Infix Expression

Here the user will have an option to select the following:

![image](https://user-images.githubusercontent.com/48323426/116313747-11cd2980-a7a6-11eb-9e5a-1f59357da8d1.png)
1. Select Option 1
2. Enter folder path to scan for text files

Here the folder will be scanned for any text files in the specified directory<br/>
The user will have an option to select the text file to match the expression:<br/>
![image](https://user-images.githubusercontent.com/48323426/116314365-e860cd80-a7a6-11eb-9263-251edf8373a2.png)

___
# Regular Expression
A regular expression (regex) is a string containing a series of characters, some of the charactrers in regex have a special meaning. For example, the special characters include ```.```, ```|```, ```*```. The meaning for these characters are as follows: 
* ```.``` To concatenate two characters together, so ```a.b``` means ```a``` followed by ```b```.
* ```|``` One OR the other, so ```a|b``` means ```a``` OR ```b```.
* ```*``` To concatenate zero or more, so ```a*``` means any number of ```a``` `s.


# Algorithms:

### Shunting Yard Algorithm
The shunting yard algorith was invented by [Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) in 1961, who was a Dutch computer scientist.<sup>12</sup> This algorithm is used for converting an infix expression to postfix expression. A stack is used for holding the operators, the purpose of the stack is to reverse the order of the operators in the expression using a last in first out method [LIFO](https://www.freshbooks.com/hub/accounting/what-is-lifo). The stack also serves as a storage structure, for no operator can be printed until both of its operands have appeared.<sup>13</sup> 

An operator precedence is defined to evaluate the priority of the operators as follows:`{'*': 100, '.': 90, '|': 80}`.

To convert an Infix expression to Postfix, using `a.(b.b)*.a` infix expression:
| Current Symbol | Operator Stack | Postfix String |
|:--------------:|:--------------:|:--------------:|
| a |  | a |
| . | . | a |
| ( | . ( | a |
| b | . ( | a b |
| . | . ( . | a b |
| b | . ( . | a b b | 
| ) | . | a b b . |
| * | . * | a b b . |
| . | . | a b b . * |
| a | . | a b b . * . a |
|  |  | a b b . * . a . |

As you can see the infix expression `a.(b.b)*.a` was converted to postfix expression: `abb.*.a.`.<sup>13</sup>

To see the the psedocode for converting infix to postfix [Go Here](https://aquarchitect.github.io/swift-algorithm-club/Shunting%20Yard/)

### Thompsons Construction
Thomposons Construction algorithm was invented by [Ken Thomposn](https://en.wikipedia.org/wiki/Ken_Thompson) in 1960's. This algorithm is used for converting a Postfix expression into a [Non-deterministic Finite Automata](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) (NFA). The NFA can be used to match strings against the regular expression.<sup>14</sup> It is easy to constuct an NFA than [DFA](https://en.wikipedia.org/wiki/Deterministic_finite_automaton) for a given regular language, the NFA has many paths for specific input from the current state to the next state. Every NFA is not DFA, but each NFA can be translated into DFA, NFA's can be represented by diagraphs called state.<sup>15</sup> In python the classes for NFA and the State are defined using class keywoard. 

The State class has label for the arrows pointing from one state to the other. The arrows are the list of states to point to, the accept is a boolean value if its in the accepted state:
```python
class State:
    def __init__(self, label, arrows, accept):
        self.label = label
        self.arrows = arrows
        self.accept = accept
```

The NFA class holds a start and end state locations for the state:
```python
class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
```
The function to compile the NFA from the given expression is defined:
```python
def compileNFA(infix):
    # Construct an NFA from the infix expression
```
The `compileNFA(infix)` function will convert the infix epxression to postfix using the shunting yard algorithm, and return the NFA.
This function has a stack of NFA's, where a for loop is defiend to loop over each character in postfix expression until the expression is complete and if and only if the stack holds one NFA it will be returned.

The stack uses the Last in First Out method. The NFA has 5 simple rules to apply when constructing the NFA from its regular expression. To see the process visually of constructing an NFA see this article [here](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)<sup>16</sup>

### Matching Alogrithm

### Followes algorithm


### TEST the algorithm and document here 





___
# Answers to follwing questions
* ### What is Regular Expression ?
Regular Expression, or regex, is extremely powerful in searching and manupulating strings.<sup>8</sup> The concept of Regular Expression arose in the 1950s by an American mathematician named Stephen Cole Kleene in which he formalized the description of a regular language.<sup>7</sup> A regular expression is a string containing a sequence of characters, some of these characters have a special meaning. All non special characters in regular expression match to themselves, e.g. the regex ```a``` matches the character ```'a'``` in a string, regex ```1``` matches ```'1'```. The special characters have their own special meaning in regex. <sup>8</sup> 

To understand some of the meanings behind these special characters see table below:<sup>10</sup>

| Special Character | Character Function | Example | 
|:-----------------:| ------------------ | ------- |
| ```.``` | Concatenation, matches anything except a newline | ```a.b``` Matches 3 string char beginning with ```'a'``` and ending with ```'b'``` |
| ```*``` | Kleene Star, Zero or more occurences of the same character | ```ab*``` Will apply to the ```'b'``` so ```ab*``` will match character ```'a'``` followed by any number of ```'b's``` |
| `\|` | Or, specifies 2 alternatives either one or the other expression | ```ab\|dc``` Matches anything containing either ```'ab'``` or ```'dc'```  |
| `+` | Plus, similar to `*` except this allows at least one occurence or more | `(ab)+` Will match `'aba'` and `'abbba'` but not `'aa'` |
| `?` | Question Mark, similar to `*` except this allows zero or one occurences | `ab?c` Will match `'abc'` and `'ac'` or nothing at all |
| `(...)`| Parentheses will group expressions together | `(ab\|bc)y` Will match either `'aby'` or `'bcy'` |

Based on these special characters, there are multiple expressions that can be built with this. Here in Ireland/UK we have different spelling differences compared to American spellings. Some of the examples are:

| American English | British English |
|:----------------:|:---------------:|
| Traveling | Travelling |
| Signaling | Signalling |
| Color | Colour | 
| Meter | Metre | 

This can cause some confusion from time to time. So to build a regular expression to find these differences, expressions would be as follows:
1. `(Traveling|Travelling)` would match one or the other, a simpler expression to use would be `Travell?ing` which would also match one or the other because the `'?'` operator will find zero or one occurrence of the character `'l'`.
2. `(Color|Colour)` would apply the same as above, so to substitute the simpler expression would apply as follows `Colou?r`.
This is just a small example of what regular expressions can achieve.

We are all familiar `CTRL-F` combination to enter a string to find any matching text. So in comparison Regular Expression engines rise above our favourite `CTRL-F` way of finding text. This will allow you to build a specific expression to search whatever pattern you're looking for. We recognize all kind of text patterns in our everyday lives, such as email addresses will have a single @ symbol in the middle, Irish PPSN numbers have 7 digits followed by a single character, all URL's start either with http:// or https:// and many more. This is how we humans know what is an email address, or a URL, whether it's secure or not.
Tech writer Cory Doctorow suggests that regular expressions should be taught before programming, to which he adds that knowing regex can save you so much time, to unknowledgeable people it would take 3000 steps to solve a problem, where just by knowing regex you can solve a problem in 3 steps.<sup>11</sup>





* ### How do regular expressions differ across implementations?

* ### Can all formal languages be encoded as regular expressions?
___
# References
Lab References:

* [Python and Git basics](https://web.microsoftstream.com/video/06cb5fe5-d714-42fd-839a-654fff91d5df)

* [Python lists and dictionaries](https://web.microsoftstream.com/video/aee618f5-b7cd-4763-aaa4-9f610d2f3212)

* [Python functions, ifs, and whiles](https://web.microsoftstream.com/video/fe45c30e-da2a-4952-89bd-71aae58ed836)

* [DFA Automata in Python](https://web.microsoftstream.com/video/ceb5505c-c3a2-4107-a9f3-d8d6492ee15f)

* [Implementing the Shunting Yard Algorithm in Python (Part 1)](https://web.microsoftstream.com/video/04fbd7f8-8880-426e-bfb5-2e5478db497e)

* [Implementing the Shunting Yard Algorithm in Python (Part 2)](https://web.microsoftstream.com/video/85152016-d320-4bbe-bfff-48baebcd59a6)

* [Regular Expressions](https://web.microsoftstream.com/video/166bc23b-d814-42f6-90df-5748712026bc)

* [Shunting Yard Algorithm for Regular Expressions](https://web.microsoftstream.com/video/9ddadf79-1e30-46d9-b1b5-63070e6d7a10)

* [Thompson's construction in code](https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32)

* [Sketching out the match function](https://web.microsoftstream.com/video/8fe195b7-f7c3-4265-86bc-7ff2c367eee9)

* [NFAs: Code to follow the e arrows](https://web.microsoftstream.com/video/59770e5a-2fed-4575-a4eb-0fd691b77d54)

References:

1. To get a better understanding of the RE library in python https://www.w3schools.com/python/python_regex.asp
2. TO get a better understanding of python functions https://www.w3schools.com/python/python_functions.asp
3. https://en.wikipedia.org/wiki/Thompson%27s_construction
4. Kleene Start Definition https://www.definitions.net/definition/kleene+star
5. Showed me a different perspective behind RE to NFA theory https://www.youtube.com/watch?v=RYNN-tb9WxI&t=370s&ab_channel=BarryBrown
6. Research on how to make a high quality Readme for github https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
7. [Regular expression, Wikipedia. Accessed 19 April 2021.](https://en.wikipedia.org/wiki/Regular_expression)
8. [Www3.ntu.edu.sg. 2021. Regular Expression (Regex) Tutorial. Accessed 19 April 2021.](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html)
9. [Guide on citing sources for Git README.md](https://github.com/freeCodeCamp/guide/pull/2337/files#diff-230a9052be3f27a5607aea2debfbf534)
10. [Emerson.emory.edu. 2021. Regular Expressions. Accessed 19 April 2021.](http://www.emerson.emory.edu/services/editors/ne/Regular_Expressions.html)
11. [Automatetheboringstuff.com. 2021. Automate the Boring Stuff with Python. Accessed 19 April 2021.](https://automatetheboringstuff.com/2e/chapter7/)
12. [En.wikipedia.org. 2021. Shunting-yard algorithm - Wikipedia. Accessed 20 April 2021.](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
13. [Mathcenter.oxford.emory.edu. 2021. The Shunting Yard Algorithm. Accessed 20 April 2021.](http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/)
14. [En.wikipedia.org. 2021. Thompson's construction - Wikipedia. Accessed 20 April 2021.](https://en.wikipedia.org/wiki/Thompson%27s_construction)
15. [www.javatpoint.com. 2021. NFA | Non-Deterministic Finite Automata - Javatpoint. Accessed 24 April 2021.](https://www.javatpoint.com/non-deterministic-finite-automata#:~:text=An%20NFA%20can%20be%20represented%20by%20digraphs%20called%20state%20diagram.&text=The%20initial%20state%20is%20marked,denoted%20by%20the%20double%20circle.)
16. [Medium. 2021. Visualizing Thompson’s Construction Algorithm for NFAs, step-by-step. Accessed 24 April 2021.](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)
17. 
