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
___
# Regular Expression
A regular expression (regex) is a string containing a series of characters, some of the charactrers in regex have a special meaning. For example, the special characters include ```.```, ```|```, ```*```. The meaning for these characters are as follows: 
* ```.``` To concatenate two characters together, so ```a.b``` means ```a``` followed by ```b```.
* ```|``` One OR the other, so ```a|b``` means ```a``` OR ```b```.
* ```*``` To concatenate zero or more, so ```a*``` means any number of ```a``` `s.


# Algorithms:

### Shunting Yard Algorithm

### Thompsons Construction
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
Tech writer Cory Doctorow suggests that regular expressions should be taught before programming, to which he adds that knowing regex can save you so much time, to unknowledgeable people it would take 3000 steps to solve a problem, where just by knowing regex you can solve a problem in 3 steps.
<sup>11</sup>






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
