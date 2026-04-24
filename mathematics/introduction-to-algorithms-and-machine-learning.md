# Introduction to Algorithms and Machine Learning

## _from Sorting to Strategic Agents_ Justin Skycak


Copyright © 2022 Justin Skycak.


First edition.


Allrights reserved. No partofthis publication may be reproduced,distributed,


or transmitted in any form or by any means, including photocopying,


recording, or other electronic or mechanical methods, without the prior


written permission of the author, except in the case of brief quotations


embodied in critical reviews and certain other noncommercial uses permitted


by copyright law. For permission requests, contact the author through the


website below.


www.justinmath.com


# **Preamble: The Story of Math** **Academy’s Eurisko Sequence**

This book was written to support Eurisko, an advanced math and


computer science elective course sequence within the Math Academy


program at Pasadena High School. During its operation from 2020 to


2023, Eurisko was the most advanced high school math/CS sequence in


the USA. (“Eurisko” is Greek for“I discover,” and is the namesake of an


AI system from the 1980s that won a particular game competition twice


in a row, even when the rules were changed in an attempt to handicap


it.)


Eurisko’s courses were presented at a level of intensity comparable to


those offered at elite technical universities, and students wrote all their


code from scratch before they were allowed to import external libraries.


This was possible because students had already learned a large amount


of college-level math through Math Academy, including multivariable


calculus, linear algebra, and differential equations by the end of 10th


grade.


v


The first Eurisko course was inspired by MIT’s Introduction to


ComputerScience andwentfarbeyondit. In addition to implementing


canonical data structures and algorithms (sorting, searching, graph


traversals), students wrote their own machine learning algorithms


from scratch (polynomial and logistic regression, k-nearest neighbors,


k-means clustering, parameter fitting via gradient descent).


In subsequent courses, students implemented more advanced machine


learning algorithms such as decision trees and neural networks. They


also reproduced academic research papers in artificial intelligence


leading up to Blondie24, an AI computer program that taught itself


to play checkers. At the same time, they worked together to implement


Space Empires, an extremely complex board game that pushed their


large-scale project skills (object-oriented design, version control, etc.)


to the limit. The ultimate goal was to create artificially intelligent


Space Empires players, drawing inspiration from techniques used in


Blondie24.


This book would not have been written if the Eurisko program had


not existed, and Eurisko would not have been possible without the


collaboration of Jason and Sandy Roberts, founders of Math Academy.


Eurisko started in June 2020 when Jason asked me to teach his 15

year-old son Colby some serious computer science over the summer.


He pulled in some of Colby’s classmates who had the necessary


mathematical background, and we put together a summer computer


science group that met three times a week with about 10 hours of


problem sets each week.


All problem sets required students to write code individually, from


scratch, in Python. They weren’t allowed to use external libraries.


Instead, they had to build everything themselves. They were allowed


to collaborate at a high level, discussing different approaches to solving


the problems, but every student had to write up every problem set on


their own.


To our surprise, the students progressed even faster than we could have


possibly expected:


   - At the start of June, they didn’t know how to write helper


functions. Even something as simple as checking if a string was a


palindrome was not trivial to them.


   - By the start of July, they had built a matrix class and a gradient


descent optimizer from scratch. The matrix class included


methods for matrix arithmetic as well as standard linear algebra


procedures like row reduction, determinants, and inverses.


   - By the start of August, they had built a regression library on top


of their matrix class and gradient descent optimizer. The library


includedpolynomial,logistic,andmultiple linearregressors with


interaction terms.


   - On top of all this,they also implemented standard algorithms for


sorting arrays and traversing graphs. And per Jason’s suggestion,


to get some systems programming experience, they also created


a simple version of the Space Empires board game and played


againsteachotherbyprogrammingandsubmittingautonomous


strategies.


At the end of the summer, Eurisko was fortunate to receive funding


for an official high school class through a partnership with App


Academy. Jason recruited a second cohort of incoming 10th graders,


and – through an extreme feat of class management – I managed to


continue supporting the first cohort while simultaneously launching


the second cohort within the same class period.


The class setup during the 2020-21 year was incredibly tricky. School


was fully remote due to the pandemic, and each cohort only had two


hours of class time over a group video call each week. If a student got


stuck, they had to ask for help by posting a message on Slack, and the


message had to be descriptive enough that I or another classmate could


quicklyunderstandtheirquestion andrespondbrieflywithoutburning


much time. This setup would be a steep learning curve for any junior


developer,much less a high school underclassman with little to no prior


coding experience – but we made do, and those students who muscled


through it emerged with an incredible amount of self-sufficiency and


debugging ability. (Not to mention, we did all this on school-issued


Chromebooks using free online development environments like Replit


and Gitpod.)


Later years became significantly smoother as I refined the curriculum


and school returned to in-person classes. During the 2021-22 year, most


problem sets contained written tutorials descriptive enough that I only


had to give a traditional lesson once per week. Over summer 2022 I


further refined and organized these tutorials into book chapters, and


during the 2022-23 year, the Eurisko classes were almost entirely self

service. Students read the assigned chapter on their own and completed


practice problems. In class, instead of giving a traditional lesson, I


answered questions and helped students debug their code.


In 2021, Jason shared a wild idea to have Eurisko students reproduce


the Blondie24 research papers and use that as inspiration to create


artificially intelligent Space Empires players. This became our vision


for the ultimate capstone project. The first Eurisko cohort came within


striking distance but ultimately ran out of time because they only


had two full years of Eurisko instead of three. But the second cohort


managed to reproduce one to two of the three papers in the Blondie24


research program and use this as inspiration for evolving combat


strategies within Space Empires.


The second cohort’s final year (2022-23) also happened to be the final


year of the Eurisko program due to my relocation. All together, there


were 16 students who stayed for the duration of the program.


   - _Cohort 1 (Summer 2020 - Spring 2022):_ David Gieselman, George

Meza, Riley Paddock, Colby Roberts, Elijah Tarr


   - _Cohort_ _2_ _(Fall_ _2020_ _-_ _Spring_ _2023):_ Maia Dimas, Justin Hong,

Cayden Lau, Anton Perez, William Wallius, Charlie Weinberger


   - _Cohort_ _3_ _(Fall_ _2021_ _-_ _Spring_ _2023):_ Celeste Acosta, Elias Gee,

Benjamin Park, Jeffrey Smithwick


   - _Cohort 4 (Fall 2022 - Spring 2023):_ Matteo Paz


Finally, a sincere thank you to Sanjana Kulkarni for her thoughtful


suggestions and diligent proofreading of this book.


# **Contents**

### _Preamble: The Story of Math Academy’s Eurisko_ Sequence v **I Hello World 1** 1. Some Short Introductory Coding Exercises 3 _2. Converting Between Binary, Decimal, and_ Hexadecimal 9 3. Recursive Sequences 17 4. Simulating Coin Flips 21 5. Roulette Wheel Selection 25 6. Cartesian Product 29 **II Searching and Sorting 33** _7. Brute Force Search with Linear-Encoding_ Cryptography 35

xi


### 8. Solving Magic Squares via Backtracking 41 _9. Estimating Roots via Bisection Search and Newton-_ Raphson Method 47 10. Single-Variable Gradient Descent 51 11. Multivariable Gradient Descent 63 12. Selection, Bubble, Insertion, and Counting Sort 69 13. Merge Sort and Quicksort 79 **III Objects 85** 14. Basic Matrix Arithmetic 87 _15. Reduced Row Echelon Form and Applications to_ Matrix Arithmetic 91 16. K-Means Clustering 95 17. Tic-Tac-Toe and Connect Four 105 18. Euler Estimation 111 19. SIR Model For the Spread of Disease 115 _20. Hodgkin-Huxley Model of Action Potentials in_ Neurons 119 21. Hash Tables 127 22. Simplex Method 133


### **IV Regression and Classification 151** _23. Linear, Polynomial, and Multiple Linear_ Regression via Pseudoinverse 153 _24. Regressing a Linear Combination of Nonlinear_ Functions via Pseudoinverse 169 _25. Power, Exponential, and Logistic Regression via_ Pseudoinverse 179 _26. Overfitting, Underfitting, Cross-Validation, and_ the Bias-Variance Tradeoff 193 27. Regression via Gradient Descent 207 28. Multiple Regression and Interaction Terms 215 29. K-Nearest Neighbors 223 30. Naive Bayes 237 **V Graphs 245** 31. Breadth-First and Depth-First Traversals 247 32. Distance and Shortest Paths in Unweighted Graphs 255 _33. Dijkstra’s Algorithm for Distance and Shortest_ Paths in Weighted Graphs 259 34. Decision Trees 271 35. Introduction to Neural Network Regressors 315


### 36. Backpropagation 329 **VI Games 359** 37. Canonical and Reduced Game Trees for Tic-Tac-Toe 361 38. Minimax Strategy 365 _39. Reduced Search Depth and Heuristic Evaluation_ for Connect Four 373 40. Introduction to Blondie24 and Neuroevolution 379 41. Reimplementing Fogel’s Tic-Tac-Toe Paper 389 42. Reimplementing Blondie24 401 43. Reimplementing Blondie24: Convolutional Version 407


# **Part I** **Hello World**

1


_Justin Skycak_


2


# **1. Some Short Introductory** **Coding Exercises**

Let’s get started on some introductory coding exercises. It’s assumed


that you’ve had some basic exposure to programming and that


you know about variables, functions, if statements, for loops, while


statements,arrays,strings,anddictionaries. Ideally,you’velearnedsome


object-oriented programming (classes, attributes, methods) as well. We


will speak in terms of Python, but the general ideas are applicable to any


programming language.


It’s important to understand that in coding, you should always try to


do as much as you can on your own, using Google as a resource if


needed. Don’t know what a word means? Google it. Don’t know how


to run a file from the command line? Google it. Don’t know how to get


the second character of a string? Google it. Our goal is to provide just


enough scaffolding to give you direction while avoiding hand-holding.


3


_Justin Skycak_

## **Exercises**


Write the following functions from scratch. Don’t use any external


libraries or any built-in functions that allow you to bypass the use of


for loops, while loops, or if statements in nontrivial ways. In particular,


don’t use `Set` or `Counter` . But you can use primitives like `len()`


and `Array.append` .


and `False` if not. You can ignore capitalization.


2 _._ `convert_to_numbers(string)`


Return an array of numbers corresponding to letters in a


string where space = 0 _,_ a = 1 _,_ b = 2 _,_ and so on. For


`'a` `cat'` .


4 _._ `get_intersection(array1,` `array2)`


Return an array consisting of the elements that are in both


`array1` and `array2` . There should not be any repeated


elements in the output array.


5 _._ `get_union(array1,` `array2)`


Return an array consisting of the elements that are in either


4


_Introduction to Algorithms and Machine Learning_


`array1` or `array2` . Again, there should not be any repeated


elements in the output array.


6 _._ `count_characters(string)`


Count the number of each character in a string and


return the counts in a dictionary. Lowercase and


uppercase letters should not be treated differently. For


7 _._ `is_prime(N)`


Check whether an input integer _N_ _>_ 1 is prime by checking


whether there exists some _n_ _∈{_ 2 _,_ 3 _,_ 4 _, . . ., ⌊N/_ 2 _⌋}_ such that

_n_ divides _N._ (The _⌊⌋_ symbol denotes the _floor function_ .)

## **Tests**


In another file, write a variety of tests for each function. Two example


tests are shown below for `check_if_symmetric` . You can use these,


but you should also write more tests that cover all the edge-cases you


can think of. (For example, an empty string is symmetric, and the string


`'!ab123` `4` `321ba!'` is also symmetric.)


5


_Justin Skycak_









6


_Introduction to Algorithms and Machine Learning_

## **Debugging**


Run your tests and fix any failures. If you struggle with anything, _don’t_

ask others for help until you’ve made a thorough effort to debug the


issue on your own. Here are some debugging tips:


1 _._ _Print out everything._ Within the function that you’re debugging,

print out every manipulation that your code makes, even if you


don’t think it’s making a mistake there. Bugs often show up in


places you don’t expect. Also, don’t just print out the values of


variables – itwillhelp you avoidconfusion ifyou printthe names


of the variables as well.


2 _._ _Identify_ _the_ _first_ _discrepancy._ Manually work out what the

printouts should be, and then look for the first instance where


the actual printouts deviate from what you’re expecting.


3 _._ _If the discrepancy involves a helper function, then isolate the issue_

_in a separate file and return to step_ 1 _._ If the issue is occurring

when you’re passing inputs into a helper function, then create


a separate file where all you do is pass those inputs into the


helper function, and go back to step 1 (print out everything)


with the helper function. This way, you can focus entirely on


the helper function without worrying about any other pieces of


code interacting with it.


4 _._ _If the discrepancy does not involve a helper function and you still_

_can’t figure_ _out what’s_ _going_ _wrong, then_ _ask for help._ Be sure

that you can explain what you’ve done to debug the issue so


far, including the furthest point back to which you’ve traced the


7


_Justin Skycak_


bug. Keepyourdebugging printstatements in yourfunction and


make sure the printouts are organized so that another person


can follow along with them without knowing all the nitty-gritty


details of your code.

## **Code Quality**


Your code should be clean and work in general. If you have thorough


testcoverage,youcanbefairlyconfidentthatyourcodeworksingeneral.


To be confident that your code is clean, do the following:


   - _Run your code through a linter_ (like pep8online) and fix all the

issues.


   - _Use_ _proper_ _cases._ In Python, variables, functions, and files

use `snake_case` (all lowercase with underscores separating


words), while classes use `PascalCase` (no spaces with each


separate word capitalized).


   - _Make sure that your variable names are clear and appropriate._

Variablesandclassesshouldbenouns,whilefunctions(including


methods) should be verbs. Additionally, names should be


descriptive. It’s okay to make a name multiple words long if


you need. For example, `calc_prob()` is much better than


`prob()` or `cp()` .


8


# **2. Converting Between Binary,** **Decimal, and Hexadecimal**

We are used to representing numbers using ten characters: 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4 _,_

5 _,_ 6 _,_ 7 _,_ 8 _,_ 9 _._ This is called the **decimal** number system.


However, there are other number systems that use more or fewer

characters. For example, the **binary** or **base-** 2 number system uses two

characters (0 and 1), and the hexadecimal or **base-** 16 number system

uses sixteen characters (0 _,_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _,_ 7 _,_ 8 _,_ 9 _, A, B, C, D, E, F,_


where _A_ = 10 _, B_ = 11 _, C_ = 12 _, D_ = 13 _, E_ = 14 _, F_ = 15).

## **Counting Demonstration**


Below is a table that illustrates how to count from zero to thirty

two in these different number systems. Each column corresponds to


a different number system, and each row shows how the same quantity


is represented in the three different number systems.


9


_Justin Skycak_


The key pattern to notice is that you always increment the character


in the rightmost digit, unless it has reached the last character. In that


case, you replace it with the first character and then increment the digit


directly to the left.


Decimal Binary Hexadecimal


0 0 0


1 1 1


2 10 2


3 11 3


4 100 4


5 101 5


6 110 6


7 111 7


8 1000 8


9 1001 9


10 1010 A


11 1011 B


12 1100 C


13 1101 D


14 1110 E


15 1111 F


16 10000 10


17 10001 11


18 10010 12


19 10011 13


20 10100 14


10


_Introduction to Algorithms and Machine Learning_


Decimal Binary Hexadecimal


21 10101 15


22 10110 16


23 10111 17


24 11000 18


25 11001 19


26 11010 1A


27 11011 1B


28 11100 1C


29 11101 1D


30 11110 1E


31 11111 1F


32 100000 20

## Converting from Base- b to Decimal


In general,if you have a number consisting of digits _xnxn−_ 1 _. . . x_ 1 _x_ 0 in

base- _b,_ then you can convert it to decimal using the following formula:


_xn · b_ _[n]_ + _xn−_ 1 _· b_ _[n][−]_ [1] + _. . ._ + _x_ 1 _· b_ [1] + _x_ 0 _· b_ [0]


For instance, the number 11010 in binary (base-2) corresponds to the


following number in decimal:


11


_Justin Skycak_


1 _·_ 2 [4] + 1 _·_ 2 [3] + 0 _·_ 2 [2] + 1 _·_ 2 [1] + 0 _·_ 2 [0]


= 26


Likewise, the number 3B07F in hexadecimal (base-16) corresponds to


the following number in decimal:


3 _·_ 16 [4] + B _·_ 16 [3] + 0 _·_ 16 [2] + 7 _·_ 16 [1] + F _·_ 16 [0]


3 _·_ 16 [4] + 11 _·_ 16 [3] + 0 _·_ 16 [2] + 7 _·_ 16 [1] + 15 _·_ 16 [0]


= 241791

## Converting from Decimal to Base- b


On the other hand, if you have a decimal number and you want to


convertitto base- _b,_ then you can repeatedly compute the highestpower

of _b_ (call it _b_ _[n]_ ) that’s less than or equal to your decimal number, and

then subtract off the largest multiple of _b_ _[n]_ that’s less than or equal to


your decimal number.


For example, to convert the decimal number 26 to binary (base-2), we


do the following:


1 _._ The largest power of 2 that’s less than or equal to 26 is 2 [4] =


16 _._ The largest multiple of 16 that’s less than or equal to 26 is


1 _·_ 16 = 16 _._ Subtracting off, we have 26 _−_ 16 = 10 _._


12


_Introduction to Algorithms and Machine Learning_


2 _._ The largest power of 2 that’s less than or equal to 10 is 2 [3] = 8 _._


Thelargestmultipleof 8 that’slessthanorequalto 10 is 1 _·_ 8 = 8 _._


Subtracting off, we have 10 _−_ 8 = 2 _._


3 _._ The largest power of 2 that’s less than or equal to 2 is 2 [1] = 2 _._


The largest multiple of 2 that’s less than or equal to 2 is 1 _·_ 2 = 2 _._


Subtracting off, we have 2 _−_ 2 = 0 _._


4 _._ We subtracted off 1 _·_ 2 [4] _,_ 1 _·_ 2 [3] _,_ and 1 _·_ 2 [1] _._ Therefore, We can

write 26 as 1 _·_ 2 [4] +1 _·_ 2 [3] +0 _·_ 2 [2] +1 _·_ 2 [1] +0 _·_ 2 [0] _,_ which has


coefficients 1 _,_ 1 _,_ 0 _,_ 1 _,_ 0 and therefore corresponds to the binary


number 11010 _._


Likewise, to convert the decimal number 241791 to hexadecimal (base

16), we do the following:


1 _._ The largest power of 16 that’s less than or equal to 241791 is

16 [4] = 65536 _._ The largest multiple of 65536 that’s less than or


equalto 241791 is 3 _·_ 65536 = 196608 _._ Subtracting off,we have


241791 _−_ 196608 = 45183 _._


2 _._ Thelargestpowerof 16 that’slessthanorequalto 45183 is 16 [3] =


4096 _._ The largest multiple of 4096 that’s less than or equal to


45183 is 11 _·_ 4096 = 45056 _._ Subtracting off, we have 45183 _−_


45056 = 127 _._


3 _._ The largest power of 16 that’s less than or equal to 127 is 16 [1] =


16 _._ The largest multiple of 16 that’s less than or equal to 127 is


7 _·_ 16 = 112 _._ Subtracting off, we have 127 _−_ 112 = 15 _._


4 _._ We subtractedoff 3 _·_ 16 [4] _,_ 11 _·_ 16 [3] _,_ 7 _·_ 16 [1] _,_ and 15 _·_ 16 [0] _._ Therefore,

We can write 241791 as 3 _·_ 16 [4] +11 _·_ 16 [3] +0 _·_ 16 [2] +7 _·_ 16 [1]


13


_Justin Skycak_


+15 _·_ 16 [0] _,_ which has coefficients 3 _,_ 11 _,_ 0 _,_ 7 _,_ 15 and therefore


corresponds to the hexadecimal number 3B07F _._

## **Exercises**


Write the following functions. You can use string representations for


all your inputs and outputs. As always, write a handful of tests for each


function.


1 _._ `binary_to_decimal(string)`


Take a binary representation of a number and


return the decimal representation. For example,


`binary_to_decimal('11010')` should return `'26'` .


2 _._ `hexadecimal_to_decimal(string)`


Take a hexadecimal representation of a number and return the


decimal representation.


3 _._ `decimal_to_binary(string)`


Take a decimal representation of a number and return the binary


representation.


4 _._ `decimal_to_hexadecimal(string)`


Take a decimal representation of a number and return the


hexadecimal representation.


5 _._ `binary_to_hexadecimal(string)`


Take a binary representation of a number and return the


hexadecimal representation. This is easy once you’ve written the


14


_Introduction to Algorithms and Machine Learning_


functions above: just convert from binary to decimal, and then


from decimal to hexadecimal.


6 _._ `hexadecimal_to_binary(string)`


Take a hexadecimal representation of a number and return the


binary representation. This is easy once you’ve written the


functions above: just convert from hexadecimal to decimal, and


then from decimal to binary.


15


_Justin Skycak_


16


# **3. Recursive Sequences**

A **recursive sequence** is a sequence where each term is a function of

the previous terms.


For example, consider the following rule for generating a recursive


sequence: starting with 3 _,_ generate each term by doubling the previous


term and adding 1 _._ The terms of this sequence are as follows:


3 _,_ 7 _,_ 15 _,_ 31 _,_ 63 _,_ 127 _,_ 255 _,_ 511 _, . . ._

## **Implementing Recursive Sequences**


One way to implement recursive sequences in code is to store all terms


in an array. For example, a function that returns the first _n_ terms of the


recursive sequence “starting with 3 _,_ generate each term by doubling the


previous term and adding 1” could be implemented as follows:


17


_Justin Skycak_





Ifallwe wantis the _n_ thterm,then itcan sometimes be more convenient


to make the implementation itself recursive. This way, we don’t have


to bother storing any intermediate values.


To understand how the function above works, first notice that

`calc_nth_term(1)` will return 3 _._ This is called the **base** **case** . If

a different input is passed, then the function will keep calling itself in a


lower input until it reaches the base case.


18


_Introduction to Algorithms and Machine Learning_
















## **Exercises**

Several different recursive sequences are described below. For each


sequence, write a function to generate an array containing first _n_ terms,

and then write a separate _recursive_ function to generate the _n_ th term.

Be sure to work these sequences out by hand and write tests.


1 _._ Starting with 5 _,_ generate each term by multiplying the previous


term by 3 and subtracting 4 _._


19


_Justin Skycak_


2 _._ Starting with 25 _,_ generate each term by taking half of the


previous term if it’s even, or multiplying by 3 and adding 1 if

it’s odd. (This is an instance of a _Collatz sequence_ .)


3 _._ Starting with 0 _,_ 1 _,_ generate each term by adding the previous

two terms. (This is the famous _Fibonacci sequence_ .)


4 _._ Starting with 2 _, −_ 3 _,_ generate each term by adding the product


of the previous two terms.


20


# **4. Simulating Coin Flips**

It’s often possible to estimate probabilities of events by simulating a


large number of random experiments and measuring the proportion of


trials in which the desired outcome occurred. This technique is known

as **Monte Carlo simulation**, named after a famous casino town.


To simulate random experiments in code, it’s common to use a random


number generator and then map the output of the random number


generator to an outcome of the experiment. For example, to simulate a


coin flip, one could generate a random decimal _r_ between 0 and 1 and


apply the following function:



outcome( _r_ ) =








heads if _r_ _<_ 0 _._ 5


tails otherwise



tails otherwise



21


_Justin Skycak_

## **Exercises**


Write a function `sim_probability(num_heads,` `num_flips)`


thatusesMonteCarlo simulation tocompute theprobabilityofgetting


a given number of heads in a given number of flips of a fair coin.


1 _._ First, simulate a large number of trials (say, 1000). In each trial,


flipacoin `num_flips` timesandcounthowmanyheadsappear.


You may import a random number generator for this.


2 _._ Then, count the number of trials in which exactly `num_heads`


heads appeared and divide it by the total number of trials (1000).


To test your implementation, work out the result by hand for several


combinations of `num_heads` and `num_flips`, and verify that your


function consistently returns results that are close to these true values.

## **High-Level Sanity Checks**


In this exercise, we tested the function by working out the probability


by hand. However, Monte Carlo simulation is often used to estimate


probabilities that are too complicated to work out by hand. In such


cases, it’s common to test the implementation by


   - working out simple cases by hand when possible, and


   - performing high-level sanity checks.


22


_Introduction to Algorithms and Machine Learning_


High-level sanity checks still involve identifying and verifying true


statements, but these true statements do not need to refer to exact


values.


To illustrate, let’s brainstorm some characteristics about how the


probability of getting a particular number of heads is related to the


number of coin flips:


   - The probabilities should form a distribution, i.e. they should be


non-negative and add up to 1 _._


   - This distribution should look somewhat like a bell curve, with


themostlikelyoutcomebeingthathalfofthecoinslandonheads


and the other half on tails.


   - Since landing on heads is just as likely as landing on tails, the


distribution should be symmetric.


To verify these characteristics, you can choose some value of


`num_flips`, compute the values


   - `sim_probability(1,` `num_flips)`,


   - `sim_probability(2,` `num_flips)`,


   - ...,


   - `sim_probability(num_heads,` `num_flips)`,


and then check the following:


23


_Justin Skycak_


   - The values are all non-negative and their sum is approximately


1 _._


   - The graph of probability vs `num_heads` looks like a symmetric


bell curve.


Try doing this for several values of `num_flips` .


24


# **5. Roulette Wheel Selection**

As we saw previously, it’s easy to simulate a random coin flip by


generating a random decimal _r_ between 0 and 1 and applying the


following function:



outcome( _r_ ) =








heads if _r_ _<_ 0 _._ 5


tails otherwise



tails otherwise



This is a special case of a more general idea: sampling from a discrete


probability distribution. Flipping a fair coin is tantamount to sampling


from the distribution `[0.5,` `0.5]`, i.e. 0 _._ 5 probability heads and 0 _._ 5


probability tails.


More complicated contexts may require sampling from longer


distributions that may or may not be uniform. For example, if we wish


to simulate the outcome of rolling a die with two red faces, one blue


face, one green face, and one yellow face, then we need to sample from


the distribution `[0.4,` `0.2,` `0.2,` `0.2]` .


Note that when we sample from the distribution, we need only

sample an _index_ from the distribution, and then use the index to look


25


_Justin Skycak_


up the desired value. For example, when we sample an index from


the distribution `[0.4,` `0.2,` `0.2,` `0.2]`, we have probabilities


0 _._ 4 _,_ 0 _._ 2 _,_ 0 _._ 2 _,_ and 0 _._ 2 of getting indices 0 _,_ 1 _,_ 2 _,_ and 3 respectively.


Then, all we need to do is look up that index in the following array:


`[red,` `blue,` `green,` `yellow]` .

## **Roulette Wheel Selection**


**Roulette** **wheel** **selection** is an elegant technique for sampling an

index from an arbitrary discrete probability distribution. It works as


follows:


1 _._ turn the distribution into a cumulative distribution,


2 _._ sample a random number _r_ between 0 and 1 _,_ and then


3 _._ find the index of the first value in the cumulative distribution


that is greater than or equal to _r._


To illustrate, let’s sample an index from the distribution


`[0.4,` `0.2,` `0.2,` `0.2]` that was mentioned above in the


context of a die roll.


1 _._ First, we construct the cumulative distribution:


2 _._ Then, we sample a random number _r_ between 0 and 1 _._ Suppose


we get _r_ = 0 _._ 63 _._


26


_Introduction to Algorithms and Machine Learning_


3 _._ Finally, we find the index of the first value in the cumulative


distribution that is greater than or equal to _r_ = 0 _._ 63 _._ In our


case, this is the value 0 _._ 8 at index 2 _,_ because the next value (1 _._ 0


at index 3) is greater than _r_ = 0 _._ 63 _._


So, we have sampled the index 2 _._

## **Exercise**


sampling index `i` .


To test your function on a particular distribution, sample many indices


from the distribution and ensure that the proportion of times each


index gets sampled matches the corresponding probability in the


distribution. Do this for a handful of different distributions.


27


_Justin Skycak_


28


# **6. Cartesian Product**

Implementing the Cartesian product provides good practice working


with arrays. Recall that the Cartesian product constructs all the points


whose elements occupy the given ranges. To illustrate:











29


_Justin Skycak_

## **Implementation**


The Cartesian product can be implemented elegantly via the following


procedure:


1 _._ Create an array that will contain all the points in the


cartesian product. Initialize it with a single empty point, i.e.


`points` `=` `[[]]` .


2 _._ Create a copy of `points`, and for each copied point, loop


through the first range and create an extended point by


appending a range item onto the copied point, create a handful


of new points. Collect all these extended points and save them


to `points` .


3 _._ Repeat step 2 for each range.


Below is a worked example.


30


_Introduction to Algorithms and Machine Learning_





















31


_Justin Skycak_

## **Copying an Array**


When copying an array, it’s essential to create an entirely new array, not


just reference the original array. Observe that if we just reference the old


array, then any new changes to the original array get propagated to the


new array.


To avoid this issue, you need to create an entirely new array:


Note that if our array contains items that are themselves arrays, then


it’s necessary to copy those items as well.


Implement `calc_cartesian_product`, verify that it reproduces


the example above, and write a handful of other tests.


32


# **Part II** **Searching and Sorting**

33


_Justin Skycak_


34


# **7. Brute Force Search with** **Linear-Encoding** **Cryptography**

An **encoding function** maps a string to a sequence of numbers. For

example, you have already implemented the _trivial encoding function_,

defined as follows:


There are many different types of encoding functions, but here we will

focus on _linear encoding functions_ . For example,using a linear encoding

function _f_ ( _x_ ) = 2 _x_ + 3 _,_ we can encode the message `'a` `cat'` as


follows:


35


_Justin Skycak_

## **Recovering a Message**


Ifwewanttorecoverourmessagefromthelinearencoding,wefirstsolve

for the inverse of the encoding function, i.e. the _decoding_ function:


_f_ ( _x_ ) = 2 _x_ + 3


_x_ = 2 _f_ _[−]_ [1] ( _x_ ) + 3


_f_ _[−]_ [1] ( _x_ ) = _[x][ −]_ [3]

2


Then, we apply the decoding function to the encoded message:


36


_Introduction to Algorithms and Machine Learning_

## **Recovering a Message with Multiple Possible** **Encoding Functions**


Now,supposewehaveamessage `[3,` `1,` `9,` `31,` `15]` andweknow


that this message was encoded using a linear encoding function _f_ ( _x_ ) =


_ax_ + _b_ with _a_ _∈{_ 1 _,_ 2 _}_ and _b_ _∈{_ 1 _,_ 2 _}._ Can we break the code and


recover the initial message?


The simplest way to do this is through **brute-force** **search**, which

involves trying every single possibility. Here, there are 4 possible


encoding functions:


_fab_ ( _x_ ) = _ax_ + _b_


_f_ 11( _x_ ) = 1 _x_ + 1


_f_ 12( _x_ ) = 1 _x_ + 2


_f_ 21( _x_ ) = 2 _x_ + 1


_f_ 22( _x_ ) = 2 _x_ + 2


By inverting these encoding functions, we obtain the following


decoding functions:


37


_Justin Skycak_


_fab_ _[−]_ [1][(] _[x]_ [) =] _[x][ −]_ _[b]_

_a_


_f_ 11 _[−]_ [1][(] _[x]_ [) =] _[x][ −]_ [1]

1

_f_ 12 _[−]_ [1][(] _[x]_ [) =] _[x][ −]_ [2]

1

_f_ 21 _[−]_ [1][(] _[x]_ [) =] _[x][ −]_ [1]

2

_f_ 22 _[−]_ [1][(] _[x]_ [) =] _[x][ −]_ [2]

2


Let’s apply each of these decoding functions to our encoded message


`[3,` `1,` `9,` `31,` `15]` and see what they come up with. Remember


that in order to represent a message, the results must all be integers


between 0 and 26 inclusive.


38


_Introduction to Algorithms and Machine Learning_























We conclude that the original message was `'a` `dog'` and that it was


encoded using _a_ = 2 and _b_ = 1 _._


39


_Justin Skycak_

## **Exercises**


As usual, be sure to include a variety of tests.


_f_ ( _x_ ) = _ax_ + _b_ and returns the resulting array of numbers.


2 _._ Write a function `decode_numbers(numbers,` `a,` `b)` that


attempts to decode the `numbers` array under the assumption


that the encoding function was _f_ ( _x_ ) = _ax_ + _b._ If the numbers


represent a message, then return the string corresponding to that


message. Otherwise, return `False` .


3 _._ Write a script to decode the message `[377,` `717,` `71,`

```
   513, 105, 921, 581, 547, 547, 105, 377, 717,

```




with a linear encoding function _f_ ( _x_ ) = _ax_ + _b_ where _a_ and


_b_ are both integers between 0 and 100 inclusive. Be sure to


print out all valid messages along with the values of _a_ and _b_ that


generated them. Note that although there may be more than


one valid message, only one will contain real words.


40


# **8. Solving Magic Squares via** **Backtracking**

Brute force search can often be slow or infeasible when there are lots of


possibilities that must be checked.


However, a technique called **backtracking** can often be used to

drastically cut down the number of possibilities that must be checked.


The idea is that whenever we find ourselves constructing a set of

possibilities thatwe know are hopeless,we skip overthem and _backtrack_

to the the point right before we started constructing the hopeless


possibilities.

## **Exercise: Brute Force**


Use brute-force search to find all arrangements of the digits 1 _,_ 2 _, . . .,_

9 into a 3 _×_ 3 _magic square_ where all the rows, columns, and diagonals

add up to 15 and no digits are repeated.


You may use 9 nested for loops if you’d like. It’s ugly but conceptually


simple and gets the job done. To illustrate, pseudocode is provided


below.


41


_Justin Skycak_





Note that this solution will be rather slow because it will require


checking 9! = 362 880 arrangements of digits.

## **Exercise: Backtracking**


Repeat the above exercise, but this time, whenever you reach an


arrangement of digits that can no longer become a valid magic square,


do not explore that arrangement any further. You can accomplish this


by doing the following:


42


_Introduction to Algorithms and Machine Learning_


1 _._ Write a function `is_hopeless(square)` to check whether


an incomplete square could ever become a valid square. A square


is hopeless if any row, column, or diagonal is filled in and does


not sum to 15 _._


2 _._ Place `continue` statements in your 9 nested for loops so that


you skip inner loops whenever you detect a hopeless square.


Below are some examples to illustrate how the `is_hopeless`


function should work.









43


_Justin Skycak_

















44


_Introduction to Algorithms and Machine Learning_


Below is an illustration of how to skip inner loops using `continue`


statements.















To give a concrete demonstration of backtracking, the first several


arrangements that get explored are shown below.


45


_Justin Skycak_







































46


# **9. Estimating Roots via** **Bisection Search and** **Newton-Raphson Method**

Two of the simplest methods for estimating roots of functions are

**bisection search** and the **Newton-Raphson method** . We will cover

both of these here.

## **Bisection Search**


To estimate the root of a function using **bisection** **search**, we start

with a lower bound and an upper bound and then repeatedly move one


bound halfway to the other.




_[√]_ 3
Let’s use bisection search to approximate the value of



2 by



approximating the root of the function _f_ ( _x_ ) = _x_ [3] _−_ 2 _._ We’ll use


_x_ = 1 as the lower bound and _x_ = 3 as the upper bound since


_f_ (1) _<_ 0 _<_ _f_ (3) _._ Note that the function values are positive to the


right of the root and negative to the left of the root.


47


_Justin Skycak_


1 _._ Our bounds are [1 _,_ 3] and the midpoint 2 _._ Since _f_ (2) = 6 _>_ 0 _,_


we know that 2 is bigger than the root. So, we use 2 as our new


upper bound.


2 _._ Our bounds are [1 _,_ 2] and the midpoint 1 _._ 5 _._ Since _f_ (1 _._ 5) =


1 _._ 375 _>_ 0 _,_ we know that 1 _._ 5 is bigger than the root. So, we use


1 _._ 5 as our new upper bound.


3 _._ Our bounds are [1 _,_ 1 _._ 5] and the midpoint is 1 _._ 25 _._ Since


_f_ (1 _._ 25) = _−_ 0 _._ 046875 _<_ 0 _,_ we know that 1 _._ 25 is smaller than


the root. So, we use 1 _._ 25 as our new lower bound.


4 _._ Our bounds are [1 _._ 25 _,_ 1 _._ 5] and the midpoint is 1 _._ 375 _._ Since


_f_ (1 _._ 375) _≈_ 0 _._ 599609 _>_ 0 _,_ we know that 1 _._ 375 is bigger than


the root. So, we use 1 _._ 375 as our new upper bound.




_[√]_ 3
Our next bounds are [1 _._ 25 _,_ 1 _._ 375] _,_ which tells us that



2 is between



1 _._ 25 and 1 _._ 375 _._ Our best guess is the midpoint, 1 _._ 3125 _,_ and the

_precision_ of our guess (i.e. the maximum amount we can be off by) is the

distance from the midpoint to the bounds. In our case, the precision


is 0 _._ 0625 _._ We can keep on repeating the bisection procedure until our


guess is as precise as we want.

## **Newton-Raphson Method**


To estimate the root of a function using the **Newton-Raphson**

**method**, we start with an initial guess and then repeatedly update our

guess to be the root of the _tangent line_ to the function.


48


_Introduction to Algorithms and Machine Learning_




_[√]_ 3
To illustrate, let’s again approximate the value of



2 by approximating



the root of the function _f_ ( _x_ ) = _x_ [3] _−_ 2 _._ We’ll use _x_ = 2 as our


initial guess. Remember that the slope of the tangent line is given by

the derivative, which in this case is _f_ _[′]_ ( _x_ ) = 3 _x_ [2] _._


1 _._ Our guess is _x_ = 2 _._ The function value is _f_ (2) = 6 and the

slope of the tangent line is _f_ _[′]_ (2) = 12 _,_ so the tangent line is


given by _y_ _−_ 6 = 12( _x −_ 2) _._ The root of this tangent line is


obtained by solving the equation 0 _−_ 6 = 12( _x −_ 2) _,_ which


gives us _x_ = 1 _._ 5 _._


2 _._ Ourguess is _x_ = 1 _._ 5 _._ The function value is _f_ (1 _._ 5) = 1 _._ 375 and

the slope of the tangent line is _f_ _[′]_ (1 _._ 5) = 6 _._ 75 _,_ so the tangent


line is given by _y_ _−_ 1 _._ 375 = 6 _._ 75( _x −_ 1 _._ 5) _._ The root of this


tangent line is obtained by solving the equation 0 _−_ 1 _._ 375 =


6 _._ 75( _x −_ 1 _._ 5) _,_ which gives us _x ≈_ 1 _._ 2963 _._


Our next guess would be _x_ = 1 _._ 2963 _._ Note that this is rounded to


4 decimal places, but we wouldn’t actually round this number in our


computer program. We can keep on repeating the Newton-Raphson

procedure until our guesses _converge_, i.e. stay the same when rounded

to the desired number of decimal places.


Lastly, note that to implement the Newton-Raphson procedure, it’s


necessary to come up with a formula for the root of the tangent line. If

the tangent line is _y −_ _y_ 0 = _m_ ( _x −_ _x_ 0) _,_ then the root is the value of _x_

that solves the equation 0 _−_ _y_ 0 = _m_ ( _x −_ _x_ 0) _._ You can find this value

of _x_ in terms of the other variables _x_ 0 _, y_ 0 _,_ and _m._


49


_Justin Skycak_

## **Exercises**


As usual, be sure to include a variety of tests.




_[√]_ 3
1 _._ Write a script that approximates



2 to a precision of 6 decimal



places using bisection search. (This should match up against the


provided example and continue for more iterations.)




_[√]_ 3
2 _._ Write a script that approximates



2 to a precision of 6 decimal



places using the Newton-Raphson method. (This should


match up against the provided example and continue for more


iterations.)


3 _._ Writeafunction `calc_root_bisection(a,` `n,` `precision)`

_[√]_ _n_
that approximates _a_ to the desired level of precision using


bisection search.


4 _._ Write a function `calc_root_newton_raphson(a,` `n,`

_[√]_ _n_
`precision)` that approximates _a_ to the desired level of


precision using the Newton-Raphson method.


50


# **10. Single-Variable Gradient** **Descent**

**Gradient** **descent** is a technique for minimizing differentiable

functions. The idea is that we take an initial guess as to what the


minimum is, and then repeatedly use the gradient to nudge that guess


further and further “downhill” into an actual minimum.


Let’s startby considering the simple case ofminimizing a single-variable

function – say, _f_ ( _x_ ) = _x_ [2] with the initial guess that the minimum is


at _x_ = 1 _._ Of course, this guess is not correct since the minimum is not


actually at _x_ = 1 _,_ but we will repeatedly update the guess to become


more and more correct.

## **Intuition About the Sign of the Derivative**


To update our guess, we start by computing the gradient at _x_ = 1 _._ For


a single-variable function, the gradient is just the plain old derivative.


51


_Justin Skycak_


_f_ ( _x_ ) = _x_ [2]


_f_ _[′]_ ( _x_ ) = 2 _x_


_f_ _[′]_ (1) = 2 _·_ 1 = 2


We found that the derivative is _f_ _[′]_ (1) = 2 _._ Now that we know the


value of the derivative at our guess, we can use it to update our guess.


In general, we have the following intuition:


   - If the derivative is _positive_, then the function is sloping _up_, and

we can move downhill by nudging our guess to the _left_ (i.e.

_decreasing_ the _x_ -value of our guess).


   - If the derivative is _negative_, then the function is sloping _down_,

and we can move downhill by nudging our guess to the _right_ (i.e.

_increasing_ our the _x_ -value of our guess).


Put more simply:


   - If the function is increasing, then we should decrease our guess.


   - If the function is decreasing, then we should increase our guess.


Here, the derivative _f_ _[′]_ (1) = 2 is positive, which means the function

is increasing and we should _decrease_ the _x_ -value of our guess. Indeed,

if we sketch up a graph of the situation, we can see that decreasing our


guess will take us closer to the actual minimum:


52


_Introduction to Algorithms and Machine Learning_

## **Gradient Descent Formula**


Now, the question is: by how much should we update our guess? If we


decrease the _x_ -value of our guess by too much,then we’ll pass right over


the minimum and end up on the other side, maybe even further away


from the minimum than we were to start with. But if we decrease the


_x_ -value of our guess by too little, then we will barely move at all and we


will have to repeat this procedure an excessive number of times before


actually getting close to the minimum.


For most differentiable functions that appear in machine learning, the


amountbywhichweshouldupdateourguessdependsonhowsteepthe


graphis. The steeperthe graphis,the furtherwe are from the minimum,


and the more freedom we have to update our guess without worrying


about moving it too far. So, we have the following formula for our next


guess:


53


_Justin Skycak_


_xn_ +1 = _xn −_ _αf_ _[′]_ ( _xn_ )


Before we perform any computations with this formula, let’s elaborate


on each part of it.


   - _xn_ is our _n_ th guess (i.e. the current guess), and _xn_ +1 is the next

guess.


   - _f_ _[′]_ ( _xn_ ) is the derivative at our current guess, and it tells us

whether the function is increasing or decreasing (as well as how


steep the function is).


   - _α_ is a positive constant called the _learning rate_, and the quantity

_αf_ _[′]_ ( _xn_ ) is the amount by which we update our guess. (We

generally try to run the gradient descent algorithm with a


learning rate around _α ≈_ 0 _._ 01 to start with, but if this learning


rate causes our guesses to diverge, then decrease the learning rate


and try again. More on that later.)


   - We are subtracting _αf_ _[′]_ ( _xn_ ) because we want to move our guess

_xn_ in the _opposite_ direction as the derivative _f_ _[′]_ ( _xn_ ). Remember

that if the function is increasing (i.e. positive derivative) then we


want to move our guess to the left (i.e. decrease it), and if the


function is decreasing (i.e. negative derivative) then we want to


moveourguesstotheright(i.e. increaseit). Thesteeperthegraph


is (i.e. the larger the magnitude of the derivative), the further we


want to move our guess.


54


_Introduction to Algorithms and Machine Learning_

## **Worked Example**


Now, let’s finish working out our example. We are trying to minimize

the function _f_ ( _x_ ) = _x_ [2] _,_ our first guess is _x_ 0 = 1 _,_ and the derivative at

this guess is _f_ _[′]_ (1) = 2 _._ If we use a learning rate of _α_ = 0 _._ 01 _,_ then our


next guess is


_x_ 1 = _x_ 0 _−_ _αf_ _[′]_ ( _x_ 0)

= 1 _−_ (0 _._ 01) _f_ _[′]_ (1)


= 1 _−_ (0 _._ 01)(2)


= 0 _._ 98 _._


To get the guess after that, we simply repeat the procedure again:


_x_ 2 = _x_ 1 _−_ _αf_ _[′]_ ( _x_ 1)

= 0 _._ 98 _−_ (0 _._ 01) _f_ _[′]_ (0 _._ 98)


= 0 _._ 98 _−_ (0 _._ 01)(1 _._ 96)


= 0 _._ 9604


In practice, we usually implement gradient descent as a computer


program because it is extremely tedious to do by hand. You should do


this and verify that you get the same results as shown in the table below.


In the table, we will round to 6 decimal places (but we do not actually


round in our computer program).


55


_Justin Skycak_


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 1 2 0 _._ 02


1 0 _._ 98 1 _._ 96 0 _._ 0196


2 0 _._ 9604 1 _._ 9208 0 _._ 019208


3 0 _._ 941192 1 _._ 882384 0 _._ 018824
... ... ... ...


25 0 _._ 603465 1 _._ 206929 0 _._ 012069


50 0 _._ 364170 0 _._ 728339 0 _._ 007283


100 0 _._ 132620 0 _._ 265239 0 _._ 002652


200 0 _._ 017588 0 _._ 035176 0 _._ 000352


300 0 _._ 002333 0 _._ 004665 0 _._ 000047


400 0 _._ 000309 0 _._ 000619 0 _._ 000006


We can visualize these results on our graph. Indeed, we see that our


guesses are converging to the minimum at _x_ = 0 _._


56


_Introduction to Algorithms and Machine Learning_

## **Local vs Global Minima**


There is one big caveat to gradient descent that is essential to


understand: it is not guaranteed to converge to a global minimum. It’s


possible for gradient descent to get "stuck" in a local minimum, just like


a ball rolling down a hill might roll into a depression and get stuck there


instead of falling all the way to the bottom of the hill.


To illustrate this caveat numerically, let’s use gradient descent to find

the minimum value of the function _f_ ( _x_ ) = _x_ [4] + _x_ [3] _−_ 2 _x_ [2] starting


with the initial guess _x_ = 1 _._ Note that the derivative of this function

is _f_ _[′]_ ( _x_ ) = 4 _x_ [3] + 3 _x_ [2] _−_ 4 _x._


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 1 3 0 _._ 03


1 0 _._ 97 2 _._ 593392 0 _._ 025934


2 0 _._ 944066 2 _._ 263154 0 _._ 022632


3 0 _._ 921435 1 _._ 990732 0 _._ 019907
... ... ... ...


25 0 _._ 736701 0 _._ 280693 0 _._ 002807


50 0 _._ 701878 0 _._ 053456 0 _._ 000535


100 0 _._ 693413 0 _._ 002445 0 _._ 000024


200 0 _._ 6930014 0 _._ 000005 0 _._ 000000


Uh oh! We are converging to the local minimum at _x_ = 0 _._ 69 _,_ but this


is not the global minimum of the function.


57


_Justin Skycak_

## **Trying Different Initial Guesses**


Because it’s possible for gradient descent to get stuck in local minima,


it’s often a good idea to run the gradient descent procedure with several


differentinitialguessesandusewhicheverfinalguessgivesthebestresult


(i.e. lowest function value).


To illustrate, let’s run the gradient descent algorithm a couple more


times with different initial guesses. For the next run, we’ll start with the


initial guess _x_ = 0 _._


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 0 0 0


1 0 0 0


2 0 0 0


3 0 0 0


58


_Introduction to Algorithms and Machine Learning_


Uh oh! This is even worse. We started at the top of a hill, and the


function is flat there (i.e. the derivative is zero), so our guesses are not


changing at all. In other words, the ball is not rolling down the hill


because it was placed at the very top where it’s flat.


Let’s try again, this time with initial guess _x_ = _−_ 1 _._


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 _−_ 1 3 0 _._ 03


1 _−_ 1 _._ 03 2 _._ 931792 0 _._ 029318


2 _−_ 1 _._ 059318 2 _._ 848862 0 _._ 028489


3 _−_ 1 _._ 087807 2 _._ 752289 0 _._ 027523
... ... ... ...


25 _−_ 1 _._ 410141 0 _._ 389810 0 _._ 003898


50 _−_ 1 _._ 441723 0 _._ 015732 0 _._ 000157


100 _−_ 1 _._ 442999 0 _._ 000022 0 _._ 000000


200 _−_ 1 _._ 443000 0 _._ 000000 0 _._ 000000


There we go! This time, we reached the desired global minimum.

## **Final Remarks**


There are many different variations of gradient descent that attempt to


betteravoid getting stuck in local minima. Forexample,some variations


incorporate the “momentum” of a ball rolling down a hill to help the


guesses “roll through” shallow local minima, whereas other variations


include random perturbations.


59


_Justin Skycak_


Additionally, there are ways to choose better initial guesses. In the


example above, we did not use any particular rationale when choosing


our initial guesses ( _x_ = 1 _,_ 0 _, −_ 1). But we could have (for instance)


randomly generated a large number of initial guesses, plugged each one


into our function _f_ ( _x_ ) _,_ and only run gradient descent on those initial


guesses that were associated with the lowest values of _f_ ( _x_ ) _._


Also note that it’s often necessary to try out different learning rates.


In the examples above, we used a learning rate of _α_ = 0 _._ 01 and this


worked out fine. If we had chosen a learning rate that was too high,


say _α_ = 0 _._ 5 _,_ then our guesses would update by too large an amount


each time, causing them to jump too far and never converge. This is


demonstrated below.


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 _−_ 1 3 1 _._ 5


1 _−_ 2 _._ 5 _−_ 33 _._ 75 _−_ 16 _._ 875


2 14 _._ 375 12444 6222


3 _−_ 6208 _−_ 956777563439 _−_ 478388781719


On the other hand, if we had chosen a learning rate that was too low,


say _α_ = 0 _._ 000001 _,_ then our guesses would update by too miniscule


an amount each time and we would require an excessive number of


iterations to converge. This is demonstrated below.


60


_Introduction to Algorithms and Machine Learning_


_n_ _xn_ _f_ _[′]_ ( _xn_ ) _αf_ _[′]_ ( _xn_ )


0 _−_ 1 3 0 _._ 000003


1 _−_ 1 _._ 000003 2 _._ 999994 0 _._ 000003


10 _−_ 1 _._ 000030 2 _._ 999940 0 _._ 000003


100 _−_ 1 _._ 000300 2 _._ 999399 0 _._ 000003


1000 _−_ 1 _._ 002997 2 _._ 993925 0 _._ 000003


10000 _−_ 1 _._ 029675 2 _._ 932619 0 _._ 000003


100000 _−_ 1 _._ 250157 1 _._ 873863 0 _._ 000002


1000000 _−_ 1 _._ 442997 0 _._ 000046 0 _._ 000000


Lastly, note that we can maximize functions by performing gradient

_ascent_, which is similar to gradient descent except that we replace the

subtraction with addition in the update rule: _xn_ +1 = _xn_ + _αf_ _[′]_ ( _xn_ ) _._

## **Exercises**


Use gradient descent to minimize the following functions. Before


looking at the graph, perform gradient descent using several different


initialguesses,andthenplugyourfinalguessesbackintothefunctionto


determinewhichfinalguessisthebest(i.e. givesyouthelowestfunction


value). Then, look at the graph to check whether you found the global


maximum.


1 _._ _f_ ( _x_ ) = _x_ [2] + _x_ + 1


2 _._ _f_ ( _x_ ) = _x_ [3] _−_ _x_ [4] _−_ _x_ [2]


61


_Justin Skycak_


3 _._ _f_ ( _x_ ) = [sin] _[ x]_

1 + _x_ [2]


4 _._ _f_ ( _x_ ) = 3 cos _x_ + _x_ [2] _e_ [sin] _[ x]_


62


# **11. Multivariable Gradient** **Descent**

Multivariable gradient descent is similar to single-variable gradient

descent, except that we replace the derivative _f_ _[′]_ ( _x_ ) with the gradient


_∇f_ ( _⃗x_ ) as follows:


_⃗xn_ +1 = _⃗xn −_ _α∇f_ ( _⃗xn_ )


Here, _⃗xn_ denotes the vector of _n_ th guesses for all the variables. For

example, if _f_ is a function of 2 input variables _x, y,_ then we denote


_⃗xn_ = _⟨xn, yn⟩_


and the update rule can be expressed as follows:


63


_Justin Skycak_


_⟨xn_ +1 _, yn_ +1 _⟩_ = _⟨xn, yn⟩−_ _α∇f_ ( _xn, yn_ )




    - _∂f_
= _⟨xn, yn⟩−_ _α_
_∂x_ _[, ][∂f]_ _∂y_



�����( _xn,yn_ )


## **Worked Example**

To illustrate, let’s use gradient descent to minimize the following


function:


_f_ ( _x, y_ ) = _x_ sin _y_ + _x_ [2]


First, we work out the gradient:




    - _∂f_
_∇f_ ( _x, y_ ) =
_∂x_ _[, ][∂f]_ _∂y_








 - _∂_
= - _x_ sin _y_ + _x_ [2][�] _,_ _[∂]_ - _x_ sin _y_ + _x_ [2][��]
_∂x_ _∂y_



= _⟨_ sin _y_ + 2 _x, x_ cos _y⟩_


If we start with the initial guess _x_ = 1 _, y_ = 2 (which we denote as

_⟨x, y⟩_ 0 = _⟨_ 1 _,_ 2 _⟩_ ) and use a learning rate of _α_ = 0 _._ 01 _,_ then our next

guess is


64


_Introduction to Algorithms and Machine Learning_


_⟨x_ 1 _, y_ 1 _⟩_ = _⟨x_ 0 _, y_ 0 _⟩−_ _α∇f_ ( _x_ 0 _, y_ 0)


= _⟨_ 1 _,_ 2 _⟩−_ (0 _._ 01) _⟨_ sin _y_ + 2 _x, x_ cos _y⟩|_ (1 _,_ 2)


= _⟨_ 1 _,_ 2 _⟩−_ (0 _._ 01) _⟨_ sin 2 + 2 _,_ cos 2 _⟩_


_≈⟨_ 0 _._ 970907 _,_ 2 _._ 004161 _⟩_ _._


We will carry out the rest of the iterations using a computer program.


You should do this too and verify that you get the same results as shown


in the table below. In the table, we will round to 6 decimal places (but


we do not actually round in our computer program).


_n_ _⟨xn, yn⟩_ _∇f_ ( _xn, yn_ )


0 _⟨_ 1 _,_ 2 _⟩_ _⟨_ 2 _._ 909297 _, −_ 0 _._ 416147 _⟩_


1 _⟨_ 0 _._ 970907 _,_ 2 _._ 004161 _⟩_ _⟨_ 2 _._ 849372 _, −_ 0 _._ 40771 _⟩_


2 _⟨_ 0 _._ 942413 _,_ 2 _._ 008239 _⟩_ _⟨_ 2 _._ 790665 _, −_ 0 _._ 399229 _⟩_


3 _⟨_ 0 _._ 914507 _,_ 2 _._ 012231 _⟩_ _⟨_ 2 _._ 733153 _, −_ 0 _._ 390711 _⟩_
... ... ...


25 _⟨_ 0 _._ 427158 _,_ 2 _._ 078619 _⟩_ _⟨_ 1 _._ 728121 _, −_ 0 _._ 207717 _⟩_


50 _⟨_ 0 _._ 086462 _,_ 2 _._ 109688 _⟩_ _⟨_ 1 _._ 031202 _, −_ 0 _._ 044371 _⟩_


100 _⟨−_ 0 _._ 242655 _,_ 2 _._ 084195 _⟩_ _⟨_ 0 _._ 385770 _,_ 0 _._ 119178 _⟩_


250 _⟨−_ 0 _._ 457667 _,_ 1 _._ 862063 _⟩_ _⟨_ 0 _._ 042547 _,_ 0 _._ 131426 _⟩_


500 _⟨−_ 0 _._ 496295 _,_ 1 _._ 657935 _⟩_ _⟨_ 0 _._ 003616 _,_ 0 _._ 043192 _⟩_


1000 _⟨−_ 0 _._ 499975 _,_ 1 _._ 577936 _⟩_ _⟨_ 0 _._ 000025 _,_ 0 _._ 003569 _⟩_


2000 _⟨−_ 0 _._ 500000 _,_ 1 _._ 570844 _⟩_ _⟨_ 0 _._ 000000 _,_ 0 _._ 000024 _⟩_


3000 _⟨−_ 0 _._ 500000 _,_ 1 _._ 570797 _⟩_ _⟨_ 0 _._ 000000 _,_ 0 _._ 000000 _⟩_


65


_Justin Skycak_


If we plot graph of the surface and some of our intermediate guesses,


we can see that our guesses do indeed take us down the valley into a


minimum:

## **Sanity Check**


When we run gradient descent on functions with more than two input


variables, it becomes difficult to visualize the graph of the function.


However, we can still verify that we’re moving in the correct direction


by evaluating the function at each guess and making sure the function


values are decreasing.


To illustrate, let’s add another column _f_ ( _xn, yn_ ) on the right side of

the table above. We can see that the function values in this column


are decreasing, and this tells us that we are successfully minimizing our


function _f._


66


_Introduction to Algorithms and Machine Learning_


_n_ _⟨xn, yn⟩_ _∇f_ ( _xn, yn_ ) �� _f_ ( _xn, yn_ )

0 _⟨_ 1 _,_ 2 _⟩_ _⟨_ 2 _._ 909297 _, −_ 0 _._ 416147 _⟩_ �� 1 _._ 909297

1 _⟨_ 0 _._ 970907 _,_ 2 _._ 004161 _⟩_ _⟨_ 2 _._ 849372 _, −_ 0 _._ 40771 _⟩_ �� 1 _._ 823815

2 _⟨_ 0 _._ 942413 _,_ 2 _._ 008239 _⟩_ _⟨_ 2 _._ 790665 _, −_ 0 _._ 399229 _⟩_ �� 1 _._ 741817

3 _⟨_ 0 _._ 914507 _,_ 2 _._ 012231 _⟩_ _⟨_ 2 _._ 733153 _, −_ 0 _._ 390711 _⟩_ �� 1 _._ 663164
... ... ... ����� ...

25 _⟨_ 0 _._ 427158 _,_ 2 _._ 078619 _⟩_ _⟨_ 1 _._ 728121 _, −_ 0 _._ 207717 _⟩_ �� 0 _._ 555717

50 _⟨_ 0 _._ 086462 _,_ 2 _._ 109688 _⟩_ _⟨_ 1 _._ 031202 _, −_ 0 _._ 044371 _⟩_ �� 0 _._ 081684

100 _⟨−_ 0 _._ 242655 _,_ 2 _._ 084195 _⟩_ _⟨_ 0 _._ 385770 _,_ 0 _._ 119178 _⟩_ �� _−_ 0 _._ 152491

250 _⟨−_ 0 _._ 457667 _,_ 1 _._ 862063 _⟩_ _⟨_ 0 _._ 042547 _,_ 0 _._ 131426 _⟩_ �� _−_ 0 _._ 228931

500 _⟨−_ 0 _._ 496295 _,_ 1 _._ 657935 _⟩_ _⟨_ 0 _._ 003616 _,_ 0 _._ 043192 _⟩_ �� _−_ 0 _._ 248103

1000 _⟨−_ 0 _._ 499975 _,_ 1 _._ 577936 _⟩_ _⟨_ 0 _._ 000025 _,_ 0 _._ 003569 _⟩_ �� _−_ 0 _._ 249987

2000 _⟨−_ 0 _._ 500000 _,_ 1 _._ 570844 _⟩_ _⟨_ 0 _._ 000000 _,_ 0 _._ 000024 _⟩_ �� _−_ 0 _._ 250000

3000 _⟨−_ 0 _._ 500000 _,_ 1 _._ 570797 _⟩_ _⟨_ 0 _._ 000000 _,_ 0 _._ 000000 _⟩_ �� _−_ 0 _._ 250000

## **Exercises**


Use gradient descent to minimize the following functions. Use several


different initial guesses, and then plug your final guesses back into the


function to determine which final guess is the best (i.e. gives you the


lowest function value). Be sure to evaluate the function at each guess


and verify that the function values are decreasing.


1 _._ _f_ ( _x, y_ ) = ( _x −_ 1) [2] + 3 _y_ [2]


2 _._ _f_ ( _x, y_ ) = _y_ [2] + _y_ cos _x_


3 _._ _f_ ( _x, y, z_ ) = ( _x −_ 1) [2] + 3( _y −_ 2) [2] + 4( _z_ + 1) [2]


4 _._ _f_ ( _x, y, z_ ) = _x_ [2] + 3 _y_ [2] + 4 _z_ [2] + cos( _xyz_ )


67


_Justin Skycak_


68


# **12. Selection, Bubble,** **Insertion, and Counting Sort**

There are many different methods for sorting items in arrays. Let’s go


over some of the simplest methods.

## **Selection Sort**


Theabsolutesimplestsortingmethod, **selection sort**,involvesbuilding

up a separate sorted array by repeatedly taking the minimum


element from the original array. To illustrate, let’s sort the array


`[3,` `5,` `8,` `2,` `5]` using selection sort.


   - Our original array is `[3,` `5,` `8,` `2,` `5]` and our sorted array


is empty `[` `]` since we just started. The minimum element of


our original array is `2`, and we move this element to the sorted


array.


69


_Justin Skycak_


   - Our original array is now `[3,` `5,` `8,` `5]` and our sorted array


is `[2]` . The minimum element of our original array is `3`, and


we move this element to the sorted array.


   - Our original array is now `[5,` `8,` `5]` and our sorted array is


`[2,` `3]` . The minimum element of ouroriginal array is `5`,and


we move this element to the sorted array.


   - Our original array is now `[8,` `5]` and our sorted array is


`[2,` `3,` `5]` . The minimum element of our original array is `5`,


and we move this element to the sorted array.


   - Our original array is now `[8]` and our sorted array is


`[2,` `3,` `5,` `5]` . The minimum element of our original array


is `8`, and we move this element to the sorted array.


   - Our original array is now empty `[` `]` and our sorted array is


`[2,` `3,` `5,` `5,` `8]` . We’re done!

## **Bubble Sort**


Another simple sorting method, **bubble** **sort** involves repeatedly

looping through all pairs of consecutive elements in the array


and swapping them if they are out of order. Let’s sort the array


`[3,` `5,` `8,` `2,` `5]` using bubble sort.


1 _._ First pass


order, so we do nothing.


70


_Introduction to Algorithms and Machine Learning_


order, so we do nothing.


swap them. Our updated array is `[3,` `5,` `2,` `8,` `5]` .


swap them. Our updated array is `[3,` `5,` `2,` `5,` `8]` .


2 _._ Since we made a swap in the first pass, we proceed to a second


pass.


**–** `[(3,` `5),` `2,` `5,` `8]`


**–** `[3,` `2,` `(5,` `5),` `8]`


**–** `[3,` `2,` `5,` `(5,` `8)]`


3 _._ Since we made a swap in the second pass, we proceed to a third


pass.


**–** `[2,` `(3,` `5),` `5,` `8]`


**–** `[2,` `3,` `(5,` `5),` `8]`


**–** `[2,` `3,` `5,` `(5,` `8)]`


4 _._ Since we made a swap in the third pass, we proceed to a fourth


pass.


71


_Justin Skycak_


**–** `[(2,` `3),` `5,` `5,` `8]`


**–** `[2,` `(3,` `5),` `5,` `8]`


**–** `[2,` `3,` `(5,` `5),` `8]`


**–** `[2,` `3,` `5,` `(5,` `8)]`


5 _._ Since we made no swaps in the fourth pass, we are done!

## **Insertion Sort**


**Insertion** **sort** is similar to bubble sort, with one key difference.

Whenever we find something out of order, instead of carrying out just


one swap,we repeatedly swap the out-of-orderelementbackwards until


it is in the correct position. Let’s illustrate.


   - `[(3,` `5),` `8,` `2,` `5]`


   - `[3,` `(5,` `8),` `2,` `5]`


   - `[3,` `5,` `(8,` `2),` `5]`   - Swap and note where we left off. We


will now start looking backwards, continuing to swap the `2`


until it is in the correct position.


   - `[3,` `(5,` `2),` `8*,` `5]`   - Swap and continue looking


backwards.


   - `[(3,` `2),` `5,` `8*,` `5]`   - Swap. Normally we would continue


looking backwards, but we can’t go backwards any more since


we’re at the beginning of the array. So, we’re done dealing with


the `2` and we can pick up from where we left off.


72


_Introduction to Algorithms and Machine Learning_


   - `[2,` `3,` `5,` `(8,` `5)]`   - Swap and note where we left off. We


will now start looking backwards, continuing to swap the `5`


until it is in the correct position.


   - `[2,` `3,` `(5,` `5),` `8*]`   - No swap needed. The `5` is in the


correct position. Normally we would pick up from where we left


off, but we left off at the end of the array, so we’re done!

## **Counting Sort**


Lastly, **counting sort** is quite different from all the sorting methods

we’ve coveredso far. It’s more involved,so we willoutline the procedure


before showing an example. The procedure is as follows:


1 _._ Identify the minimum number in the array and then subtract it


from all numbers in the array. This way, the updated array has a


minimum of `0` and all other elements are positive.


2 _._ Let `N` be the maximum number in the array. Create another


array, `counts`, with `N+1` entries, all initialized to `0` .


3 _._ Loop through the array. Foreach number `n` that you encounter,


increment `counts[n]` . This way, the value of `counts[n]`


represents the amount of times that you encountered the


number `n` .


4 _._ Read off the `counts` array into a sorted array that contains


`counts[n]` instances of each number `n` .


73


_Justin Skycak_


5 _._ In the first step, you subtracted the minimum number of the


original array. Undo that by adding the minimum number to


each element in your sorted array. Finally, we’re done!


Below is an example of applying counting sort to sort the array


`[3,` `5,` `8,` `2,` `5]` .


1 _._ The minimum number is `2` . Subtracting `2` from all numbers


in the array, the updated array is `[1,3,6,0,3]` .


2 _._ The maximum number in the new array is `6` . So, we let


`counts` `=` `[0,0,0,0,0,0,0]` .


3 _._ We loop through the array `[1,3,6,0,3]` and increment


`counts` .


4 _._ We read off the array `counts` `=` `[1,1,0,2,0,0,1]` as


follows: `1` zero, `1` one, `0` twos, `2` threes, `0` fours, `0` fives,


`1` six. So, we have a sorted array `[0,` `1,` `3,` `3,` `6]` .


74


_Introduction to Algorithms and Machine Learning_


5 _._ In the first step, we subtracted `2` . Now we add that back to each


item of the sorted array and get `[2,` `3,` `5,` `5,` `8]` . We’re


done!

## **Time Complexity**


It’s common to referto **time complexity** when talking about the speed

of various algorithms. Selection, bubble, and insertion sort all have

average-case time complexity _O_ ( _n_ [2] ) _,_ pronounced _order of n squared_ .

Loosely speaking, this means that if we were to create a mathematical


expression for the average number of operations required to sort a list

of _n_ elements, the variable part of the dominating term would be _n_ [2] _._


To understand why selection sort is _O_ ( _n_ [2] ) _,_ remember that selection


sortinvolvesrepeatedlybuildingupaseparatesortedarraybyrepeatedly


taking the minimum element from the original array. The original array


initially consists of _n_ elements, and we need to check each of them


when computing the minimum, so there are _n_ operations. Once we’ve


computed the minimum and moved it to the sorted array, we need to


repeat the procedure on the remaining _n −_ 1 elements. Continuing


the pattern and adding up all the operations, we get the following


expression:


75


_Justin Skycak_


_n_ + ( _n −_ 1) + ( _n −_ 2) + _. . ._ + 1


= _[n]_ [(] _[n]_ [ + 1)]

2



= [1]




[1] [1]

2 _[n]_ [2][ +] 2



2 _[n]_



Indeed,thedominatingtermis [1]



2 _[n]_ [2] _[,]_ [anditsvariablepartis] _[n]_ [2] _[.]_ [Thetime]



complexities ofbubble andinsertion sortcan be derivedin a similarway.



Counting sort is generally faster than selection, bubble, and insertion


sort. However, the drawback is that it can require lots of memory.

## **Exercises**


First, write a function `calc_min(arr)` that calculates the minimum


elementofanarraybyloopingthroughandkeepingtrackofthesmallest


element that has been found. Then, for each sorting method described


above, write a function that takes an input array and sorts it using the


described procedure.


Donotusethebuilt-in `min()` function; instead,useyour `calc_min`


function. Be sure to write plenty of tests that cover a variety of cases


(negative numbers, repeated numbers, duplicates, decimals, etc).


1 _._ Write `calc_min(arr)` .


2 _._ Write `selection_sort(arr)` .


76


_Introduction to Algorithms and Machine Learning_


3 _._ Write `bubble_sort(arr)` .


4 _._ Write `insertion_sort(arr)` .


5 _._ Write `counting_sort(arr)` .


6 _._ Derive the average-case time complexity of bubble sort.


7 _._ Derive the average-case time complexity of insertion sort.


8 _._ Derive the average-case time complexity of counting sort.


9 _._ Construct an example in which counting sort requires drastically


more memory than selection, bubble, and insertion sort. (Hint:


what would cause the `counts` array to become enormous?)


77


_Justin Skycak_


78


# **13. Merge Sort and Quicksort**

**Merge sort** is a sorting algorithm that works by breaking an array in

half, recursively calling merge sort on each half separately, and then


merging the two sorted halves. The base case is that empty arrays and


arrays of 1 item are already sorted (so if you call merge sort on such an


array, it leaves the array as-is).









Note that when an odd-length array is broken in half, it is okay for one


of the halves to have one more item than the other half.


79


_Justin Skycak_

## **Example of Merge Sort**


Below is a concrete example illustrating how `merge_sort` sorts an


array.


80


_Introduction to Algorithms and Machine Learning_


81


_Justin Skycak_

## **Quicksort**


Anothersortingalgorithm, **quicksort**,isverysimilartomergesort. The

only difference is that instead of splitting the array in half, we randomly

choose a _pivot element_ and split the array into 3 pieces: elements that are

less than the pivot element,elements that are equal to the pivot element,


and elements that are greater than the pivot element. Then, we apply


quicksort recursively on the “less than” and “greaterthan” pieces before


combining the pieces.


82


_Introduction to Algorithms and Machine Learning_

## **Time Complexity**


With an average-case time complexity of _O_ ( _n_ log _n_ ) _,_ merge sort and


quicksort are generally faster than selection, bubble, and insertion sort.


And unlike counting sort, they are not susceptible to blowup in the


amount of memory required.


83


_Justin Skycak_

## **Exercises**


Implement merge sort and quicksort. As always, be sure to write


plenty of tests that cover a variety of cases (negative numbers, repeated


numbers, duplicates, decimals, etc).


1 _._ Writeahelperfunction `merge(arr1,` `arr2)` thatmergestwo


sorted arrays by repeatedly looking at the first element of each


array and moving the smaller one into a new array.


2 _._ Write a function `merge_sort(arr)` that sorts an array using


the merge sort algorithm.


3 _._ Write a function `quicksort(arr)` that sorts an array using


the quicksort algorithm.


84


# **Part III** **Objects**

85


_Justin Skycak_


86


# **14. Basic Matrix Arithmetic**

Let’s use arrays to implement matrices and their associated


mathematical operations. We will jump straight to exercises - it


is assumed that you are already familiar with matrix arithmetic and


reduced row echelon form.

## **Exercise: Addition, Subtraction, Transpose,** **and Scalar Multiplication**


To start, create a class `Matrix` that implements basic matrix


arithmetic.


87


_Justin Skycak_





In addition to the methods shown above, you should also


implement `subtract` and `scalar_multiply` . (The input


to `scalar_multiply` is a number, and it should multiply all entries


of the matrix.)


To keep your code clean, you’ll need to implement some helper


attributes like `num_cols` and `num_rows` .


88


_Introduction to Algorithms and Machine Learning_





Your class (and tests) should be general to matrices of any dimensions.


Do not assume the matrix is square. However, if you struggle and get


stuck, then you can build some scaffolding for yourself by first hard

coding a class for, say, a 2 _×_ 3 matrix. Handling the general case often


becomes easier once you’ve worked through a specific case.


Rememberthatsome operations impose constraints on the dimensions


of the matrices involved. For example, you cannot add two matrices


unless their dimensions are equal. In your code, be sure to check that


all such constraints are satisfied before attempting to carry out the


operation. If any constraint is not satsified, then throw an error with


a descriptive message so that the user can understand why your matrix


class is unable to perform the desired computation.


89


_Justin Skycak_

## **Exercise: Matrix Multiplication and** **Recursive Determinant**


Next, implement the method `matrix_multiply` . This will be


trickier than the methods above, but remember that the element at row


_i_ and column _j_ in the product _AB_ is just the dot product of row _i_


in _A_ and column _j_ in _B._ (This means that you should write a helper


function for computing dot products.)


Then, implement the method `recursive_determinant` which


computes the determinant using recursive cofactor expansion. As a


refresher, below is an example of using recursive cofactor expansion


to compute the determinant of a 3 _×_ 3 matrix.





1 2 3










det



4 5 6

7 8 9











= 1 det




- 5 6


8 9




_−_ 2 det




4 6


7 9



+ 3 det




4 5


7 8



= 1 (5 det [9] _−_ 6 det [8]) _−_ 2 (4 det [9] _−_ 6 det [7]) + 3 (4 det [8] _−_ 5 det [7])


= 1 (5 _·_ 9 _−_ 6 _·_ 8) _−_ 2 (4 _·_ 9 _−_ 6 _·_ 7) + 3 (4 _·_ 8 _−_ 5 _·_ 7)


= 1 (45 _−_ 48) _−_ 2 (36 _−_ 42) + 3 (32 _−_ 35)


= 1 ( _−_ 3) _−_ 2 ( _−_ 6) + 3 ( _−_ 3)


= _−_ 3 + 12 _−_ 9


= 0


90


# **15. Reduced Row Echelon** **Form and Applications to** **Matrix Arithmetic**

Recall from linear algebra the following procedure for converting a


matrix to reduced row echelon form (RREF):













91


_Justin Skycak_


This algorithm is a bit tricky, so before you attempt to implement


anything, be sure to work out the above algorithm by hand on several


concrete examples until you feel comfortable with it.


Again, we will jump straight to exercises – it is assumed that you are


already familiar with matrix arithmetic and reduced row echelon form.

## **Exercise: RREF with Helper Functions**


Once you’re comfortable working out the algorithm by hand, write


some helper functions.


   - For example, the first helper method you’ll need to write will


check whether a pivot row exists for a particular column in


a matrix. If it does exist, then return the index of the row.


Otherwise, return nothing.


   - There are at least 3 other helper methods that you’ll need to


write. But don’t stop thinking once you come up with 3 helper


methods. Keep going until you think you’ve really narrowed


down the problem to its atomic sub-procedures.


It’s often a good idea to write tests for your helper functions and get

them passing _before_ you start trying to use them together, especially

when you’re fairly new to coding. In your tests, be sure to consider


a variety of matrices that are substantially different from each other.


When writing tests, your goal is to try (and fail) to break the function


that you wrote.


92


_Introduction to Algorithms and Machine Learning_


Once you’ve written the helper functions, you can stitch them together


into the full RREF algorithm.

## **Exercise: Inverse via RREF**


Once you’ve written a working RREF algorithm, you can use it to


implement a method that computes the inverse of a matrix. Remember


that to compute the inverse of a square matrix _A,_ you can just


1 _._ augment the matrix as [ _A|I_ ] where _I_ is the identity matrix,


2 _._ run RREF on the augmented matrix to convert it to [ _I|A_ _[−]_ [1] ] _,_


and then


3 _._ read _A_ _[−]_ [1] on the right-hand side.

## **Exercise: Determinant via RREF**


You can also use the RREF algorithm to compute determinants much


faster than with the recursive cofactor expansion method.


   - Whenever you divide a row by some amount during the RREF


algorithm, the determinant gets divided by that same amount.


   - Whenever you swap two rows during the RREF algorithm, the


determinant switches sign (from positive to negative or vice


versa).


93


_Justin Skycak_


   - At the end of the RREF algorithm, the final matrix has a


determinant of 1 _._


   - So, you can “build up” the determinant during the execution


of the RREF algorithm by keeping track of the product of the


numbers you divide by and switching the sign every time you


swap two rows.


To avoidcluttering up yourRREF algorithm,itis advisable to justcopy

paste it into a new `determinant` method and then make whatever


adjustments you need to build up the determinant along the way.


94


# **16. K-Means Clustering**

**Clustering** istheprocessofgroupingsimilarrecordswithindata. Some

examples ofclusters in real-life data include users who buy similaritems,


songs in a similar genre, and patients with similar health conditions.


One ofthe simplestclustering methods is called **k-means clustering** . It

works by guessing some initial clusters in the data and then repeatedly


updating the guesses to make the clusters more cohesive.


1 _._ Initialize the clusters.


1 _._ 1 Randomly divide the data into _k_ parts (where _k_ is an input


parameter). Each part is an initial cluster.


1 _._ 2 Compute the mean of each part. Each mean is an initial


cluster center.


2 _._ Update the clusters.


2 _._ 1 Re-assign each record to the cluster with the nearest center.


2 _._ 2 Compute the new clustercenters by taking the mean of the


records in each cluster.


3 _._ Keep repeating step 2 until the clusters stop changing.


95


_Justin Skycak_

## **Worked Example**


As a concrete example, consider the following data set. Each row


represents a cookie with some ratio of ingredients. We can use k-means


clustering to separate the data into different overarching “types” of


cookies.





We will work out the first iteration of the k-means algorithm supposing


that there are _k_ = 3 clusters in the data.


96


_Introduction to Algorithms and Machine Learning_


The first step is to randomly divide the data into _k_ = 3 clusters. To do


this, we can simply add an extra column in our data that represents the


cluster number, and count off cluster numbers 1 _,_ 2 _,_ 3 _,_ 1 _,_ 2 _,_ 3 _,_ and so


on. We will put the extra column at the beginning of the data set.





97


_Justin Skycak_


So, our initial guesses for the clusters are as follows:


98


_Introduction to Algorithms and Machine Learning_


To compute each cluster center, we take the mean of each component


of the data (ignoring the first component, which is the cluster label and


was not part of the original data set).





99


_Justin Skycak_


Carrying out the above computations, we get the following results


(rounded to 3 decimal places for readability):


Once we’ve computed each cluster center, we then loop through the


data and re-assign each data point to the nearest cluster center. We will


use the Euclidean distance when determining the nearest cluster center.


100


_Introduction to Algorithms and Machine Learning_




## **Interpreting the Clusters**

If you repeat this process over and over, the cluster labels will eventually


stop changing,indicating that every data point is assigned to the nearest


cluster. In this example, it should be straightforward to interpret the


meaning of your final clusters:


101


_Justin Skycak_


1 _._ One clusterrepresents cookies with a greaterproportion of sugar.


These might be sugar cookies.


2 _._ Another cluster represents cookies with a greater proportion of


butter. These might be shortbread cookies.


3 _._ Another cluster represents cookies with a greater proportion of


eggs. These might be fortune cookies.

## **Elbow Method**


Finally, remember that _k_ (the number of clusters that we assume)


is an input parameter to the algorithm. Because we usually don’t


know the number of clusters in the data beforehand, it’s helpful to


graph the "cohesiveness" of the clusters versus the value of _k._ We can


measure cohesiveness by computing the total sum of distances between


points and their cluster centers (the smaller the total distance, the more


cohesive the clusters).


The graphoftotaldistance versus _k_ willbe decreasing: the more clusters


we assume, the closer the points will be to their clusters. In the extreme


case where we set _k_ equal to the number of points in our data set, it’s


possible thateachpointcouldbe assignedto a separate cluster,resulting


in a total distance of 0 but providing us with absolutely no information


about groups of similar records in the data.


To choose _k,_ it’s common to use the **elbow** **method** and roughly

estimate where the graph forms an “elbow,” i.e. exhibits maximum


curvature. This represents the point of diminishing returns, meaning


102


_Introduction to Algorithms and Machine Learning_


that assuming a greater number of clusters in the data will not make


the clusters that much more cohesive.

## **Exercises**


First, implement the example that was worked out above and interpret


the resulting clusters. Then, generate a plot of total distance versus _k_


and identify the elbow in the graph. Was _k_ = 3 a good choice for the


number of clusters in our data set? In other words, is the elbow of the


graph near _k_ = 3?


103


_Justin Skycak_


104


# **17. Tic-Tac-Toe and Connect** **Four**

One of the best ways to get practice with object-oriented programming


is implementing games. Tic-tac-toe and connect four are great for


learning the ropes. Later on, we will also use these implementations


for developing AI players.

## **Exercise: Tic-Tac-Toe with Random Players**


Develop a tic-tac-toe game in which two random players play against


each other. You can implement your game however you want, provided


that you adhere to the constraints below.


   - There should be a `Game` class and a `RandomPlayer`


class. The game should be initialized via


105


_Justin Skycak_


in the `Player` class that takes a copy of the tic-tac-toe board as


input and returns a random (but legal) move as output.


   - Players should NOT actually update the board themselves   

otherwise, they could cheat by changing the board in any way


they please. Rather, the game should ask the player what move


it chooses, and then the game should update its own board


(provided that it’s a legal move). If a player attempts to make


an illegal move, then the game should skip that player’s turn.


   - You should be able to run an entire game via `game.run(log)` .


If `log` `==` `true`, then the game should print out the sequence


of board states and player moves (as well as whether or not the

move was legal). _Be sure to implement logging as soon as you start_


_coding up the game, because printing out logs will save you a lot of_


_time debugging._

## **Exercise: Tic-Tac-Toe with Manual Player**


Then, create a `ManualPlayer` class that allows you to play manually


via the command line. You can use Python’s built-in `input()`


function for this.


106


_Introduction to Algorithms and Machine Learning_


Besuretotestyourgamebymanuallyplayingahandfulofgamesagainst


the random player. (Don’t try to win every game – you’ll need to tie


and lose some games for testing purposes.)

## **Exercise: Strategy Functions**


Currently, you have two types of tic-tac-toe players: `RandomPlayer`


and `ManualPlayer` . The only difference between these players is in


how they choose moves. The rest of the code is duplicated, which is


not ideal. There should really be just one `Player` class, where the


`choose_move` method is automatically adjusted as desired.


the tic-tac-toe board as input and returns a random move as output.


107


_Justin Skycak_


Once you’ve implemented this, test your game again by manually


playing a handful of games against the random player. Additionally,


make sure that you are always able to beat the “cheater” strategy shown


below. (If the cheater strategy wins, then it probably means that you’re


allowing the player to access the actual game board instead of giving it

a _copy_ of the board.)










## **Exercise: Custom Strategy**

Create a custom strategy that beats the random player most of the time.


108


_Introduction to Algorithms and Machine Learning_

## **Exercise: Connect Four**


Repeattheaboveexercisesforthegameofconnectfour. There arereally


only two differences:


1 _._ A player chooses a column to place their piece into, rather than


an actual board space. So, a move will be a single integer rather


than a tuple.


2 _._ Checking whether a player has won is more complicated.


109


_Justin Skycak_


110


# **18. Euler Estimation**

Arrays can be used to implement more than just matrices. We can also


implement other mathematical procedures like Euler estimation. We


willjump straightto exercises – itis assumedthatyou’re already familiar


with Euler estimation from calculus.

## **Exercise: Single-Variable Euler Estimator**


To start, build a single-variable Euler estimation class as follows:


111


_Justin Skycak_







Then, use your Euler estimator to plot several solution curves to the


following differential equation on the interval _x ∈_ [0 _,_ 5] _._ (Your Euler


estimator generates a list of points, and then you can use that list of


points to generate a plot.)


d _y_
d _x_ [=] _[ x][ −]_ [2]


For one curve, use the initial condition _y_ (0) = _−_ 2 _._ For another curve,


use _y_ (0) = _−_ 1 _._ Then another curve with _y_ (0) = 0 _,_ another with


_y_ (0) = 1 _,_ and another with _y_ (0) = 2 _._ All 5 of these curves can go on


the same plot.


112


_Introduction to Algorithms and Machine Learning_


Based on your knowledge of calculus, you should be able to tell if your


plots look right.

## **Exercise: Multivariable Euler Estimator**


Once you’ve implemented a single-variable Euler estimator, you can


generalize it to simulate systems of differential equations. For example,


consider the following system:


_a_ _[′]_ ( _t_ ) = _a_ ( _t_ ) + 1


_b_ _[′]_ ( _t_ ) = _a_ ( _t_ ) + _b_ ( _t_ )


_c_ _[′]_ ( _t_ ) = 2 _b_ ( _t_ ) + 3 _t_


To simulate this system starting with the initial state _a_ ( _−_ 0 _._ 4) =


_−_ 0 _._ 45 _, b_ ( _−_ 0 _._ 4) = _−_ 0 _._ 05 _, c_ ( _−_ 0 _._ 4) = 0 _,_ construct a multivariable


Euler estimator as follows:


113


_Justin Skycak_













114


# **19. SIR Model For the Spread** **of Disease**

One of the simplest ways to model the spread of disease using

differential equations is the **SIR model** . Let’s construct a SIR model

and use our multivariable Euler estimator to plot the solution curves.


The SIR model assumes three sub-populations: susceptible, infected,


and recovered.


   - The number of susceptible people ( _S_ ) decreases at a rate


proportional to the rate of meeting between susceptible and


infected people (because susceptible people have a chance of


catching the disease when they come in contact with infected


people).


   - The number of infected people ( _I_ ) increases at a rate


proportional to the rate of meeting between susceptible


and infected people (because susceptible people become infected


after catching the disease), and decreases at a rate proportional to


the number of infected people (as the diseased people recover).


115


_Justin Skycak_


   - The number of recovered people ( _R_ ) increases at a rate


proportional to the number of infected people (as the diseased


people recover).

## **Exercise: SIR Model Equations and Initial** **Conditions**


First, write a system of differential equations using the following


assumptions:


   - There are initially 1000 susceptible people and 1 infected person.


   - The number of meetings between susceptible and infected


people each day is proportional to the product of the numbers


of susceptible and infected people, by a factor of 0 _._ 01 _._ The


transmission rate of the disease is 3% _._ (In other words, 3% of


meetings result in transmission.)


   - Each day, 2% of infected people recover.























d _S_

= ___ _,_ _S_ (0) = ___
d _t_

d _I_

= ___ _,_ _I_ (0) = ___
d _t_

d _R_

= ___ _,_ _R_ (0) = ___
d _t_


116


_Introduction to Algorithms and Machine Learning_


If you’ve written the system correctly, then at _t_ = 0 you should have



d _S_



d _I_ d _R_

d _t_ [= 0] _[.]_ [28] _[,]_ d _t_



d _S_ d _I_

d _t_ [=] _[ −]_ [0] _[.]_ [3] _[,]_ d _t_



d _t_ [= 0] _[.]_ [02] _[ .]_


## **Exercise: SIR Model Simulation**

Then use your multivariable Euler estimator to simulate the solution


curve, and plot the result.


   - Be sure to choose the step size small enough that the simulation


doesn’t blow up, but large enough that it doesn’t take long to


run.


   - Likewise, choose an interval that displays all the main features of


the differential equation, i.e. an interval that shows the behavior


of the curves until they start to asymtpote off.


If your plot is correct, then you should be able to easily describe what


is happening in the plot and why it is happening.


117


_Justin Skycak_


118


# **20. Hodgkin-Huxley Model of** **Action Potentials in Neurons**

In 1952, Alan Hodgkin and Andrew Huxley published a differential


equation model of “spikes” (i.e. “action potentials”) in the voltage of


neurons. Forthis work,theyreceivedthe 1963 NobelPrize in Physiology


or Medicine (shared with Sir John Carew Eccles).


Below, we summarize the key points of the model so that you


may implement and simulate it yourself. The primary source is the

original paper, _A quantitative description of membrane current and its_


_application to conduction and excitation in nerve._


Forbackgroundinformation,itis recommendedto watchthe following


short videos:


1 _._ _Neurons or nerve cells - Structure function and types of neurons_ by

Elearnin


( `[https://www.youtube.com/watch?v=cUGuWh2UeMk](https://www.youtube.com/watch?v=cUGuWh2UeMk)` )


2 _._ _2-Minute Neuroscience: Action Potential_ by Neuroscientifically

Challenged


( `[https://www.youtube.com/watch?v=W2hHt_PXe5o](https://www.youtube.com/watch?v=W2hHt_PXe5o)` )


119


_Justin Skycak_

## **Idea 1: Start with Physics Fundamentals**


From physics, we know that current is proportional to voltage by a


constant _C_ called the capacitance:


_I_ = _C_ [d] _[V]_

d _t_


So, the voltage of a neuron can be modeled as



d _V_



_C_ _[.]_



d _V_ _[I]_

d _t_ [=] _C_



For neurons, we have _C_ _≈_ 1 _._ 0 _._

## **Idea 2: Decompose Current into Four** **Subcurrents (Stimulus and Ion Channels)**


The current _I_ consists of


   - a stimulus _s_ to the neuron (from an electrode or other neurons),


   - current flux across sodium and potassium ion channels ( _I_ Na and

_I_ K), and


   - current leakage, treated as a channel _I_ L _._


120


_Introduction to Algorithms and Machine Learning_


The stimulus increases the voltage, while the flux and leakage decrease


it. So, we have



d _V_



_C_ [[] _[s][ −]_ _[I]_ [Na] _[ −]_ _[I]_ [K] _[ −]_ _[I]_ [L][]] _[ .]_



d _V_ [1]

d _t_ [=] _C_


## **Idea 3: Model the Ion Channel Currents**

The current across an ion channel is proportional to the voltage


difference, relative to the equilibrium voltage of that channel:


_I_ Na( _V, m, h_ ) = _g_ Na( _m, h_ ) ( _V_ _−_ _V_ Na) _V_ Na _≈_ 115


_I_ K( _V, n_ ) = _g_ K( _n_ ) ( _V_ _−_ _V_ K) _V_ K _≈−_ 12


_I_ L( _V_ ) = _g_ L _·_ ( _V_ _−_ _V_ L) _V_ L _≈_ 10 _._ 6


The constants of proportionality are conductances, which were


modeled experimentally:


_g_ Na( _m, h_ ) = _g_ Na _m_ [3] _h_ _g_ Na _≈_ 120


_g_ K( _n_ ) = _g_ K _n_ [4] _g_ K _≈_ 36


_g_ L = _g_ L _g_ L _≈_ 0 _._ 3 _,_


where


121


_Justin Skycak_


d _n_

d _t_ [=] _[ α][n]_ [(] _[V]_ [ )(1] _[ −]_ _[n]_ [)] _[ −]_ _[β][n]_ [(] _[V]_ [ )] _[n]_



d _m_

d _t_ [=] _[ α][m]_ [(] _[V]_ [ )(1] _[ −]_ _[m]_ [)] _[ −]_ _[β][m]_ [(] _[V]_ [ )] _[m]_



d _h_

d _t_ [=] _[ α][h]_ [(] _[V]_ [ )(1] _[ −]_ _[h]_ [)] _[ −]_ _[β][h]_ [(] _[V]_ [ )] _[h.]_



and


0 _._ 01(10 _−_ _V_ )       _αn_ ( _V_ ) = _βn_ ( _V_ ) = 0 _._ 125 exp _−_ _[V]_
exp [0 _._ 1(10 _−_ _V_ )] _−_ 1 80







0 _._ 1(25 _−_ _V_ )       _αm_ ( _V_ ) = _βm_ ( _V_ ) = 4 exp _−_ _[V]_
exp [0 _._ 1(25 _−_ _V_ )] _−_ 1 18








        _αh_ ( _V_ ) = 0 _._ 07 exp _−_ _[V]_

20




- 1
_βh_ ( _V_ ) =
exp [0 _._ 1(30 _−_ _V_ )] + 1 _[.]_


## **Exercise**

Your task is to implement the Hodgkin-Huxley neuron model using


Euler estimation. You can represent the state of the neuron at time _t_


using


        -         _t,_ ( _V, n, m, h_ ) _,_


andyou can approximate the initialvalues bysetting _V_ 0 = 0 andsetting

_n, m,_ and _h_ equal to their asymptotic values for _V_ 0 = 0:


122


_Introduction to Algorithms and Machine Learning_


_αn_ ( _V_ 0)
_n_ 0 =
_αn_ ( _V_ 0) + _βn_ ( _V_ 0)

_αm_ ( _V_ 0)
_m_ 0 =
_αm_ ( _V_ 0) + _βm_ ( _V_ 0)

_αh_ ( _V_ 0)
_h_ 0 =
_αh_ ( _V_ 0) + _βh_ ( _V_ 0)


(When we take _V_ 0 = 0 _,_ we are letting _V_ represent the voltage _offset_

from the usual resting potential.)


Simulate the system for _t_ _∈_ [0 _,_ 80 ms] with step size ∆ _t_ = 0 _._ 01 and


stimulus



_∪_ [56 _,_ 57] _∪_ [59 _,_ 60] _∪_ [62 _,_ 63] _∪_ [65 _,_ 66]



150 _,_ _t ∈_ [10 _,_ 11] _∪_ [20 _,_ 21] _∪_ [30 _,_ 40] _∪_ [50 _,_ 51] _∪_ [53 _,_ 54]



_s_ ( _t_ ) =













0 otherwise _._



You should get the following result:


123


_Justin Skycak_


The corresponding plot of _n, m,_ and _h_ is provided to help you debug:


Lastly, here is an incomplete code template to get you started:


124


_Introduction to Algorithms and Machine Learning_









125


_Justin Skycak_


126


# **21. Hash Tables**

Under the hood, dictionaries are hash tables.


The most elementary (and inefficient) version of a hash table would be


a list of tuples. For example, if we wanted to implement the dictionary





then we’d have the following list of tuples:





To add a new key-value pair to the dictionary, we’d just append the


corresponding tuple, and to look up the value for some key, we’d just


127


_Justin Skycak_


loopthroughthetuplesuntilwegettothetuplewiththekeywewanted


(and then we’d return the corresponding value).

## **Exercise: Buckets and Hash Functions**


Searching through a long array is slow. So, to be more efficient, we use

several lists of tuples. We call those lists **buckets**, and we use a **hash**

**function** to tell us which bucket to put the new key-value pair in.


Complete the code below to implement a special case of an elementary


hash table. We’ll expand on this example soon, but let’s start with


something simple.


128


_Introduction to Algorithms and Machine Learning_





129


_Justin Skycak_


Here’s an example of how the hash table will work:


130


_Introduction to Algorithms and Machine Learning_

## **Exercise: Hash Table**


Write a class `HashTable` thatgeneralizes the hashtable you previously


wrote. Thisclassshouldstorean arrayofbuckets,andthehashfunction


should add up the alphabet indices of the input string and mod the


result by the number of buckets.


131


_Justin Skycak_





132


# **22. Simplex Method**

The **simplex method** is a technique for maximizing linear expressions

subject to linear constraints. Many applied problems can be framed like


this – for example, a business may have a variety of raw materials and


need to determine the most profitable inventory of products that they


can produce from those materials. This would ultimately amount to


maximizing a linear expression for profit, subject to a linear inequality


for each type of raw material (the total amount of raw material used in


the products produced must be less than or equal to the amount of raw


material available).


At its core, the simplex method is just algebra that can be implemented


elegantly using array manipulations. Let’s work through the algebra on


an example:


maximize _x_ 1 + 2 _x_ 2 + _x_ 3 such that


2 _x_ 1 + _x_ 2 + _x_ 3 _≤_ 14


4 _x_ 1 + 2 _x_ 2 + 3 _x_ 3 _≤_ 28


2 _x_ 1 + 5 _x_ 2 + 5 _x_ 3 _≤_ 30


_x_ 1 _,_ _x_ 2 _,_ _x_ 3 _≥_ 0


133


_Justin Skycak_

## **Step 1: Introduce Slack Variables**


Math is generally easier when we work with equations (rather than


inequalities). We can convert most of the system above into equations if


we move everything to the RHS and then assign those RHS expressions

to new variables called _slack variables_ .


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


0 _≤_ 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


0 _≤_ 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


0 _≤_ 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


_x_ 4 = 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


_x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


The slack variables that we created are _x_ 4 _, x_ 5 _, x_ 6 _._ Note that the original

system is entirely equivalent to the definition of the slack variables. The


system involving slackvariables is exactlythe same as the originalsystem,


but written a little differently. (This is analogous to change of variables


in integration.)


134


_Introduction to Algorithms and Machine Learning_

## **Step 2: Evaluate the Objective Quantity**


Each system in the above form is associated with a “guess” that comes

from setting all the _basic_ variables equal to 0 _._ The basic variables are the

variables that appear in the expressions for other _non-basic_ variables.


In our case, the basic variables are _x_ 1 _, x_ 2 _, x_ 3 because they appear in the

quantity we’re trying to maximize and also in the expressions for the

non-basic variables _x_ 4 _, x_ 5 _, x_ 6 _._ You can also remember that the basic

variables are the RHS and the non-basic variables are the LHS.


When we set the basic variables equal to 0 _,_ we plug


_x_ 1 = 0


_x_ 2 = 0


_x_ 3 = 0


into the quantity that we’re trying to maximize (known as the _objective_

_quantity_ ) and get


_x_ 1 + 2 _x_ 2 + _x_ 3


_→_ 0 + 2(0) + 0


_→_ 0 _._


135


_Justin Skycak_


So currently, we have a guess _x_ 1 = _x_ 2 = _x_ 3 = 0 and this brings the

objective quantity to 0 _._ This is a pretty bad guess, but we’re going to


repeatedly improve it until it’s optimal.

## **Step 3: Identify the Basic Variable with the** **Greatest Slope**


We’re going to improve upon our guess by repeatedly increasing the


basic variable that will most quickly improve our guess.


To improve our guess, we need to increase the objective quantity _x_ 1 +

2 _x_ 2 + _x_ 3 _,_ which we write as a function below:


_M_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 + 2 _x_ 2 + _x_ 3


The basic variable that will most quickly improve our guess is the one


that will make the objective quantity increase the fastest (when we


increase that variable). In other words, it is the one with the greatest


slope.


slope( _x_ 1) = 1 _,_ slope( _x_ 2) = 2 _,_ slope( _x_ 3) = 1


Here, the basic variable with the largest slope is _x_ 2 _._ So this what we will

increase.


136


_Introduction to Algorithms and Machine Learning_

## **Step 4: Identify which Non-Basic Variable** **to Trade for that Basic Variable**


The basic variable with the largest slope is _x_ 2 _._ We will now trade this

for one of the non-basic variables ( _x_ 4 _, x_ 5 _, x_ 6).


For our next guess, we want to increase _x_ 2 as much as possible (since

doing so will increase our objective quantity the fastest). But we can’t


increase it too much – remember that the system has constraints, and


we can’t invalidate those constraints.


Each of the constraints of the original system was converted into a non

basic variable. So, we need to identify the non-basic variable that places

the strictest constraint on _x_ 2 _,_ and then trade it with _x_ 2 (i.e. make that

variable basic in exchange for making _x_ 2 non-basic).


Here is where we are so far:


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


_x_ 4 = 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


_x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


Since 0 _≤_ _x_ 4 _, x_ 5 _, x_ 6 _,_ we have the following constraints:


137


_Justin Skycak_


0 _≤_ _x_ 4 = 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


0 _≤_ _x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


0 _≤_ _x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


Let’s simplify a bit:


0 _≤_ 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


0 _≤_ 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


0 _≤_ 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


Now, let’s set move _x_ 2 to the LHS of each constraint and set the other

basic variables ( _x_ 1 _, x_ 3) equal to zero so that we can see which constraint

is strictest:


_x_ 2 _≤_ 14


_x_ 2 _≤_ 14


_x_ 2 _≤_ 6


The strictest constraint is the constraint that places the lowest non
negative upper bound on _x_ 2 _._ Here, the third constraint is the strictest,

and if you look at the work backwards, you’ll see that it came from the

non-basic variable _x_ 6:


138


_Introduction to Algorithms and Machine Learning_


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


_↕_


0 _≤_ 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


_↕_


_x_ 2 _≤_ 6


So, we need to trade the non-basic variable _x_ 6 for the basic variable _x_ 2 _._

## **Step 5: Execute the Trade**


This step will feel more familiar than the earlier steps. We have an

equation relating _x_ 6 and _x_ 2:


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


All we need to do is solve this equation for _x_ 2 and then substitute that

into our system.


Solving for _x_ 2 _,_ we get



_x_ 2 = 6 _−_ [2]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6] _[.]_



139


_Justin Skycak_


Then, we substitute into our system. The only catch is that we need to

fullyreplacethe _x_ 6 = equationwiththe _x_ 2 = equation. (Thisequation

issupposedtocapturetherelationshipbetween _x_ 2 and _x_ 6,andifwejust

substituted _x_ 2 in the RHS, then it would simplify to a useless equation

_x_ 6 = _x_ 6).


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


_x_ 4 = 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


_x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6




6 _−_ [2]



5 _[x]_ [6]




+ _x_ 3



maximize _x_ 1 + 2




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6]



_x_ 4 = 14 _−_ 2 _x_ 1 _−_




6 _−_ [2]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5





_−_ _x_ 3




6 _−_ [2]



5 _[x]_ [6]



_x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5





_−_ 3 _x_ 3



_x_ 2 = 6 _−_ [2]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6]



0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


140


_Introduction to Algorithms and Machine Learning_



maximize 12 + [1]



5 _[x]_ [6]




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5




[8] [1]

5 _[x]_ [1][ +] 5



_x_ 4 = 8 _−_ [8]



5 _[x]_ [6]



_x_ 5 = 16 _−_ [16]




[2]
5 _[x]_ [1] _[ −]_ _[x]_ [3][ +] 5



5 _[x]_ [6]



_x_ 2 = 6 _−_ [2]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6]



0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


Just to keep things tidy, we’ll re-order the equations so that the LHS


variables are sorted:



maximize 12 + [1]




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5



5 _[x]_ [6]



_x_ 2 = 6 _−_ [2]

5

_x_ 4 = 8 _−_ [8]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6]



5 _[x]_ [6]




[8] [1]

5 _[x]_ [1][ +] 5



_x_ 5 = 16 _−_ [16]




[2]
5 _[x]_ [1] _[ −]_ _[x]_ [3][ +] 5



5 _[x]_ [6]



0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6

## **Step 6: Repeat Steps 2-5 Until No Slopes Are** **Positive**


_Evaluate the objective quantity._ We will evaluate the objective quantity

for our new guess. Remember that our guess is obtained by setting the


141


_Justin Skycak_


basicvariablesequalto 0 _._ Thebasicvariablesarenow _x_ 1 _, x_ 3 _, x_ 6 _._ Setting

these variables equal to 0 _,_ our objective quantity becomes



12 + [1]




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5



5 _[x]_ [6]



_→_ 12 + [1]




[1]

5 [(0)] _[ −]_ [2(0)] _[ −]_ [2] 5



5 [(0)]



_→_ 12 _._


So our guess has improved! Our previous guess gave us an objective


quantity of 0 _,_ and our new guess gave us an objective quantity of 12 _._

## **Sanity Checks**


In this example, if you ever get a new guess that does not appear to


increase the objective quantity, then something went wrong. The new

guess should _always_ increase the objective quantity. (In rare cases,

it’s possible for the simplex algorithm to “cycle” around suboptimal


minima that yield the same value of the objective function, but this


example is not one of those cases.)


Additionally, you should always verify that your guess satisfies the

constraints of the _original_ problem statement. Below is an explanation

of how to do that. As a reminder, the original problem statement was

to maximize _x_ 1 + 2 _x_ 2 + _x_ 3 subject to the following constraints:


142


_Introduction to Algorithms and Machine Learning_


2 _x_ 1 + _x_ 2 + _x_ 3 _≤_ 14


4 _x_ 1 + 2 _x_ 2 + 3 _x_ 3 _≤_ 28


2 _x_ 1 + 5 _x_ 2 + 5 _x_ 3 _≤_ 30


_x_ 1 _,_ _x_ 2 _,_ _x_ 3 _≥_ 0


The original problem statement is framed in terms of variables

_x_ 1 _, x_ 2 _, x_ 3 _._ The slack variables _x_ 4 _, x_ 5 _, x_ 6 are artificial things that we

made up. Here, our guess is _x_ 1 = _x_ 3 = _x_ 6 = 0 _._ Although _x_ 2 is not

explicit in our guess, we can find it by substituting our guess into our


system. Doing so, we find


_x_ 2 = 6 _,_ _x_ 4 = 8 _,_ _x_ 5 = 16 _._


So in terms of the original variables of our system, our guess is


_x_ 1 = 0 _,_ _x_ 2 = 6 _,_ _x_ 3 = 0 _._


Indeed, if we evaluate the objective quantity shown in the problem


statement, we get


_x_ 1 + 2 _x_ 2 + _x_ 3


_→_ 0 + 2(6) + 0


_→_ 12 _._


143


_Justin Skycak_


Additionally,the guess _x_ 1 = 0 _,_ _x_ 2 = 6 _,_ _x_ 3 = 0 satisfies all constraints

in the original problem statement.

## **Another Iteration**


_Identify the basic variable with the largest slope._ Our objective function

is now



_M_ ( _x_ 1 _, x_ 3 _, x_ 6) = 12 + [1]



5 _[x]_ [6] _[,]_




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5



and the basic variable with the largest slope is _x_ 1 _._


_Identify which non-basic variable to trade for that basic variable._ With

a bit of algebra work (which you should do on your own), we have the


following constraints:


_x_ 1 _≤_ 15


_x_ 1 _≤_ 5


_x_ 1 _≤_ 5


Thesecondandthirdconstraintsarethestrictest. Theyareequallystrict,


so we can choose to proceed with either one. Referring back to our

system (shown below), these two constraints come from _x_ 4 and _x_ 5 _._


144


_Introduction to Algorithms and Machine Learning_



maximize 12 + [1]



5 _[x]_ [6]




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



_x_ 2 = 6 _−_ [2]

5

_x_ 4 = 8 _−_ [8]



5 _[x]_ [6]



5 _[x]_ [6]




[8] [1]

5 _[x]_ [1][ +] 5



_x_ 5 = 16 _−_ [16]




[2]
5 _[x]_ [1] _[ −]_ _[x]_ [3][ +] 5



5 _[x]_ [6]



0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


Let’s proceed with the _x_ 4 constraint since it’s simpler (it contains fewer

variables).


_Execute the trade._ Solving for _x_ 1 in terms of _x_ 4 (which you should do

on your own), we get



_x_ 1 = 5 _−_ [5]




[5] [1]

8 _[x]_ [4][ +] 8



8 _[x]_ [6]



I’ll leave it to you to finish the trade execution by substituting into your


system.


In the next round, you should find that your guess has improved, but


that no slopes are positive, which means you’re done and have found


the optimal solution.


145


_Justin Skycak_

## **Array Manipulations**


The algebra above can be implemented more elegantly as array


manipulations. Let’s start by taking the system that we obtained after


introducing slack variables, and converting it to an array:


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


_x_ 4 = 14 _−_ 2 _x_ 1 _−_ _x_ 2 _−_ _x_ 3


_x_ 5 = 28 _−_ 4 _x_ 1 _−_ 2 _x_ 2 _−_ 3 _x_ 3


_x_ 6 = 30 _−_ 2 _x_ 1 _−_ 5 _x_ 2 _−_ 5 _x_ 3


0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


maximize _x_ 1 + 2 _x_ 2 + _x_ 3


2 _x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 = 14


4 _x_ 1 + 2 _x_ 2 + 3 _x_ 3 + _x_ 5 = 28


2 _x_ 1 + 5 _x_ 2 + 5 _x_ 3 + _x_ 6 = 30


_x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 6 constant

maximize 1 2 1 0 0 0 0


constraint 2 1 1 1 0 0 14


constraint 4 2 3 0 1 0 28


constraint 2 5 5 0 0 1 30


146


_Introduction to Algorithms and Machine Learning_


From the array, we can tell that _x_ 2 has the largest slope since it has the

largest entry in the top row. To find the row that places the strictest

constraint on _x_ 2 _,_ we just divide the constant column by the _x_ 2 column:


_x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 6 constant constraint

maximize 1 2 1 0 0 0 0 _−_


constraint 2 1 1 1 0 0 14 14 _/_ 1 = 14


constraint 4 2 3 0 1 0 28 28 _/_ 2 = 14


constraint 2 5 5 0 0 1 30 30 _/_ 5 = 6


The bottom row places the strictest constraint. To execute the trade,


we perform elementary row operations using the bottom row to kill off

the rest of the _x_ 2 column. (That is, we divide the bottom row so that

the entry in the _x_ 2 column becomes 1 _,_ and then we subtract multiples

of the bottom row from the other rows.)


_x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 6 constant

maximize 0 _._ 2 0 _−_ 1 0 0 _−_ 0 _._ 4 _−_ 12 _←_ max is 12


constraint 1 _._ 6 0 0 1 0 _−_ 0 _._ 2 8


constraint 3 _._ 2 0 1 0 1 _−_ 0 _._ 4 16


constraint 0 _._ 4 1 1 0 0 0 _._ 2 6


This matches up with the system that we got after the first iteration


when we worked out the algebra (shown below). The only catch is that


the _−_ 12 in the “constant” column really means that we’ve reached a

maximum of _positive_ 12 _._ (This happens because the constant column

usually represents the constant once it’s been moved to the other side


147


_Justin Skycak_


of the equality sign, but there is no equality sign in the expression that


we’re trying to maximize.)



maximize 12 + [1]




[1]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [2] 5



5 _[x]_ [6]



_x_ 4 = 8 _−_ [8]




[8] [1]

5 _[x]_ [1][ +] 5



5 _[x]_ [6]



_x_ 5 = 16 _−_ [16]




[2]
5 _[x]_ [1] _[ −]_ _[x]_ [3][ +] 5



5 _[x]_ [6]



_x_ 2 = 6 _−_ [2]




[2]

5 _[x]_ [1] _[ −]_ _[x]_ [3] _[ −]_ [1] 5



5 _[x]_ [6]



0 _≤_ _x_ 1 _,_ _x_ 2 _,_ _x_ 3 _,_ _x_ 4 _,_ _x_ 5 _,_ _x_ 6


Remember that the array manipulations are just implementing algebra


thatwe’vealreadyworkedthrough,soifyougetconfusedorstuckwhen


implementing the simplex method, it will help to go back to the algebra


and make sure that every array manipulation you do matches up against


the algebra.

## **Exercises**


1 _._ Work out the example that was covered, using algebra, on paper.


2 _._ Write all the relevant array manipulations next to the algebra.


3 _._ Implement the simplex method in code. The input should be


the first array that you write down, and the output should be the


last array that you wrote down.


148


_Introduction to Algorithms and Machine Learning_


4 _._ Work out the array manipulations manually for the new system


shown below, and then ensure that your implementation gives


the same result. Note that when you are identifying the


strictest constraint, if you ever get a constraint of that involves a


comparison to a negative number, then you can discard it (since


we already know the variables are non-negative). This should


only require you to work out 3 iterations (i.e. your 4th guess will


be the final one).


maximize 20 _x_ 1 + 10 _x_ 2 + 15 _x_ 3 such that


3 _x_ 1 + 2 _x_ 2 + 5 _x_ 3 _≤_ 55


2 _x_ 1 + _x_ 2 + _x_ 3 _≤_ 26


_x_ 1 + _x_ 2 + 3 _x_ 3 _≤_ 30


5 _x_ 1 + 2 _x_ 2 + 4 _x_ 3 _≤_ 57


_x_ 1 _,_ _x_ 2 _,_ _x_ 3 _≥_ 0 _._


149


_Justin Skycak_


150


# **Part IV** **Regression and Classification**

151


_Justin Skycak_


152


# **23. Linear, Polynomial, and** **Multiple Linear Regression via** **Pseudoinverse**

**Supervised learning** consists of fitting functions to data sets. The idea

is that we have a sample of inputs and outputs from some process, and


we want to come up with a mathematical model that predicts what

the outputs would be for other inputs. Supervised _machine_ learning

involves programming computers to compute such models.

## **Linear Regression and the Pseudoinverse**


One of the simplest ways to construct a predictive algorithm is to


assume a linear relationship between the input and output. Even if


this assumption isn’t correct, it’s always useful to start with a linear


model because it provides a baseline against which we can compare


the accuracy of more complicated models. (We can only justify using


a complicated model if it is significantly more accurate than a linear


model.)


153


_Justin Skycak_


Forexample,let’s fita linearmodel _y_ = _mx_ + _b_ to the following data set.


Thatis,wewanttofindthevaluesof _m_ and _b_ sothattheline _y_ = _mx_ + _b_


most accurately represents the following data set.


[(0 _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


While there is no single line that goes through all three points in the


data set, we can choose the slope _m_ and intercept _b_ so that the line


represents the data as accurately as possible. There are a handful of


ways to accomplish this, the simplest of which involves leveraging the

_pseudoinverse_ from linear algebra.


To start, let’s set up the system of equations that would need to be


satisfied in order for our model to have perfect accuracy on the data


set. We do this by simply taking each point ( _x, y_ ) in our data set and


plugging it into the model _y_ = _mx_ + _b._


( _x, y_ ) _→_ _y_ = _m · x_ + _b_


(0 _,_ 1) _→_ 1 = _m ·_ 0 + _b_


(2 _,_ 5) _→_ 5 = _m ·_ 2 + _b_


(4 _,_ 3) _→_ 3 = _m ·_ 4 + _b_


154


_Introduction to Algorithms and Machine Learning_


Now, we rewrite the above system using matrix notation:











 _m ·_ 0 + _b_











1


5


3















1


5


3






 _→_



 _m ·_ 2 + _b_

_m ·_ 4 + _b_







0 1


2 1


4 1







 =



 =








- _m_


_b_



You may be tempted to solve the matrix equation by inverting the


coefficient matrix that’s multiplying the unknown:












_−_ 1





- _m_


_b_







=







0 1


2 1


4 1











1


5


3







Then you might remember that the inverse of a non-square matrix does


not exist, and think that this was all fruitless.


But really, this is the main idea of the pseudoinverse method. The only


difference is that before inverting the coefficient matrix, we multiply


both sides of the equation by the transpose of the coefficient matrix so


that it becomes square.


155


_Justin Skycak_



















1


5


3







0 1


2 1


4 1







 =








- _m_


_b_




- []








- []








0 2 4




0 2 4



1 1 1



 =








- _m_


_b_



1 1 1







1


5


3







0 1


2 1


4 1




- 22


9







=




20 6



6 3



��
_m_



_b_



Geometrically, multiplying by the transpose takes the matrices involved

in the equation and _projects_ them onto the nearest subspace where a

solution exists. This means we can now take the inverse:




- _m_




_m_








20 6



6 3




- _−_ 1 �
22



_b_



=



9







= [1]

24




3 _−_ 6



��
22



9



= [1]

24




_−_ 6 20


- 12


48



=




- 1 _/_ 2


2


156


_Introduction to Algorithms and Machine Learning_



Reading off the parameters _m_ = [1]



linear model:



2 [and] _[ b]_ [ = 2] _[,]_ [ we have the following]



_y_ = [1]

2 _[x]_ [ + 2]


## **Polynomial Regression**

We can use the pseudoinverse method to fit polynomial models as well.

Toillustrate,let’sfitaquadraticmodel _y_ = _ax_ [2] + _bx_ + _c_ tothefollowing


data set:


[(0 _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3) _,_ (5 _,_ 0)]


First, we set up our system of equations:


157


_Justin Skycak_


( _x, y_ ) _→_ _y_ = _a · x_ [2] + _b · x_ + _c_


(0 _,_ 1) _→_ 1 = _a ·_ 0 [2] + _b ·_ 0 + _c_


(2 _,_ 5) _→_ 5 = _a ·_ 2 [2] + _b ·_ 2 + _c_


(4 _,_ 3) _→_ 3 = _a ·_ 4 [2] + _b ·_ 4 + _c_


(5 _,_ 0) _→_ 0 = _a ·_ 5 [2] + _b ·_ 5 + _c_


Then we convert to a matrix equation, multiply both sides by the


transpose of the coefficient matrix, and invert the resulting square


matrix.


158


_Introduction to Algorithms and Machine Learning_



















1


5


3


0







 _a_











0 [2] 0 1

2 [2] 2 1

4 [2] 4 1

5 [2] 5 1







=








_b_


_c_


























0 [2] 2 [2] 4 [2] 5 [2]







1


5


3


0











0 [2] 0 1

2 [2] 2 1

4 [2] 4 1

5 [2] 5 1











=




0 [2] 2 [2] 4 [2] 5 [2]



 0 2 4 5

1 1 1 1



 _a_




























0 2 4 5


1 1 1 1



_b_


_c_



















68


22



 _a_











897 197 45


197 45 11


45 11 4







 =











_b_


_c_










9



 _a_




















_−_ 1




897 197 45


197 45 11


45 11 4







_b_


_c_






 =


_≈_















68


22


9
















_−_ 0 _._ 73



3 _._ 42


1 _._ 02







Note that we used a computer to simplify the final step. You can start


to see why computers are essential in machine learning (and this is just


the tip of the iceberg).


159


_Justin Skycak_


We have the following quadratic model:


_y_ _≈−_ 0 _._ 73 _x_ [2] + 3 _._ 42 _x_ + 1 _._ 02

## **Multiple Linear Regression**


Lastly, the pseudoinverse method can also be used to fit models


consisting of multiple input variables. For example, let’s fit a linear


model _z_ = _ax_ + _by_ + _c_ to the following data set:


[(0 _,_ 1 _,_ 50) _,_ (2 _,_ 5 _,_ 30) _,_ (4 _,_ 3 _,_ 20) _,_ (5 _,_ 1 _,_ 10)]


Here, we have two input variables, _x_ and _y._ Our output variable is _z._


160


_Introduction to Algorithms and Machine Learning_


As usual, we begin by setting up our system of equations:


( _x, y, z_ ) _→_ _z_ = _a · x_ + _b · y_ + _c_


(0 _,_ 1 _,_ 50) _→_ 50 = _a ·_ 0 + _b ·_ 1 + _c_


(2 _,_ 5 _,_ 30) _→_ 30 = _a ·_ 2 + _b ·_ 5 + _c_


(4 _,_ 3 _,_ 20) _→_ 20 = _a ·_ 4 + _b ·_ 3 + _c_


(5 _,_ 0 _,_ 10) _→_ 10 = _a ·_ 5 + _b ·_ 0 + _c_


Then we convert to a matrix equation, multiply both sides by the


transpose of the coefficient matrix, and invert the square matrix that


results.


161


_Justin Skycak_



















50


30


20


10







 _a_



_b_


_c_











0 1 1


2 5 1


4 3 1


5 0 1







=















































0 2 4 5


1 5 3 0


1 1 1 1



=




0 2 4 5


1 5 3 0


1 1 1 1







 _a_






















50


30


20


10















0 1 1


2 5 1


4 3 1


5 0 1







_b_


_c_



















190


260


110



 _a_



22 35 9



45 22 11


22 35 9


11 9 4















 =



_b_


_c_










 _a_












_−_ 7 _._ 74


_−_ 0 _._ 60


50 _._ 12


162












_−_ 1




45 22 11


22 35 9


11 9 4







_b_


_c_






 =


_≈_



22 35 9











190


260


110


















_Introduction to Algorithms and Machine Learning_


So, we have the following model which represents a plane in 3

dimensional space:


_z_ _≈−_ 7 _._ 74 _x −_ 0 _._ 60 _y_ + 50 _._ 12

## **When the Pseudoinverse Fails**


Note that the pseudoinverse method requires that the columns of the


coefficient matrix be independent. Otherwise,when we multiply by the


transpose,the resultis notguaranteedto be invertible. In particular,this


means that the number of parameters of the model that we want to fit


(i.e. the width of the coefficient matrix) should not exceed the number


of distinct data points in our data set (i.e. the height of the coefficent


matrix).


To illustrate what happens when the number of parameters of the


model exceeds the number of distinct data points, let’s trying to fit a


line _y_ = _mx_ + _b_ to a data set [(2 _,_ 3)] consisting of only a single point.


(The line has 2 parameters, _m_ and _b._ )


163


_Justin Skycak_


3 = _m ·_ 2 + _b_




- - - - [�] _m_
3 = 2 1







_b_




2



�� 3 =




2



1



�� - [�] _m_
2 1







1



_b_




- 6


3







=




4 2



2 1



��
_m_



_b_




- _−_ 1
does not exist




4 2



2 1



Although multiplying by the transpose gives us a square matrix, the


square matrix is notinvertible. This happens because there are infinitely


many lines that have pass through the point (2 _,_ 3) and therefore have


perfect accuracy on the data set.

## **General Formula**


Looking back at our work, we can write down the general procedure as


follows, where _y_ is the vector of outputs, _X_ is the coefficients matrix of


our system of equations, and _p_ is the vector of model parameters.


164


_Introduction to Algorithms and Machine Learning_


_y_ = _Xp_


_X_ _[T]_ _y_ = _X_ _[T]_ _Xp_


_p_ = ( _X_ _[T]_ _X_ ) _[−]_ [1] _X_ _[T]_ _y_


The _pseudoinverse_ of the matrix _X_ is defined by ( _X_ _[T]_ _X_ ) _[−]_ [1] _X_ _[T]_ _,_ as

shown in the last row of the general equation. To understand why this


quantity is called the pseudoinverse, first recall that if we attempt to


solve the equation _y_ = _Xp_ using the regular matrix, then we get a


solution of the form


_p_ = _X_ _[−]_ [1] _y._


The issue that we run into is that the regular inverse _X_ _[−]_ [1] usually does


not exist (because _X_ is usually a tall rectangular matrix, not a square


matrix). The best approximation of the solution is


_p_ = ( _X_ _[T]_ _X_ ) _[−]_ [1] _X_ _[T]_ _y,_


which takes a similar form to the previous equation, except that the

inverse _X_ _[−]_ [1] is replaced by the pseudoinverse ( _X_ _[T]_ _X_ ) _[−]_ [1] _X_ _[T]_ _._


165


_Justin Skycak_

## **Final Remarks**


Finally,notethatquantitativemodelsareusuallyreferredtoas _regression_

models when the goal is to predict some numeric value. This is

contrasted with _classification_ models, where the goal is to predict the

category or _class_ that best represents an input. So far, we have only

encountered regression models, but we will learn about classification


models soon.

## **Exercises**


Use the pseudoinverse method to fit the given model to the given data


set. Check your answer by sketching the resulting model on a graph


containing the data points and verifying that it visually appears to


capture the trend of the data. Remember that the model does not need


to actually pass through all the data points (this is usually impossible).


1 _._ Fit _y_ = _mx_ + _b_ to [(1 _,_ 0) _,_ (3 _, −_ 1) _,_ (4 _,_ 5)] _._


2 _._ Fit _y_ = _mx_ + _b_ to [( _−_ 2 _,_ 3) _,_ (1 _,_ 0) _,_ (3 _, −_ 1) _,_ (4 _,_ 5)] _._


3 _._ Fit _y_ = _ax_ [2] + _bx_ + _c_ to [( _−_ 2 _,_ 3) _,_ (1 _,_ 0) _,_ (3 _, −_ 1) _,_ (4 _,_ 5)] _._


4 _._ Fit _y_ = _ax_ [2] + _bx_ + _c_ to [( _−_ 3 _, −_ 4) _,_ ( _−_ 2 _,_ 3) _,_ (1 _,_ 0) _,_ (3 _, −_ 1) _,_


(4 _,_ 5)] _._


5 _._ Fit _y_ = _ax_ [3] + _bx_ [2] + _cx_ + _d_ to [( _−_ 3 _, −_ 4) _,_ ( _−_ 2 _,_ 3) _,_ (3 _, −_ 1) _,_


(1 _,_ 0) _,_ (4 _,_ 5)] _._


166


_Introduction to Algorithms and Machine Learning_


6 _._ Fit _z_ = _ax_ + _by_ + _c_ to [( _−_ 2 _,_ 3 _, −_ 3) _,_ (1 _,_ 0 _, −_ 4) _,_ (3 _, −_ 1 _,_ 2) _,_


(4 _,_ 5 _,_ 3)] _._


167


_Justin Skycak_


168


# **24. Regressing a Linear** **Combination of Nonlinear** **Functions via Pseudoinverse**

Previously, we learned how to use the pseudoinverse to fit linear


and polynomial models to data sets consisting of one or more input


variables. However, the pseudoinverse is even more general than that.

## **Worked Example**


For example, let’s fit the model


_y_ = _a_ sin _x_ + _b ·_ 2 _[x]_


to the following data set:


169


_Justin Skycak_


[(0 _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


Although the model is more complicated, the procedure for fitting it is


exactly the same. First, we set up our system:


( _x, y_ ) _→_ _y_ = _a ·_ sin _x_ + _b ·_ 2 _[x]_


(0 _,_ 1) _→_ 1 = _a ·_ sin 0 + _b ·_ 2 [0]


(2 _,_ 5) _→_ 5 = _a ·_ sin 2 + _b ·_ 2 [2]


(4 _,_ 3) _→_ 3 = _a ·_ sin 4 + _b ·_ 2 [4]


Then we convert to a matrix equation and multiply both sides by the


transpose of the coefficient matrix.











sin 0 2 [0]




_a_


_b_



1


5


3














sin 2 2 [2]

sin 4 2 [4]







 =




- []








- []




_a_


_b_











sin 0 sin 2 sin 4







1


5


3



sin 2 2 [2]



sin 0 2 [0]

sin 2 2 [2]

sin 4 2 [4]








sin 0 sin 2 sin 4



2 [0] 2 [2] 2 [4]



 =



2 [0] 2 [2] 2 [4]



Finally, we evaluate the expression involving the inverse using a


computer:


170


_Introduction to Algorithms and Machine Learning_



5



1


5


3




- []



2 [0] 2 [2] 2 [4]




- []



















- _a_


_b_



=


_≈_



sin 2 2 [2]



sin 0 2 [0]

sin 2 2 [2]

sin 4 2 [4]





















- 3 _._ 89


0 _._ 37




 sin 0 sin 2 sin 4




_−_ 1
  sin 0 sin 2 sin 4



2 [0] 2 [2] 2 [4]



We have the following model:


_y_ _≈_ 3 _._ 89 sin _x_ + 0 _._ 37(2) _[x]_

## **Pulling Functions Apart**


We can apply the pseudoinverse method to fit linear combinations of


general functions:


171


_Justin Skycak_


_y_ = _af_ ( _x_ ) + _bg_ ( _x_ ) + _ch_ ( _x_ ) + _. . ._


Note that we can sometimes simplify models into the general form


above even if they appear not to be of that form. For example, consider


the following crazy-looking model:


_√_

_bx_

_y_ = _[±]_ [2] _[a]_ [+] _[x][ ±]_

1 + _x_


By applying the rules of algebra, we can “pull apart” this model as


follows:



_√_

[2] _[a]_ [+] _[x]_ _[±]_

1 + _x_ [+] 1 +



_y_ = _[±]_ [2] _[a]_ [+] _[x]_



_bx_

1 + _x_



_√_

[2] _[a][ ·]_ [ 2] _[x]_

+ _[±]_
1 + _x_



= _[±]_ [2] _[a][ ·]_ [ 2] _[x]_



_b ·_ _[√]_ _x_

1 + _x_



2 _[x]_ _√_
= _±_ 2 _[a]_ _·_

1 + _x_ _[±]_



_√_
_x_
_b ·_
1 + _x_



_√_
Note that 2 _[a]_ and



_b_ are themselves constants, so this is in the desired



generalform. Let’s fitthis modelto the data setthatwe’ve been working


with:


[(0 _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


172


_Introduction to Algorithms and Machine Learning_


First, we set up our system:



_√_
_x_
_b ·_
1 + _x_



2 _[x]_ _√_
( _x, y_ ) _→_ _y_ = _±_ 2 _[a]_ _·_

1 + _x_ _[±]_



2 _[x]_ _√_

1 + _x_ _[±]_



2 [0] _√_
(0 _,_ 1) _→_ 1 = _±_ 2 _[a]_ _·_

1 + 0 _[±]_

2 [2] _√_
(2 _,_ 5) _→_ 5 = _±_ 2 _[a]_ _·_

1 + 2 _[±]_

2 [4] _√_
(4 _,_ 3) _→_ 3 = _±_ 2 _[a]_ _·_

1 + 4 _[±]_



2 [0] _√_

1 + 0 _[±]_

2 [2] _√_

1 + 2 _[±]_

2 [4] _√_

1 + 4 _[±]_



_√_



_b ·_


_b ·_


_b ·_



0 _√_
_→_ 1 = _±_ 2 _[a]_ _·_ 1 _±_
1 + 0



4
_→_ 1 = _±_ 2 _[a]_ _·_ [16]
1 + 4 5



_b ·_ 0



_√_



2
_→_ 1 = _±_ 2 _[a]_ _·_ [4]
1 + 2 3



_b ·_



_√_

2

3



_√_




[4] _√_

3 _[±]_




[16] _√_

5 _[±]_



_b ·_ [2]

5



Then we convert to a matrix equation and multiply both sides by the


transpose of the coefficient matrix.















1 0



_√_
_±_



_b_



1


5


3











 =







16 _/_ 5 2 _/_ 5



_√_
4 _/_ 3



2 _/_ 3











_±_ 2 _[a]_












_√_
_±_








1 4 _/_ 3 16 _/_ 5








1 0



2 _/_ 3



 =




1 4 _/_ 3 16 _/_ 5



_√_
0



2 _/_ 3 2 _/_ 5



_b_



_√_
0



2 _/_ 3 2 _/_ 5











_±_ 2 _[a]_







1


5


3







_√_
4 _/_ 3



16 _/_ 5 2 _/_ 5



173


_Justin Skycak_


Finally, we evaluate the expression involving the inverse using a


computer:



_√_
0



2 _/_ 3 2 _/_ 5
























_±_ 2 _[a]_












1 0




_−_ 1
 1 4 _/_ 3 16 _/_ 5



_√_
0



2 _/_ 3 2 _/_ 5



_√_
_±_



_b_













- 
_−_ 0 _._ 14


10 _._ 01




1 4 _/_ 3 16 _/_ 5













=


_≈_







_√_
4 _/_ 3



16 _/_ 5 2 _/_ 5



2 _/_ 3







1


5


3



We have the following model:



_√_

2 _[x]_ _x_
_y_ _≈−_ 0 _._ 14 _·_

1 + _x_ [+ 10] _[.]_ [01] _[ ·]_ 1 + _x_


174


_Introduction to Algorithms and Machine Learning_

## **Functions that Cannot be Pulled Apart**


Despite the example above, not every model can be fit using the


pseudoinverse method. For example, the model below cannot be fit


using the pseudoinverse because there are no rules ofalgebra thatwould


allow us to pull it apart:


_y_ = sin( _ax_ ) cos( _bx_ )

## **Functions of Multiple Inputs**


Finally,notethatallthediscussionabovealsogeneralizestofunctionsof


multiple inputs. For example, we can apply the pseudoinverse method


to fit any model of the following form:


_z_ = _af_ ( _x, y_ ) + _bg_ ( _x, y_ ) + _ch_ ( _x, y_ ) + _. . ._


To demonstrate how this works, let’s fit the model


_z_ = _ax_ sin _y_ + _by_ ln(1 + _x_ )


to the following data set:


175


_Justin Skycak_


[(0 _,_ 1 _,_ 50) _,_ (2 _,_ 5 _,_ 30) _,_ (4 _,_ 3 _,_ 20) _,_ (5 _,_ 1 _,_ 10)]


First, we set up our system:


( _x, y, z_ ) _→_ _z_ = _a · x_ sin _y_ + _b · y_ ln(1 + _x_ )


(0 _,_ 1 _,_ 50) _→_ 50 = _a ·_ 0 sin 1 + _b ·_ 1 ln(1 + 0) _→_ 50 = _a ·_ 0 + _b ·_ 0


(2 _,_ 5 _,_ 30) _→_ 30 = _a ·_ 2 sin 5 + _b ·_ 5 ln(1 + 2) _→_ 30 = _a ·_ 2 sin 5 + _b ·_ 5 ln 3


(4 _,_ 3 _,_ 20) _→_ 20 = _a ·_ 4 sin 3 + _b ·_ 3 ln(1 + 4) _→_ 20 = _a ·_ 4 sin 3 + _b ·_ 3 ln 5


(5 _,_ 1 _,_ 10) _→_ 10 = _a ·_ 5 sin 1 + _b ·_ 1 ln(1 + 5) _→_ 10 = _a ·_ 5 sin 1 + _b ·_ ln 6


Then we convert to a matrix equation and multiply both sides by the


transpose of the coefficient matrix.



50

30

20

10


50

30

20

10



�0 2 sin 5 4 sin 3 5 sin 1

0 5 ln 3 3 ln 5 ln 6


176



0 0

2 sin 5 5 ln 3

4 sin 3 3 ln 5

5 sin 1 ln 6






=






=

















- _a_

_b_







0 0

2 sin 5 5 ln 3

4 sin 3 3 ln 5

5 sin 1 ln 6









�0 2 sin 5 4 sin 3 5 sin 1

0 5 ln 3 3 ln 5 ln 6























- _a_

_b_






_Introduction to Algorithms and Machine Learning_


Finally, we evaluate the expression involving the inverse using a


computer:







50

30

20

10




_−_ 1

�0 2 sin 5 4 sin 3 5 sin 1

0 5 ln 3 3 ln 5 ln 6

































0 0

2 sin 5 5 ln 3

4 sin 3 3 ln 5

5 sin 1 ln 6




- _a_

_b_







=


_≈_




















- _−_ 0 _._ 13

4 _._ 93



�0 2 sin 5 4 sin 3 5 sin 1

0 5 ln 3 3 ln 5 ln 6







We have the following model:


_z_ _≈−_ 0 _._ 13 _x_ sin _y_ + 4 _._ 93 _y_ ln(1 + _x_ )


177


_Justin Skycak_

## **Exercises**


Use the pseudoinverse method to fit each model to the given data set.


Check your answer each time by sketching the resulting model on a


graph containing the data points and verifying that it visually appears


to capture the trend of the data.


1 _._ Fit _y_ = _a_ ln(1 + _x_ ) + _[b]_

_x_ [to][ [(1] _[,]_ [ 0)] _[,]_ [ (3] _[,][ −]_ [1)] _[,]_ [ (4] _[,]_ [ 5)]] _[.]_

2 _._ Fit _y_ = _[ax]_ [ +] _[ b]_ to [(1 _,_ 0) _,_ (3 _, −_ 1) _,_ (4 _,_ 5)] _._

2 _[x]_




_[√]_ 3
3 _._ Fit _y_ = _±_ 3 _[a]_ [+] _[x]_ _±_



_bx_ to [(1 _,_ 0) _,_ (3 _, −_ 1) _,_ (4 _,_ 5)] _._



4 _._ Fit _z_ = _axy_ [2] + _b_ _·_ 2 _[x]_ [+] _[y]_ to [( _−_ 2 _,_ 3 _, −_ 3) _,_ (1 _,_ 0 _, −_ 4) _,_ (3 _, −_ 1 _,_ 2) _,_


(4 _,_ 5 _,_ 3)] _._


178


# **25. Power, Exponential, and** **Logistic Regression via** **Pseudoinverse**

Previously, we learned that we can use the pseudoinverse to fit any


regression model that can be expressed as a linear combination of


functions. Unfortunately, there are a handful of useful models that

_cannot_ be expressed as a linear combination of functions. Here, we will

explore 3 of these models in particular.


Power regression: _y_ = _a · x_ _[b]_


Exponential regression: _y_ = _a · b_ _[x]_


1
Logistic regression: _y_ =
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


The techniques that we will learn for fitting these models will apply

more generally to any model that can be _transformed_ into a linear

combination of functions (where the parameters are the coefficients


in the linear combination).


179


_Justin Skycak_

## **Power and Exponential Regressions**


Power and exponential regressions are familiar algebraic functions,


so we will address them first. To transform a power or exponential


regression into a linear combination of functions, we can transform the


equation by taking the natural logarithm of both sides and applying the


laws of logarithms to pull apart the expression on the right-hand side:


Power regression


ln _y_ = ln     - _a · x_ _[b]_ [�] _→_ ln _y_ = ln _a_ + _b_ ln _x_


Exponential regression


ln _y_ = ln ( _a · b_ _[x]_ ) _→_ ln _y_ = ln _a_ + (ln _b_ ) _· x_


Let’s fit the power regression to the following data set.


[(1 _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


As usual, we set up the system of equations, convert it into a matrix


equation, and apply the pseudoinverse.


180


_Introduction to Algorithms and Machine Learning_


( _x, y_ ) _→_ ln _y_ = (ln _a_ ) _·_ 1 + _b ·_ ln _x_


(1 _,_ 1) _→_ ln 1 = (ln _a_ ) _·_ 1 + _b ·_ ln 1 _→_ 0 = (ln _a_ ) _·_ 1 + _b ·_ 0


(2 _,_ 5) _→_ ln 5 = (ln _a_ ) _·_ 1 + _b ·_ ln 2


(4 _,_ 3) _→_ ln 3 = (ln _a_ ) _·_ 1 + _b ·_ ln 4







0



1 0















1 ln 2


1 ln 4



ln 5







 =








- ln _a_


_b_



ln 3


- ln _a_


_b_



=


_≈_



0 ln 2 ln 4




- []



0








- [] 1 0




















- 0 _._ 35


0 _._ 79




1 1 1













_−_ 1
 1 1 1



0 ln 2 ln 4











1 ln 2


1 ln 4







ln 5


ln 3



So, we have the following model:


ln _y_ _≈_ 0 _._ 35 _·_ 1 + 0 _._ 79 _·_ ln _x_


By combining the logarithms and reversing the transformation that we

originally applied to the power regression _y_ = _a · x_ _[b]_ _,_ we can write the


above model in power regression form:


181


_Justin Skycak_


ln _y_ _≈_ 0 _._ 35 + 0 _._ 79 _·_ ln _x_


ln _y_ _≈_ ln( _e_ [0] _[.]_ [35] ) + ln _x_ [0] _[.]_ [79]


ln _y_ _≈_ ln 1 _._ 42 + ln _x_ [0] _[.]_ [79]


ln _y_ _≈_ ln 1 _._ 42 _x_ [0] _[.]_ [79]


_y_ _≈_ 1 _._ 42 _x_ [0] _[.]_ [79]

## **Danger: Unintentional Domain Constraints**


Notice that the data set we used above was slightly different from


the data set that we’ve used earlier in this chapter. We changed the _x_ 

coordinate 0 to a 1 in the first data point.


Earlier: [( **0** _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


Now: [( **1** _,_ 1) _,_ (2 _,_ 5) _,_ (4 _,_ 3)]


182


_Introduction to Algorithms and Machine Learning_


The reason why we modified the data set is that the earlier data set

exposes a limitation of the pseudoinverse method. We _can’t_ fit our

power regression model to the earlier data set, because the _x_ -coordinate


of 0 causes a catastrophic issue in our transformed power regression


equation.


To see what the issue is, let’s substitute the point (0 _,_ 1) into our


transformed power regression equation and see what happens:


( _x, y_ ) _→_ ln _y_ = (ln _a_ ) _·_ 1 + _b ·_ ln _x_


( **0** _,_ 1) _→_ ln 1 = (ln _a_ ) _·_ 1 + _b ·_ ln **0**


The quantity ln 0 is not defined, so 0 is not a valid input for _x._ By


transforming the equation, we unintentionally imposed a constraint


on the valid inputs _x._

## **Danger: Suboptimal Fit**


Unfortunately, this is not the only bad news. Even with our new


data set, which does not contain any points with an _x_ -value of 0 _,_

the pseudoinverse did _not_ give us the most accurate fit of the power

regression _y_ = _ax_ _[b]_ _._ It gave us the most accurate fit of the transformed

model ln _y_ = (ln _a_ ) _·_ 1 + _b ·_ ln _x,_ but this is _not_ the most accurate

fit of the original power regression even though the two equations are


mathematically equivalent.


183


_Justin Skycak_


To understand this more clearly, let’s consider an extreme example. If


we were to fit a power regression to the data set


[(0 _._ 001 _,_ 0 _._ 01) _,_ (2 _,_ 4) _,_ (3 _,_ 9)]


using the same method that we demonstrated above, then we would get


the following model:


_y_ _≈_ 2 _._ 89 _x_ [0] _[.]_ [82]


However, if we plot this curve along with the data, then it’s easy to see


that this is not the most accurate model. It doesn’t even curve the right

way! A hand-picked model as simple as _y_ = _x_ [2] would be vastly more


accurate.


184


_Introduction to Algorithms and Machine Learning_


The reason the pseudoinverse method gave us an inaccurate model is


that we transformed the model and data into a different space before


we applied the pseudoinverse:


_y_ = _a · x_ _[b]_ _→_ ln _y_ = (ln _a_ ) _·_ 1 + _b ·_ ln _x_


Inthespacethatthedatawastransformedto,itturnsoutthatthemodel

_y_ _≈_ 2 _._ 89 _x_ [0] _[.]_ [82] is more accurate than the model _y_ = _x_ [2] _._ To visualize


this, we can plot these two models along with the data in the space of


points (ln _x,_ ln _y_ ) _._


_y_ = 2 _._ 89 _x_ [0] _[.]_ [82] _→_ ln _y_ = ln 2 _._ 89 + 0 _._ 82 ln _x_


_y_ = _x_ [2] _→_ ln _y_ = 2 ln _x_


[(0 _._ 001 _,_ 0 _._ 01) _,_ (2 _,_ 4) _,_ (3 _,_ 9)] _→_ [(ln 0 _._ 001 _,_ ln 0 _._ 01) _,_ (ln 2 _,_ ln 4) _,_ (ln 3 _,_ ln 9)]


_≈_ [( _−_ 6 _._ 91 _, −_ 4 _._ 61) _,_ (0 _._ 69 _,_ 1 _._ 39) _,_ (1 _._ 10 _,_ 2 _._ 20)]


185


_Justin Skycak_


Indeed, ln _y_ = ln 2 _._ 89 + 0 _._ 82 ln _x_ is the most accurate model in the

space of points (ln _x,_ ln _y_ ) _,_ but it is _not_ the most accurate model in the

space of points ( _x, y_ ) _._


This is something to be cautious of whenever you transform a model


into a space where the pseudoinverse can be applied - you should


always check the function afterwards and verify that it is looks accurate


“enough” for your purposes.

## **Logistic Regression**


Soon, we will learn about other methods of fitting models that are


robust to this sort of issue. But for now, let’s end by discussing the


logistic function:


1
_y_ =
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


186


_Introduction to Algorithms and Machine Learning_


The logistic function has a range of 0 _<_ _y_ _<_ 1 _,_ and it is a common


choice of model when the goal is to predict a bounded quantity. For


example, probabilities are bounded between 0 and 1 _,_ and rating scales


(such as movie ratings) are often bounded between 1 _−_ 5 and 1 _−_ 10 _._


Let’s construct a real-life scenario in which to fit a logistic regression.


Suppose that a food critic has rated sandwiches on a scale of 1 _−_ 5 as


follows:


   - A roast beef sandwich with 1 slice of roast beef was given a rating


of 1 out of 5 _._


   - A roastbeefsandwichwith 2 slices ofroastbeefwas given a rating


of 1 out of 5 _._


   - A roastbeefsandwichwith 3 slices ofroastbeefwas given a rating


of 2 out of 5 _._


We will model the food critic’s rating as a function of the number of


slices of roast beef. Our data set will consist of points ( _x, y_ ) _,_ where _x_


represents the number of slices of roast beef and _y_ represents the food


critic’s rating.


[(1 _,_ 1) _,_ (2 _,_ 1) _,_ (3 _,_ 2)]


To model the rating, we can fit a logistic function and then round the


output to the nearest whole number. Since the rating scale is between


1 _−_ 5 and we are going to round the output of the logistic function, we


187


_Justin Skycak_


need to construct a logistic function with the range 0 _._ 5 _<_ _y_ _<_ 5 _._ 5 _._


We can do this as follows:


1
0 _<_ _[<]_ [ 1]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


5
0 _<_ _[<]_ [ 5]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


5
0 _._ 5 _<_ [+ 0] _[.]_ [5] _[ <]_ [ 5] _[.]_ [5]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


So, our goal is to fit the following model to the data set


[(1 _,_ 1) _,_ (2 _,_ 1) _,_ (3 _,_ 2)] _._


5
_y_ = [+ 0] _[.]_ [5]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


In order to fit the model using the pseudoinverse, we need to transform


it into a linear combination of functions. We do so by manipulating


the equation to isolate the _ax_ + _b_ :


188


_Introduction to Algorithms and Machine Learning_


5
_y_ = [+ 0] _[.]_ [5]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


5
_y −_ 0 _._ 5 =
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


5
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)] =
_y −_ 0 _._ 5


5
_e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)] =
_y −_ 0 _._ 5 _[−]_ [1]


           - 5           
_−_ ( _ax_ + _b_ ) = ln
_y −_ 0 _._ 5 _[−]_ [1]


     - 5     
_−_ ln = _ax_ + _b_
_y −_ 0 _._ 5 _[−]_ [1]


Now, we can proceed with the usual process of fitting our model using


the pseudoinverse.


      - 5      ( _x, y_ ) _→_ _−_ ln = _a · x_ + _b ·_ 1
_y −_ 0 _._ 5 _[−]_ [1]


      - 5      (1 _,_ 1) _→_ _−_ ln = _a ·_ 1 + _b ·_ 1 _→_ _−_ ln 9 = _a ·_ 1 + _b ·_ 1
1 _−_ 0 _._ 5 _[−]_ [1]

      - 5      (2 _,_ 1) _→_ _−_ ln = _a ·_ 2 + _b ·_ 1 _→_ _−_ ln 9 = _a ·_ 2 + _b ·_ 1
1 _−_ 0 _._ 5 _[−]_ [1]

      - 5      (3 _,_ 2) _→_ _−_ ln = _a ·_ 3 + _b ·_ 1 _→_ _−_ ln(7 _/_ 3) = _a ·_ 3 + _b ·_ 1
2 _−_ 0 _._ 5 _[−]_ [1]


189


_Justin Skycak_


















1 1


2 1


3 1












_−_ ln 9


_−_ ln 9






 =








_a_


_b_




_−_ ln(7 _/_ 3)


   -   _a_


_b_



=


_≈_



1 1 1




- []




- []



























_−_ 3 _._ 10




1 2 3













_−_ 1
 1 2 3



1 1 1




_−_ ln 9


_−_ ln 9







1 1


2 1


3 1








_−_ ln(7 _/_ 3)




0 _._ 67







So, we have the following model:


5
_y_ _≈_ [+ 0] _[.]_ [5]
1 + _e_ _[−]_ [(0] _[.]_ [67] _[x][−]_ [3] _[.]_ [10)]


Since we had to transform the model into a space where the


pseudoinverse can be applied, we need to check the function and verify


190


_Introduction to Algorithms and Machine Learning_


that it looks accurate enough for our purposes. Here, our regression


curve looks fairly accurate, so we will proceed to analyze it.


Now that we have a regression curve, we can use it to make predictions


about the data. For example, what rating would we expect the critic to


give a sandwich with 6 slices of roast beef? To answer this question, we


just plug _x_ = 6 into our model:


5
_y_ (6) _≈_ [+ 0] _[.]_ [5]
1 + _e_ _[−]_ [((0] _[.]_ [67)(6)] _[−]_ [3] _[.]_ [10)]


_≈_ 4 _._ 08


Our result of 4 _._ 08 rounds to 4 _._ So, according to our model, we predict


that the critic would give a rating of 4 to a sandwich that had 6 slices of


roast beef.

## **Exercises**


Use the pseudoinverse method to fit each model to the given data set.


Check your answer each time by sketching the resulting model on a


graph containing the data points and verifying that it visually appears


to capture the trend of the data.


1 _._ Fit a power regression _y_ = _a · x_ _[b]_ to [(1 _,_ 0 _._ 2) _,_ (2 _,_ 0 _._ 3) _,_ (3 _,_ 0 _._ 5)] _._


2 _._ Fit an exponential regression _y_ = _a · b_ _[x]_ to [(1 _,_ 0 _._ 2) _,_ (2 _,_ 0 _._ 3) _,_


(3 _,_ 0 _._ 5)] _._


191


_Justin Skycak_


1
3 _._ Fit a logistic regression _y_ = [to][ [(1] _[,]_ [ 0] _[.]_ [2)] _[,]_ [ (2] _[,]_ [ 0] _[.]_ [3)] _[,]_
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]

(3 _,_ 0 _._ 5)] _._


4 _._ Construct a logistic regression whose range is 0 _._ 5 _<_ _y_ _<_ 10 _._ 5


and fit it to [(1 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 5)] _._


192


# **26. Overfitting, Underfitting,** **Cross-Validation, and the** **Bias-Variance Tradeoff**

We have previously described a model as “accurate” when it appears


to match closely with points in the data set. However, there are issues


with this definition that we will need to remedy. In this section, we


will expose these issues and develop a more nuanced understanding of


model accuracy by way of a concrete example.

## **Overfitting and Underfitting**


Consider the following data set of points ( _x, y_ ) _,_ where _x_ is the number


of seconds that have elapsed since a rocket has launched and _y_ is the

height (in meters) of the rocket above the ground. The data is _noisy_,

meaning that there is some random error in the measurements.


193


_Justin Skycak_


[(0 _,_ 0) _,_ (1 _,_ 10) _,_ (2 _,_ 20) _,_ (3 _,_ 50) _,_ (4 _,_ 35) _,_ (5 _,_ 100) _,_


(6 _,_ 110) _,_ (7 _,_ 190) _,_ (8 _,_ 150) _,_ (9 _,_ 260) _,_ (10 _,_ 270)]


If we use the pseudoinverse to fit linear, quadratic, and 8th degree


polynomial regressions, we get the following results. (You should do


this yourself and verify that you get the same results.)


Linear: _y_ = 28 _._ 14 _x −_ 32 _._ 05


194


_Introduction to Algorithms and Machine Learning_


Quadratic: _y_ = 2 _._ 05 _x_ [2] + 7 _._ 68 _x −_ 1 _._ 36


8th degree: _y_ = _−_ 0 _._ 00778 _x_ [8] + 0 _._ 296666 _x_ [7] _−_ 4 _._ 575859 _x_ [6]


+ 36 _._ 618048 _x_ [5] _−_ 162 _._ 04318 _x_ [4] + 390 _._ 1833 _x_ [3]


_−_ 462 _._ 14466 _x_ [2] + 212 _._ 239681 _x −_ 0 _._ 087308


195


_Justin Skycak_


Note that we used more decimal places in the 8th degree polynomial


regressor because it is very sensitive to rounding. (If you round the


coefficients to 2 decimal places and plot the result, it will look wildly


different.)


As we can see from the graph, the 8th degree polynomial regressor


matchesclosestwiththepointsinthedataset. So,ifwedefine“accuracy”


as simply matching with points in the data set, then we’d say the 8th


degree polynomial is the most accurate.


However, this doesn’t pass the sniff test. In order to match up with the


points in the data set so well, the 8th degree polynomial has to curve


and contort itself in unrealistic ways between data points.


   - For example, between the last two points in the data set, the 8th


degree polynomialrises up andfalls down sharply. Didthe rocket


really rise up 100 meters and fall down 100 meters between the


9th and 10th seconds? Probably not.


   - Likewise, the 8th degree polynomial continues dropping sharply


after the 10th second and hits the _x_ -axis shortly after. Is the


rocket really plummeting to the ground? Based on the actual


data points, it seems unlikely.


So,wecan’tplacemuchtrustinthe 8thdegreepolynomial’spredictions.


The 8th degree polynomial thinks the relationship between _x_ and _y_ is


more complicated than it actually is. When this happens, we say that

the model **overfits** the data.


On the other hand, the linear regression does not capture the fact that


the data is curving upwards. It thinks the relationship between _x_ and


196


_Introduction to Algorithms and Machine Learning_


_y_ is _less_ complicated than it actually is. When this happens, we say that

the model **underfits** the data.


Based on the graph, the quadratic regressor looks the most accurate.


It captures the fact that the data is curving upwards, but it does not


contort itself in unrealistic ways between data points, and it does not


predict that the rocket is going to fall straight down to the ground


immediately after the 10th second. The quadratic regressor neither


overfits nor underfits. So, we can place more trust in its predictions.

## **The Need for Cross Validation**


The discussion above suggests that our definition of accuracy should


be based on how well a model predicts things, not how well it matches


up with the data set. So, we have a new definition of what it means for


a model to be accurate:


   - _Old (bad) definition:_ The closer a model matches up with points

in the data set, the more accurate it is.


   - _New (good) definition:_ The better a model predicts data points

that it hasn’t seen (i.e. were not used during the model fitting


procedure), the more accurate it is.


But how can we measure how well a model predicts data points that


it hasn’t seen, if we are fitting it on the entire data set? The answer is


surprisingly simple: when measuring the accuracy of a model, don’t


197


_Justin Skycak_


fit the model on the entire data set. Instead, carry out the following

procedure, known as **leave-one-out cross validation** :


1 _._ Remove a point from the data set.


2 _._ Fit the model to all points in the data set _except_ the point that we

removed.


3 _._ Check how accurately the model would have predicted the point


that we left out.


4 _._ Place the point back in the data set.


5 _._ Repeat steps 1 _−_ 4 for every point in the data set and add up

how much each prediction was “off” by. This is called the _cross-_

_validation error_ .


6 _._ The model with the lowest cross-validation error is the most


accurate, i.e. it does the best job of predicting real data points


that it has not seen before.


The phrase _leave-one-out_ refers to when we remove a point from the

data set. The phrase _cross validation_ refers to when we have the model

predict the point we removed: we’re _validating_ that the model still does

a good job of predicting points that it hasn’t already been fitted on. The

word _cross_ indicates that during our validation, we’re asking the model

to “cross over” from points it has seen, to points it has not seen.


198


_Introduction to Algorithms and Machine Learning_

## **Example: Cross Validation**


Let’s demonstrate the leave-one-out cross validation procedure by


computing the cross-validation error for linear, quadratic, and 8th


degree polynomial regression models on our rocket launch data set. We


should find that the quadratic regression has the lowest error, the linear


regression has slightly higher error, and the 8th degree polynomial has


significantly higher error.


The table below shows some of the intermediate steps for computing


the cross-validation error for linear regression. In each row of the table,


we remove a point from the data set, fit a linear regression model to


the remaining data, and then get the predicted _y_ -value by plugging the


_x_ -coordinate of the removed point into the model.


199


_Justin Skycak_



Removed



Predicted
Remaining Data Model
Point Y-Value



Y-Value



(0 _,_ 0)


(1 _,_ 10)


(2 _,_ 20)




- (1 _,_ 10) _,_ (2 _,_ 20) _,_ 
(3 _,_ 50) _,_ (4 _,_ 35) _,_ (5 _,_ 100) _,_

(6 _,_ 110) _,_ (7 _,_ 190) _,_ (8 _,_ 150) _,_

(9 _,_ 260) _,_ (10 _,_ 270)




- (0 _,_ 0) (1 _,_ 10) _,_ 
(3 _,_ 50) _,_ (4 _,_ 35) _,_ (5 _,_ 100) _,_

(6 _,_ 110) _,_ (7 _,_ 190) _,_ (8 _,_ 150) _,_

(9 _,_ 260) _,_ (10 _,_ 270)




- (0 _,_ 0) (2 _,_ 20) _,_ 
(3 _,_ 50) _,_ (4 _,_ 35) _,_ (5 _,_ 100) _,_

(6 _,_ 110) _,_ (7 _,_ 190) _,_ (8 _,_ 150) _,_

(9 _,_ 260) _,_ (10 _,_ 270)



_y_ = 30 _._ 27 _x −_ 47 _._ 0 _−_ 47 _._ 0


_y_ = 28 _._ 8 _x −_ 37 _._ 01 _−_ 8 _._ 21


_y_ = 28 _._ 0 _x −_ 30 _._ 88 25 _._ 12



... ... ... ...



(10 _,_ 270)




- (0 _,_ 0) (1 _,_ 10) _,_ (2 _,_ 20) _,_ 
(3 _,_ 50) _,_ (4 _,_ 35) _,_ (5 _,_ 100) _,_

(6 _,_ 110) _,_ (7 _,_ 190) _,_ (8 _,_ 150) _,_

(9 _,_ 260) _,_



_y_ = 26 _._ 76 _x −_ 27 _._ 91 239 _._ 69



Once we have all the predicted points, we can compare them to the


removedpoints andcompute the cross-validation error. Foreachrowin

thetable,wecomputethe _square_ ofthedifferencebetweenthepredicted

_y_ -value and the actual _y_ -value in the removed point.


200


_Introduction to Algorithms and Machine Learning_


( _x_ actual _, y_ actual) _y_ predicted ( _y_ predicted _−_ _y_ actual) [2]


(0 _,_ 0) _−_ 47 _._ 0 ( _−_ 47 _._ 0 _−_ 0) [2]


(1 _,_ 10) _−_ 8 _._ 21 ( _−_ 8 _._ 21 _−_ 10) [2]


(2 _,_ 20) 25 _._ 12 (25 _._ 12 _−_ 20) [2]

... ... ...


(10 _,_ 270) 239 _._ 69 (239 _._ 69 _−_ 270) [2]


Note that although it might feel more natural to take the absolute value


instead of the square when computing the total error, it’s conventional


to work with squared distances in machine learning and statistics


because squaring has more desirable mathematical properties. For


example, squaring is differentiable everywhere, whereas absolute value


is not (the graph of the absolute value function is not differentiable at


0).


Finally,we sum up all the individual squared errors to get the total cross
validation error. This sum of squared errors is also known as the _cross-_

_validated RSS (residual sum of squares)_ .


( _−_ 47 _._ 0 _−_ 0) [2] + ( _−_ 8 _._ 21 _−_ 10) [2] + (25 _._ 12 _−_ 20) [2] + _. . ._ + (239 _._ 69 _−_ 270) [2]


If we compute the cross-validation error for the linear, quadratic, and


8th degree polynomial regressors separately, then we get the following


results (rounded to the nearest integer). Note that these results were


generated via code, and there was no intermediate rounding like was


done while working out the example above. You should try to calculate


201


_Justin Skycak_


these cross-validation errors on your own and verify that your numbers


match up.


Model Cross-Validation Error


Linear 13 143


Quadratic 8 033


8th Degree 7 615 290


If you need to debug anything by hand and round intermediate results,


remember to keep many decimal places in the coefficients of the 8th


degree polynomial regressor. (If you use too few decimal places, then


the regressor will give wildly different results.)


The results are just as we expected:


   - The quadratic regressor has the lowest cross-validation error,


which means it is the most accurate model to use for this data set.


   - The linear regressor has sightly higher cross-validation error


because it slightly underfits the data (it doesn’t capture the fact


that the data is curving upwards).


   - The 8th degree polynomial has massively higher cross-validation


error because it massively overfits the data (it contorts itself


and overcomplicates things so much that it thinks the rocket is


plummeting to the ground).


202


_Introduction to Algorithms and Machine Learning_

## **Bias-Variance Tradeoff**


Finally, let’s build more intuition about why these results came out as


they did. It turns out that the total cross-validation error in our model


is the sum of two different types of error:




- total cross














�error due


to bias



+




- error due



to variance



validation error



=



Loosely speaking, error due to **bias** occurs if a model assumes too

much about the relationship being modeled. In our example, the


linear regressor had high error due to bias because it assumed that the


relationship was a straight line (whereas the data was actually curving


upwards a bit). The error due to bias comes from a model’s inability to


pass through all the points that are being used to fit it. A model with

high bias is too _rigid_ to capture some trends in the data, and therefore

_underfits_ the data.


On the other hand, error due to **variance** occurs if a model changes

drastically when fit to a different sample of data points from the same


data set. In our example, the 8th degree polynomial regressor had high


error due to variance. To see this, you should plot all the different 8th


degreeregressorsthatyou cameupwithduringyourleave-one-outcross


validation and observe that the graphs look quite different from one


another. This is bad because a model is supposed to pick up on the true


relationship underlying some data, and if the model changes its mind


significantly when it’s shown different samples of data from the same

data set, then we can’t trust it! A model with high variance is so _flexible_


203


_Justin Skycak_


that it reads too much into the relationship between points in the data


set and contorts itself in weird ways.


To build further intuition for bias and variance, it can help to


anthropomorphize a bit:


   - A high-bias model is dumb: it can’t comprehend the complexity


of the relationship in the data.


   - A high-variance model is paranoid: it thinks it’s seeing all sorts


of complicated relationships that just aren’t there.


Ideally, we would like to minimize error due to bias and error due


to variance. However, bias and variance are two sides of the same


coin: when one decreases, the other increases. By minimizing one, we


maximize the other. In particular:


   - By making the model less rigid (i.e. decreasing bias), we make the


model more flexible (i.e. increase variance).


   - By making the model less flexible (i.e. decreasing variance), we


make the model more rigid (i.e. increase bias).


This is known as the the **bias-variance** **tradeoff**, and it means that

we cannot simply minimize bias and variance independently. This is


why cross-validation is so useful: it allows us to compute and thereby


minimize the sum of error due to bias and error due to variance, so that


we may find the ideal tradeoff between bias and variance.


204


_Introduction to Algorithms and Machine Learning_

## **K-Fold Cross Validation**


In closing, note that although leave-one-out cross validation can take

a long time to run on large data sets, a similar procedure called _k_ **-fold**

**cross validation** can be used instead. Instead of removing one point at

a time, we shuffle the data set, break it up into _k_ parts (with each part


containing roughly the same number of points), and then remove one


of the parts each time. Each time, we predict the points in the part that


weleftout,andthen we addupallthe squarederrors. We usuallychoose


_k_ to be a small number (such as _k_ = 5) so that the cross validation


procedure runs fairly quickly.

## **Exercise**


Work out the computations that were outlined in the examples


above. Fit and compute leave-one-out cross validation error for linear,


quadratic, and 8th degree polynomials and verify that your results


match up with the examples.


205


_Justin Skycak_


206


# **27. Regression via Gradient** **Descent**

Gradient descent can be applied to fit regression models. In particular,


it can help us avoid the pitfalls that we’ve experienced when we attempt


to fit nonlinear models using the pseudoinverse.


Previously, we fit a power regression _y_ = _ax_ _[b]_ to the following data set


and got a result that was quite obviously not the most accurate fit.


[(0 _._ 001 _,_ 0 _._ 01) _,_ (2 _,_ 4) _,_ (3 _,_ 9)]


This time, we will use gradient descent to fit the power regression and


observe that our resulting model fits the data much better.

## **Model-Fitting as a Minimization Problem**


To fit a model using gradient descent, we just have to construct an


expression that represents the error between the model and the data


207


_Justin Skycak_


that it’s supposed to fit. Then, we can use gradient descent to minimize


that expression.


Torepresenttheerrorbetweenthemodelandthedatathatit’ssupposed

to fit, we can use the _residual sum of squares (RSS)_ . To compute the

RSS, we just add up the squares of the differences between the model’s


predictions and the actual data.


data point _→_ predicted _y_ -value vs data _y_ -value


( _x, y_ ) _→_ _ax_ _[b]_ vs _y_


(0 _._ 001 _,_ 0 _._ 01) _→_ _a ·_ (0 _._ 001) _[b]_ vs 0 _._ 01


(2 _,_ 4) _→_ _a ·_ 2 _[b]_ vs 4


(3 _,_ 9) _→_ _a ·_ 3 _[b]_ vs 9


Summing up the squared differences between the predicted _y_ -values


and the _y_ -values in the data, we get the following expression for the


RSS:


RSS =  - _a ·_ (0 _._ 001) _[b]_ _−_ 0 _._ 01�2 +  - _a ·_ 2 _[b]_ _−_ 4�2 +  - _a ·_ 3 _[b]_ _−_ 9�2


Now, this is a normal gradient descent problem. We choose an initial



guess for _a_ and _b_ and then use the partial derivatives _[∂]_ [RSS]




[RSS] _[∂]_ [RSS]

_∂a_ [and] _∂b_




[RSS]

_∂b_ [to]



repeatedly update our guess so that it results in a lower RSS.


Computing partial derivatives, we have the following:


208


_Introduction to Algorithms and Machine Learning_


_∂_ RSS

= 2     - _a ·_ (0 _._ 001) _[b]_ _−_ 0 _._ 01� (0 _._ 001) _[b]_
_∂a_

+ 2      - _a ·_ 2 _[b]_ _−_ 4� _·_ 2 _[b]_


+ 2      - _a ·_ 3 _[b]_ _−_ 9� _·_ 3 _[b]_


_∂_ RSS

= 2     - _a ·_ (0 _._ 001) _[b]_ _−_ 0 _._ 01� _· a ·_ (0 _._ 001) _[b]_ ln(0 _._ 001)
_∂b_

+ 2      - _a ·_ 2 _[b]_ _−_ 4� _· a ·_ 2 _[b]_ ln 2


+ 2      - _a ·_ 3 _[b]_ _−_ 9� _· a ·_ 3 _[b]_ ln 3

## **Worked Example**


Let’s start with the initial guess _⟨a_ 0 _, b_ 0 _⟩_ = _⟨_ 1 _,_ 1 _⟩_ _,_ which corresponds

to the straight line _y_ = 1 _x_ [1] _._ Our gradient is




     - _∂_ RSS
_∇_ RSS( _a_ 0 _, b_ 0) =
_∂a_ _[, ][∂]_ [RSS] _∂b_



�����( _a_ 0 _,b_ 0)



= _⟨−_ 44 _._ 000018 _, −_ 45 _._ 095095 _⟩_ _,_


and using learning rate _α_ = 0 _._ 001 our updated guess is


_⟨a_ 1 _, b_ 1 _⟩_ = _⟨a_ 0 _, b_ 0 _⟩−_ _α∇_ RSS( _a_ 0 _, b_ 0)


= _⟨_ 1 _,_ 1 _⟩−_ (0 _._ 001) _⟨−_ 44 _._ 000018 _, −_ 45 _._ 095095 _⟩_


= _⟨_ 1 _._ 044000 _,_ 1 _._ 045095 _⟩_ _._


209


_Justin Skycak_


If we continue the process, we get the results shown in the table below.


_n_ _⟨an, bn⟩_ _∇_ RSS( _an, bn_ ) �� RSS( _an, bn_ )

0 _⟨_ 1 _,_ 1 _⟩_ _⟨−_ 44 _._ 000018 _, −_ 45 _._ 095095 _⟩_ �� 40 _._ 000081

1 _⟨_ 1 _._ 044000 _,_ 1 _._ 045095 _⟩_ _⟨−_ 43 _._ 610529 _, −_ 46 _._ 794623 _⟩_ �� 35 _._ 998548

2 _⟨_ 1 _._ 087611 _,_ 1 _._ 091890 _⟩_ _⟨−_ 42 _._ 948407 _, −_ 48 _._ 155772 _⟩_ �� 31 _._ 88666

3 _⟨_ 1 _._ 130559 _,_ 1 _._ 140045 _⟩_ _⟨−_ 41 _._ 947662 _, −_ 49 _._ 053128 _⟩_ �� 27 _._ 719376

50 _⟨_ 1 _._ 450958 _,_ 1 _._ 640770 _⟩_ _⟨_ 0 _._ 849948 _, −_ 0 _._ 569792 _⟩_ �� 0 _._ 315108

100 _⟨_ 1 _._ 410093 _,_ 1 _._ 668529 _⟩_ _⟨_ 0 _._ 783786 _, −_ 0 _._ 539881 _⟩_ �� 0 _._ 266312

500 _⟨_ 1 _._ 185035 _,_ 1 _._ 836774 _⟩_ _⟨_ 0 _._ 378140 _, −_ 0 _._ 307757 _⟩_ �� 0 _._ 061737

1000 _⟨_ 1 _._ 065472 _,_ 1 _._ 939139 _⟩_ _⟨_ 0 _._ 137242 _, −_ 0 _._ 123755 _⟩_ �� 0 _._ 008426

5000 _⟨_ 1 _._ 000014 _,_ 1 _._ 999987 _⟩_ _⟨−_ 0 _._ 000029 _, −_ 0 _._ 000028 _⟩_ �� 0 _._ 000100

10000 _⟨_ 1 _._ 000000 _,_ 2 _._ 000000 _⟩_ _⟨_ 0 _._ 000000 _,_ 0 _._ 000000 _⟩_ �� 0 _._ 000100


Our gradient descent converged to _a_ = 1 and _b_ = 2 _,_ which

corresponds to the function _y_ = 1 _x_ [2] _._ As we can see from the graph


below, this is a very good fit.


210


_Introduction to Algorithms and Machine Learning_

## **Sigma Notation and Implementation**


Note that when implementing gradient descent on a data set consisting


of more than a few points, it becomes infeasible to hard-code the entire


expression forthe RSS gradient. Instead,it becomes necessary to write a


function thatloopsthroughthepointsin thedatasetandincrementally


adds up each point’s individual contribution to the total RSS gradient.


It also becomes convenient to re-use intermediate values when possible.


To think through this, it’s helpful to express the RSS and its gradient


using sigma notation. In the example above, the RSS is given by




    RSS =


( _x,y_ ) _∈_ data


and its gradient is computed as


211




- _ax_ _[b]_ _−_ _y_ �2 _,_


_Justin Skycak_


_∇_ RSS = - _∇_ - _ax_ _[b]_ _−_ _y_ �2


( _x,y_ ) _∈_ data


=   - 2   - _ax_ _[b]_ _−_ _y_   - _∇_   - _ax_ _[b]_ _−_ _y_   

( _x,y_ ) _∈_ data




 - 2 - _ax_ _[b]_ _−_ _y_ - [�] _∂_ - _ax_ _[b]_ _−_ _y_ - _,_ _[∂]_

_∂a_
( _x,y_ ) _∈_ data




 =




_[∂]_ - _ax_ _[b]_ _−_ _y_ - [�]

_∂b_



= - 2 - _ax_ _[b]_ _−_ _y_ �� _x_ _[b]_ _, ax_ _[b]_ ln _x_ 

( _x,y_ ) _∈_ data


= - 2 - _ax_ _[b]_ _−_ _y_ - _x_ _[b]_ _⟨_ 1 _, a_ ln _x⟩_ _._


( _x,y_ ) _∈_ data



Nowthatwe’ve workedoutthe sigma notation,we can write a function


that mirrors it:





212


_Introduction to Algorithms and Machine Learning_

## **Debugging with Central Difference** **Quotients**


Lastly, note that when debugging broken gradient descent code, it can


be helpful to check your partial derivatives against difference quotient


approximations to ensure that you’re computing the partial derivatives


correctly:



RSS

_≈_ [RSS][(] _[a]_ [ +] _[ h, b]_ [)] _[ −]_ [RSS][(] _[a][ −]_ _[h, b]_ [)]
_∂a_ 2 _h_


RSS

_≈_ [RSS][(] _[a, b]_ [ +] _[ h]_ [)] _[ −]_ [RSS][(] _[a, b][ −]_ _[h]_ [)]
_∂b_ 2 _h_



_∂_ RSS



2 _h_



_∂_ RSS



2 _h_



where 0 _< h ≪_ 1 is a small positive number.


_Do not abuse difference quotients and attempt to use them to fully bypass_

_gradient computations._ Use difference quotients _only_ for debugging.

Difference quotients will be too slow to effectively train more advanced


models (such as neural networks), and it’s useful to practice gradient


computations on simpler models before moving on to more advanced


models.


213


_Justin Skycak_

## **Exercises**


Use gradient descent to fit the following models. Be sure to plot your


model on the same graph as the data to ensure that the fit is looks


reasonable.


1 _._ Implement the example that was worked out above.


2 _._ Fit _y_ = _ax_ [2] + _bx_ + _c_ to [(0 _._ 001 _,_ 0 _._ 01) _,_ (2 _,_ 4) _,_ (3 _,_ 9)] _._ Verify

that gradient descent gives the _same_ fit as compared to using the

pseudoinverse.


5
3 _._ Fit _y_ = [+] [0] _[.]_ [5] [to] [[(1] _[,]_ [ 1)] _[,]_ [ (2] _[,]_ [ 1)] _[,]_ [ (3] _[,]_ [ 2)]] _[.]_ [Verify]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]

that gradient descent gives a _better_ fit as compared to using the

pseudoinverse.


4 _._ Fit _y_ = _a_ sin _bx_ + _c_ sin _dx_ to




(0 _,_ 0) _,_ (1 _, −_ 1) _,_ (2 _,_ 2) _,_ (3 _,_ 0) _,_ (4 _,_ 0)







(5 _,_ 2) _,_ (6 _, −_ 4) _,_ (7 _,_ 4) _,_ (8 _,_ 1) _,_ (9 _, −_ 3)


214



_._


# **28. Multiple Regression and** **Interaction Terms**

In many real-life situations, there is more than one factor that controls


the quantity we’re trying to predict. That is to say, there is more than


one input variable that controls the output variable.

## **Example: Multiple Input Variables**


Forexample,suppose thata foodmanufacturing company is testing out


different ingredients on sandwiches, including peanut butter and roast


beef. They fed sandwiches to subjects and counted the proportion of


subjects who liked each sandwich.


215


_Justin Skycak_



scoops


peanut butter



scoops


jelly



slices


beef



proportion


subjects liked



0 0 0 0 _._ 0


1 0 0 0 _._ 2


2 0 0 0 _._ 5


0 1 0 0 _._ 4


0 2 0 0 _._ 6


0 0 1 0 _._ 5


0 0 2 0 _._ 8


1 1 0 1 _._ 0


1 0 1 0 _._ 0


0 1 1 0 _._ 1


We want to build a model that has 3 input variables:


_x_ 1 = scoops peanut butter


_x_ 2 = scoops jelly


_x_ 3 = slices beef


The model will predict 1 output variable:


_y_ = proportion subjects liked


Since this output variable must be between 0 and 1 _,_ we will use logistic


regression.


216


_Introduction to Algorithms and Machine Learning_


1
_y_ =
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]


The logistic model above is written with only a single input variable.


Here, we have 3 different input variables, so we will introduce a new


term for each input variable:


1
_y_ =
1 + _e_ _[−]_ [(] _[a]_ [1] _[x]_ [1][+] _[a]_ [2] _[x]_ [2][+] _[a]_ [3] _[x]_ [3][+] _[b]_ [)]


We should also introduce terms that represent interactions between the


variables, but to keep things simple and illustrate why such terms are


needed, let’s continue without them.


If we fit the above model to our data set by running gradient descent


a handful of times with different initial guesses and choosing the best


result, we get the following fitted model:


1
_y_ =
1 + _e_ _[−]_ [(0] _[.]_ [79] _[x]_ [1][+1] _[.]_ [13] _[x]_ [2][+0] _[.]_ [75] _[x]_ [3] _[−]_ [1] _[.]_ [72)]

## **The Need for Interaction Terms**


This model makes the following predictions. Some of them seem


accurate, but others do not.


217


_Justin Skycak_



scoops


peanut butter



scoops


jelly



slices


beef



proportion

prediction
subjects liked



0 0 0 0 _._ 0 0 _._ 15 ✓


1 0 0 0 _._ 2 0 _._ 28 ✓


2 0 0 0 _._ 5 0 _._ 47 ✓


0 1 0 0 _._ 4 0 _._ 36 ✓


0 2 0 0 _._ 6 0 _._ 63 ✓


0 0 1 0 _._ 5 0 _._ 27 _×_


0 0 2 0 _._ 8 0 _._ 44 _×_


1 1 0 1 _._ 0 0 _._ 55 _×_


**1** **0** **1** **0** _._ **0** **0** _._ **46** _×_


0 1 1 0 _._ 1 0 _._ 54 _×_


The weirdest inaccurate prediction (bolded above) is that the model


overrates peanut butter & roast beef sandwiches. It thinks that half of


the subjects will like them, when in reality, none of the subjects did.


And if you try to imagine that combination of ingredients, it probably


doesn’t seem appetizing.


The problem is that our model is not sophisticated enough to capture


the idea that two ingredients can taste good alone but bad together (or


vice versa). It’s easy to see why this is:


1

   - The logistic function [is increasing if] _[ a]_ _[>]_ [0][ and]
1 + _e_ _[−]_ [(] _[ax]_ [+] _[b]_ [)]

decreasing if _a <_ 0 _._


   - The coefficient on _x_ 1 (peanut butter) is _a_ 1 = 1 _._ 02 and the

coefficient on _x_ 3 (roast beef) is _a_ 3 = 1 _._ 91 _._


218


_Introduction to Algorithms and Machine Learning_


   - Both of these coefficients are positive. Consequently, the higher

_x_ 1 (the more scoops of peanut butter), the higher the prediction

will be. Likewise, the higher _x_ 3 (the more slices of roast beef), the

higher the prediction will be.

## **Interaction Terms**


To fix this, we can add **interaction terms** that multiply two variables

together. These terms will vanish unless both variables are nonzero.


1
_y_ =
1 + _e_ _[−]_ [(] _[a]_ [1] _[x]_ [1][+] _[a]_ [2] _[x]_ [2][+] _[a]_ [3] _[x]_ [3][+] _[a]_ [12] _[x]_ [1] _[x]_ [2][+] _[a]_ [13] _[x]_ [1] _[x]_ [3][+] _[a]_ [23] _[x]_ [2] _[x]_ [3][+] _[b]_ [)]


The interaction terms above are _a_ 12 _x_ 1 _x_ 2 _, a_ 13 _x_ 1 _x_ 3 _,_ and _a_ 23 _x_ 2 _x_ 3 _._ The

subscripts indicate which variables are being multiplied together.


Notice that, for example, the interaction term _a_ 13 _x_ 1 _x_ 3 will _not_ have

an effect on the predictions for _x_ 1 (peanut butter) or _x_ 3 (roast beef) in

isolation,but it _will_ have an effect when these ingredients are combined.


If we fit this model again using gradient descent, we get the following


result:


1
_y_ =
1 + _e_ _[−]_ [(1] _[.]_ [02] _[x]_ [1][+1] _[.]_ [34] _[x]_ [2][+1] _[.]_ [91] _[x]_ [3][+3] _[.]_ [82] _[x]_ [1] _[x]_ [2] _[−]_ [4] _[.]_ [82] _[x]_ [1] _[x]_ [3] _[−]_ [3] _[.]_ [34] _[x]_ [2] _[x]_ [3] _[−]_ [2] _[.]_ [11)]


Now, the model makes much more accurate predictions.


219


_Justin Skycak_



scoops


peanut butter



scoops


jelly



slices


beef



proportion

prediction
subjects liked



0 0 0 0 _._ 0 0 _._ 11 ✓


1 0 0 0 _._ 2 0 _._ 25 ✓


2 0 0 0 _._ 5 0 _._ 48 ✓


0 1 0 0 _._ 4 0 _._ 32 ✓


0 2 0 0 _._ 6 0 _._ 64 ✓


0 0 1 0 _._ 5 0 _._ 45 ✓


0 0 2 0 _._ 8 0 _._ 85 ✓


1 1 0 1 _._ 0 0 _._ 98 ✓


1 0 1 0 _._ 0 0 _._ 02 ✓


0 1 1 0 _._ 1 0 _._ 10 ✓


Asasanitycheck,wecanalsointerpretthecoefficientsoftheinteraction


terms:


   - The interaction term between _x_ 1 (peanut butter) and _x_ 2 (jelly)

is 3 _._ 82 _x_ 1 _x_ 2 _._ The _positive_ coefficient indicates that combining

peanut butter and jelly should _increase_ the prediction.


   - The interaction term between _x_ 1 (peanut butter) and _x_ 3 (roast

beef) is _−_ 4 _._ 82 _x_ 1 _x_ 3 _._ The _negative_ coefficient indicates that

combining peanut butter and roast beef should _decrease_ the

prediction.


   - The interaction term between _x_ 2 (jelly) and _x_ 3 (roast beef) is

_−_ 3 _._ 34 _x_ 2 _x_ 3 _._ The _negative_ coefficient indicates that combining

jelly and roast beef should _decrease_ the prediction.


220


_Introduction to Algorithms and Machine Learning_


Intuitively, this all makes sense. Peanut butter & jelly go together, but


peanut butter & roast beef do not go together, and nor do jelly & roast


beef.

## **Exercise**


Implement the example that was worked out above.


221


_Justin Skycak_


222


# **29. K-Nearest Neighbors**

Until now, we have been focused on **regression** problems, in which

we predict an output quantity (that is often continuous). However,

in the real world, it’s even more common to encounter **classification**

problems, in which we predict an output class (i.e. category). For


example, predicting how much money a person will spend at a store


is a regression problem, whereas predicting which items the person will


buy is a classification problem.

## **K-Nearest Neighbors**


One of the simplest classification algorithms is called **k-nearest**

**neighbors** . Given a data set of points labeled with classes, the k-nearest

neighbors algorithm predicts the class of a new data point by


1 _._ finding the _k_ points in the data set that are nearest to the new


point (i.e. its _k_ nearest neighbors),


2 _._ finding the class that occurs most often in those _k_ points (also

known as the _majority class_ ), and


223


_Justin Skycak_


3 _._ and predicting that the new data point belongs to the majority


class of its _k_ nearest neighbors.


As a concrete example, consider the following data set. Each row


represents a cookie with some ratio of ingredients. If we know the


portion of ingredients in a new cookie, we can use the k-nearest


neighbors algorithm to predict which type of cookie it is.


Cookie Type Portion Butter Portion Sugar


Shortbread 0 _._ 15 0 _._ 2


Shortbread 0 _._ 15 0 _._ 3


Shortbread 0 _._ 2 0 _._ 25


Shortbread 0 _._ 25 0 _._ 4


Shortbread 0 _._ 3 0 _._ 35


Sugar 0 _._ 05 0 _._ 25


Sugar 0 _._ 05 0 _._ 35


Sugar 0 _._ 1 0 _._ 3


Sugar 0 _._ 15 0 _._ 4


Sugar 0 _._ 25 0 _._ 35


Let’s start by plotting the data. We’ll represent shortbread cookies


using filled circles and sugar cookies using open circles. The _x_ -axis will


measure the portion butter, while the _y_ -axis will measure the portion


sugar.


224


_Introduction to Algorithms and Machine Learning_


Supposewehaveacookierecipethatconsistsof 0 _._ 25 portionbutterand


0 _._ 3 portion sugar, and we want to predict whether this is a shortbread


cookie or a sugar cookie. First, we’ll identify the corresponding point


(0 _._ 25 _,_ 0 _._ 3) on our graph and label it with a question mark.


To identify the _k_ nearest neighbors of the unknown point, we can


draw the smallest circle around the unknown point such that the circle


contains _k_ other points from our data set.


225


_Justin Skycak_


The circle for _k_ = 1 is shown below. Since this nearest neighbor is a


sugar cookie, we predict that the unknown cookie is also a sugar cookie.


Using _k_ = 2 instead, we get the circle shown below. Notice that after


the first nearest neighbor, the next two nearest neighbors are the same


distance away from our unknown point, so we have to include both of


them in our circle. Consequently, using _k_ = 3 gives us the exact same


circle.


Now we have 3 nearest neighbors: 2 shortbread cookies and 1 sugar


cookie. As a result, the majority class is shorbtread, and we predict that


the unknown cookie is a shortbread cookie.


226


_Introduction to Algorithms and Machine Learning_


Using _k_ = 4 or _k_ = 5 _,_ we get the circle below. The nearest neighbors


are 4 shortbread cookies and 1 sugar cookie, so we predict that the


unknown cookie is a shortbread cookie.


Using _k_ = 6 or _k_ = 7 _,_ the nearest neighbors are 5 shortbread


cookies and 2 sugar cookies, so we predict that the unknown cookie


is a shortbread cookie.


227


_Justin Skycak_


Using _k_ = 8 _,_ the nearest neighbors are 5 shortbread cookies and 3


sugar cookies, so we predict that the unknown cookie is a shortbread


cookie.


Using _k_ = 9 or _k_ = 10 _,_ the nearest neighbors are 5 shortbread cookies


and 5 sugar cookies. There is a tie for the majority class, so we will break


the tie by choosing the class of nearest neighbors that has the lowest


total distance from the unknown point.


228


_Introduction to Algorithms and Machine Learning_


We compute the distances of the nearest neighbors as follows:


Cookie Type Point Distance From (0 _._ 25 _,_ 0 _._ 3)

Shortbread (0 _._ 15 _,_ 0 _._ 2) �(0 _._ 15 _−_ 0 _._ 25) [2] + (0 _._ 2 _−_ 0 _._ 3) [2] _≈_ 0 _._ 141

Shortbread (0 _._ 15 _,_ 0 _._ 3) �(0 _._ 15 _−_ 0 _._ 25) [2] + (0 _._ 3 _−_ 0 _._ 3) [2] = 0 _._ 1

Shortbread (0 _._ 2 _,_ 0 _._ 25) �(0 _._ 2 _−_ 0 _._ 25) [2] + (0 _._ 25 _−_ 0 _._ 3) [2] _≈_ 0 _._ 071

Shortbread (0 _._ 25 _,_ 0 _._ 4) �(0 _._ 25 _−_ 0 _._ 25) [2] + (0 _._ 4 _−_ 0 _._ 3) [2] = 0 _._ 1

Shortbread (0 _._ 3 _,_ 0 _._ 35) �(0 _._ 3 _−_ 0 _._ 25) [2] + (0 _._ 35 _−_ 0 _._ 3) [2] _≈_ 0 _._ 071

Sugar (0 _._ 05 _,_ 0 _._ 25) �(0 _._ 05 _−_ 0 _._ 25) [2] + (0 _._ 25 _−_ 0 _._ 3) [2] _≈_ 0 _._ 206

Sugar (0 _._ 05 _,_ 0 _._ 35) �(0 _._ 05 _−_ 0 _._ 25) [2] + (0 _._ 35 _−_ 0 _._ 3) [2] _≈_ 0 _._ 206

Sugar (0 _._ 1 _,_ 0 _._ 3) �(0 _._ 1 _−_ 0 _._ 25) [2] + (0 _._ 3 _−_ 0 _._ 3) [2] = 0 _._ 15

Sugar (0 _._ 15 _,_ 0 _._ 4) �(0 _._ 15 _−_ 0 _._ 25) [2] + (0 _._ 4 _−_ 0 _._ 3) [2] _≈_ 0 _._ 141

Sugar (0 _._ 25 _,_ 0 _._ 35) �(0 _._ 25 _−_ 0 _._ 25) [2] + (0 _._ 35 _−_ 0 _._ 3) [2] = 0 _._ 05


Then, we compute the total distance for each class of nearest neighbors:


Shortbread: 0 _._ 141 + 0 _._ 1 + 0 _._ 071 + 0 _._ 1 + 0 _._ 071 = 0 _._ 483


Sugar: 0 _._ 206 + 0 _._ 206 + 0 _._ 15 + 0 _._ 141 + 0 _._ 05 = 0 _._ 753


229


_Justin Skycak_


Since shortbread neighbors have a lower total distance from the


unknown point, we predict that the unknown cookie is a shortbread


cookie.

## **Choosing the Value of K**


Now that we’ve learned how to make a prediction for any particular


value of _k,_ the big question is: which value of _k_ should we use to make


the prediction?


The value of _k_ is a _parameter_ in k-nearest neighbors, just like

the degree is a _parameter_ in polynomial regression. To choose an

appropriate degree for a polynomial regression, we used leave-one-out


cross validation.


We can take the same approach here. The only difference is that


instead of computing the residual sum of squares (RSS),we can directly


compute the accuracy by dividing the number of correct classifications


by the number of total classifications.


230


_Introduction to Algorithms and Machine Learning_


Using leave-one-out cross validation with _k_ = 1 _,_ we get 4 correct


classifications out of 10 total classifications, giving us an accuracy of


4 _/_ 10 = 0 _._ 4 _._


Using leave-one-out cross validation with _k_ = 2 _,_ we get 5 correct


classifications, giving us an accuracy of 0 _._ 5 _._


231


_Justin Skycak_


Using leave-one-out cross validation with _k_ = 3 or _k_ = 4 _,_ we get an


accuracy of 0 _._ 8 _._


With _k_ = 5 _,_ we get an accuracy of 0 _._ 7 _._


232


_Introduction to Algorithms and Machine Learning_


With _k_ = 6 _, k_ = 7 _,_ or _k_ = 8 _,_ we get an accuracy of 0 _._ 5 _._


With _k_ = 9 _,_ we get an accuracy of 0 _._ (Every point has 4 nearest


neighbors of the correct class and 5 nearest neighbors of the incorrect


class, leading us to predict the incorrect class.)


233


_Justin Skycak_


We organize our results in the graph below. The best fit (highest


accuracy) occurred at _k_ = 3 and _k_ = 4 _,_ so those would be good values


of _k_ to use in our model.


When _k_ is too _low_, the model _overfits_ the data because it is too flexible

(i.e. too high variance). In the extreme case of _k_ = 1 _,_ the model only


looks to a single nearest neighbor,which leads it to place too much trust


in fine details (that could just be noise) instead of trying to understand


the overall trend.


On the other hand, when _k_ is too _high_, the model _underfits_ the data

because it is too rigid (i.e. too high bias). In the extreme case where _k_ is


equal to the number of points in the data set, the model totally ignores


any sort of detail and will instead predict whichever class occurs most


often in the data set.


In other words:


   - when _k_ is too low, the model relies too much on anecdotal


evidence, and


234


_Introduction to Algorithms and Machine Learning_


   - when _k_ is too high, the model is unable to look beyond


stereotypes.

## **Exercises**


1 _._ Implement the example that was worked out above. Start by


classifying the unknown point (0 _._ 25 _,_ 0 _._ 3) for various values of


_k,_ and then generate the leave-one-out cross validation curve.


2 _._ Construct a cross-validation curve for the following data


set, where we measure butter in cups and sugar in grams. The

highest accuracy on this data set should be _lower_ than the highest

accuracy on the original data set. Why does using different scales


for the variables cause worse performance? Run through the


algorithm by hand until you notice and can describe what’s


happening.


235


_Justin Skycak_


Cookie Type Cups Butter Grams Sugar


Shortbread 0 _._ 6 200


Shortbread 0 _._ 6 300


Shortbread 0 _._ 8 250


Shortbread 1 _._ 0 400


Shortbread 1 _._ 2 350


Sugar 0 _._ 2 250


Sugar 0 _._ 2 350


Sugar 0 _._ 4 300


Sugar 0 _._ 6 400


Sugar 1 _._ 0 350


3 _._ As demonstrated by the previous problem, k-nearest neighbors


models tend to perform worse when variables have different


scales. To ensure that variables are measured on the same scale,

it’s common to _normalize_ data before fitting models.


In particular, _min-max normalization_ involves computing the

minimum value of a variable, subtracting the minimum from all


values, computing the new maximum value, and then dividing


all values by that maximum. This ensures that the variable is


measured on a scale from 0 to 1 _._


Normalize the “Cups Butter” variable in the data set above using


min-max normalization. Then, do the same with the “Grams


Sugar” variable. Finally, construct a cross-validation curve for


the normalized data set and verify that the performance has


improved.


236


# **30. Naive Bayes**

**Naive Bayes** is a classification algorithm that is grounded in _Bayesian_

_probability_ . It involves choosing the class with the highest conditional

probability given the corresponding data point, assuming that all the


variables in the data set are independent from each other.

## **Deriving the Formula**


The derivation of the main formula is shown below: we apply Bayes’


formula, discard the denominator _P_ (point) since it doesn’t depend


on the class, and then express _P_ (point _|_ class) as a product since we’re


assuming that the variables in the point are independent.


237


_Justin Skycak_


class = arg max [ _P_ (class _|_ point)]
class







= arg max
class




- _P_ (point _|_ class) _P_ (class)
_P_ (point)



= arg max [ _P_ (point _|_ class) _P_ (class)]
class







= arg max
class


= arg max
class



��



_P_ (variable _|_ class) _P_ (class)

variables








           
  _P_ (class) _P_ (variable _|_ class)


variables



The quantities in the final expression can be computed directly from


our data set:


   - _P_ (class) is the numberofrecords in the class,dividedby the total


number of records.


   - _P_ (variable _|_ class) is the number of records in the class that have


a matching variable value,divided by the total number of records


in the class.

## **Example: Spam Detection**


Let’s walk through a simple concrete example in which we apply the


naive Bayes algorithm to the task of spam detection. Spam detection


is the canonical example for naive Bayes because it was one of the first


commercial successes of naive Bayes.


238


_Introduction to Algorithms and Machine Learning_


Suppose that you go through 10 emails in your inbox and keep track


of whether each email was a scam, along with whether it contained


grammatical errors or links to other websites.


Scam Errors Links


No No No


Yes Yes Yes


Yes Yes Yes


No No No


No No Yes


Yes Yes Yes


No Yes No


No No Yes


Yes Yes No


No No Yes


Now, you look at 4 new emails. We can use the naive Bayes algorithm


to predict whether each of these emails is a scam, based on whether it


contains errors or links.


Scam Errors Links


? No No


? Yes Yes


? Yes No


? No Yes


239


_Justin Skycak_


First, let’s consider the email with no errors and no links. We’ll start


by writing down the naive Bayes classification formula for this specific


situation:








           
  _P_ (class) _P_ (variable _|_ class)


variables



class = arg max
class



= arg max [ _P_ (class) _P_ (no errors _|_ class) _P_ (no links _|_ class)]
class


So, we have two quantities to compare:


_P_ (scam) _P_ (no errors _|_ scam) _P_ (no links _|_ scam)


vs


_P_ (no scam) _P_ (no errors _|_ no scam) _P_ (no links _|_ no scam)


Let’s compute each of the probabilities in the above quantities:


   - Of the 10 emails in the original data set, 4 are scams and 6 are


not scams. Therefore, we have



_P_ (scam) = [4]




[4] _P_ (no scam) = [6]

10 _[,]_ 10



10 _[.]_



240


_Introduction to Algorithms and Machine Learning_


- Of the 4 emails in the original data set that are scams, 0 have no


errors and 1 has no links. Therefore, we have



_P_ (no errors _|_ scam) = [0]



4 _[.]_




[0] _P_ (no links _|_ scam) = [1]

4 _[,]_ 4




- Of the 6 emails in the original data set that are not scams, 5 have


no errors and 3 have no links. Therefore, we have



_P_ (no errors _|_ no scam) = [5]



6 _[.]_




[5] _P_ (no links _|_ no scam) = [3]

6 _[,]_ 6



Substituting these probabilities into the 2 quantities we wish to


evaluate, we get


_P_ (scam) _P_ (no errors _|_ scam) _P_ (no links _|_ scam)



= [4]




[0] [1]

4 _[·]_ 4




[4] [0]

10 _[·]_ 4



4



= 0


vs


_P_ (no scam) _P_ (no errors _|_ no scam) _P_ (no links _|_ no scam)



= [6]




[6] [5]

10 _[·]_ 6




[5] [3]

6 _[·]_ 6



6



= [1]

4 _[.]_



241


_Justin Skycak_


The “no scam” quantity gave us a greater value, so we predict that the


email with no errors and no links is not a scam.


Quantity Scam Errors Links
Scam vs No Scam

0 vs [1] No No No

4

? Yes Yes


? Yes No


? No Yes


We can predict the next row in the same way:


_P_ (scam) _P_ (errors _|_ scam) _P_ (links _|_ scam)




[4] [4]

10 _[·]_ 4



4



= [4]




[4] [3]

4 _[·]_ 4



= [3]

10



vs


_P_ (no scam) _P_ (errors _|_ no scam) _P_ (links _|_ no scam)



= [6]




[6] [1]

10 _[·]_ 6




[1] [3]

6 _[·]_ 6



6



= [1]

20 _[.]_



This time, the “scam” quantity gave us a greater value, so we predict


that the email with errors and links is a scam.


242


_Introduction to Algorithms and Machine Learning_


Quantity Scam Errors Links
Scam vs No Scam

0 vs [1] No No No

4

3 1 Yes Yes Yes
10 [vs] 20

? Yes No


? No Yes


If we apply the naive Bayes algortithm to the remaining rows, we get


the following results:


Quantity Scam Errors Links
Scam vs No Scam

0 vs [1] No No No

4

3 1 Yes Yes Yes
10 [vs] 20

1 1 Yes Yes No
10 [vs] 20

0 vs [1] No No Yes

4


Finally, note that in the event of a tie (i.e. both quantities give the same


value), it is common to choose the class that occurred most frequently


in the data set.

## **Exercise**


Implement the example that was worked out above.


243


_Justin Skycak_


244


# **Part V** **Graphs**

245


_Justin Skycak_


246


# **31. Breadth-First and** **Depth-First Traversals**

Graphs show up all the time in computer science, so it’s important to


know how to work with them. For example, consider the following


graph:


At its core, this graph is just a list of edges. Each edge ( _a, b_ ) represents


a connection from node _a_ to node _b._


247


_Justin Skycak_




## **Graph Class**

Whenworkingwithgraphs,it’susuallyconvenientandefficienttoparse


edges into a `Graph` class that handles operations behind the scenes.





248


_Introduction to Algorithms and Machine Learning_

## **Breadth-First and Depth-First Traversals**


In addition to getting the children or parents of a particular node in


the graph, it’s common to need to traverse though the graph in various

ways. The two most common types of traversals are **breadth first** and

**depth first** .


A **breadth-first** traversal starts at a node and then visits its children,

its grandchildren, its great-grandchildren, and so on. Intuitively, it


proceeds outward from the root node in broad layers.


On the other hand, a **depth-first** traversal goes down the entire family

tree of a single child before going down the family tree of another child.


Intuitively, it proceeds outward from the root node in deep spikes.


249


_Justin Skycak_

## **Implementation via Queues and Stacks**


Take a momentto make sure you understandthe examples above before


reading on.


Breadth-first and depth-first traversals are simple to implement using

_queues_ and _stacks_ (respectively), which are list-like data structures that

follow specific conventions regarding the order in which items can be


loaded and unloaded.


   - In a _queue_, the first item loaded becomes the first item unloaded

(i.e. first-in-first-out, just like a line at the grocery store).


   - In a _stack_,the firstitem loadedbecomes the LAST item unloaded

(i.e. first-in-last-out, just like a stack of paper).


To generate a breadth-first traversal, the following algorithm can be


used:


Below is a concrete walkthrough showing how the algorithm above


generates a breadth-first traversal from root node 4.


250


_Introduction to Algorithms and Machine Learning_





251


_Justin Skycak_


Generating a depth-first traversal is almost exactly the same. The only


difference is that we use a stack instead of a queue. A concrete example


illustrating the difference between a stack and a queue is given below.


1 _._ With a queue, we load on the right and unload on the left. For


example, given a queue `[1,2]`, loading `3` gives `[1,2,3]` . If


we unload, the unloaded element is `1` and the remaining queue


is `[2,3]` .


2 _._ With a stack, we load on the right and unload on the right. For


example, given a stack `[1,2]`, loading `3` gives `[1,2,3]` . If


we unload, the unloaded element is `3` and the remaining stack


is `[1,2]` .


252


_Introduction to Algorithms and Machine Learning_

## **Time Complexity**


Becausebreadth-firstanddepth-firsttraversalsbothvisiteachnodeonce


and only once, they both have time complexity _O_ ( _n_ ) where _n_ is the


number of nodes in the graph.

## **Exercises**


Implement a `Graph` class with all the methods described above, and


make sure to test it on several different types of graphs. You can use


the graph shown here as one of your test cases, but you should also test


several significantly different cases (e.g. cycles,an instance of two arrows


pointing the opposite way, a disconnected graph, etc).


253


_Justin Skycak_


254


# **32. Distance and Shortest** **Paths in Unweighted Graphs**

The **distance** between two nodes in a graph is the fewest number of

edges that must be crossed to travel from one node to the other. A **path**

between two nodes is a sequence of nodes that can be traversed to get

from one node to the other, traveling along edges. The **shortest path**

is the path with the shortest distance.

## **Demonstration**


Below is a demonstration of distances and shortest paths in a particular


graph.


255


_Justin Skycak_

## **Implementation**


The key to implementing these methods is to first create a method


`graph.set_distance_and_previous(idx)` that does a breadth

first traversal from the node at the given index and sets the attributes


`node.distance` and `node.previous` for each node encountered


during the traversal.


256


_Introduction to Algorithms and Machine Learning_


1 _._ Start at the node whose index is `idx` .


2 _._ Inthebreadth-firsttraversal,you’llendupvisitingallthechildren


of that node, those children’s children, and so on.


3 _._ Whenever you add a child to the queue, set the child’s


`previous` attribute to be the parent node that the child is


coming from, and set the child’s `distance` attribute to be one


more than that parent’s distance.


4 _._ When this is all done, each node’s `distance` attribute will


represent its distance from the initial starting node, and each


node’s `previous` attribute will represent the node that comes


before it if you’re traveling to it on the shortest path.


Note that this will require you to write a `Node` class and create an


instance for every node in your graph. It’s best to do this at the very


beginning when you first initialize the graph.


distances and shortest paths between nodes:


257


_Justin Skycak_


   - `calc_distance(from_idx,` `to_idx)`


Simply return the `distance` attribute of the “to” node.


   - `calc_shortest_path(from_idx,` `to_idx)`


1 _._ Start at the “to” node and repeatedly go to the previous


node until you get to the “from” node.


2 _._ Keep track of all the nodes you visit (this is the shortest


path in reverse).


3 _._ Return the path in order from the “from” node to the


“to” node. (You’ll have to reverse the reversed path that you


found in the previous step.)

## **Exercises**


258


# **33. Dijkstra’s Algorithm for** **Distance and Shortest Paths in** **Weighted Graphs**

In a **weighted graph**, every edge is assigned a value called a **weight** .

## **Initializing a Weighted Graph**


For example, consider the following weighted graph:


259


_Justin Skycak_


A weighted graph can be initialized with a weights dictionary instead of


an edges list. The edges list just had a list of edges, whereas the weights


dictionarywillhaveitskeysasedgesanditsvaluesastheweightsofthose


edges.








## **Distance and Shortest Paths in Weighted** **Graphs**

In a weighted graph, the distance between two nodes is the sum of the


weights on the shortest path between them. For example, the distance

4 2 1
from node 8 to node 4 is 7 because the shortest path is 8 _→_ 0 _→_ 3 _→_


4 _._


8
In particular, notice that the shortest path is NOT 8 _→_ 4 because the


distance along this path is 8 _._


260


_Introduction to Algorithms and Machine Learning_




## **Dijkstra’s Algorithm for Distance**

The underlying algorithms for `calc_distance` and


`calc_shortest_path` are a bit more complicated for weighted


graphs than for unweighted graphs.


To implement `calc_distance(from_idx,` `to_idx)` we need to

use **Dijkstra’s** **algorithm**, which works by assigning each node an

initial guess for its distance and then repeatedly updating those guesses


until they actually represent the distances to those nodes.


1 _._ When setting initial guesses, the “from” node is assigned a


distance value of 0, and all other nodes are assigned distance


values of _∞_ (just use a large number like 9999999999).


2 _._ Set the `current_node` to be the “from” node.


261


_Justin Skycak_


3 _._ Loop through the `current_node` ’s unvisited children


and update their distances as `child.distance` `=`





4 _._ Update the `current_node` to be the _unvisited_ node with the

_smallest_ distance value (not necessarily a child node).


5 _._ If the ending node has not been visited yet, then return to step


3 _._


6 _._ Return the `distance` attribute of the “to” node.


Let’s demonstrate each iteration of Dijkstra’s algorithm when


computing the distance from node 8 to node 6 _._


First, we set the initial guesses for the distance values. Since we’re


starting at node 8 _,_ we already know that it’s a distance of 0 from itself.


All the other nodes get initial guesses of infinity.


262


_Introduction to Algorithms and Machine Learning_


Now, we visit node 8 (the “from” node) and update the distance values


on its children.


The next node we visit should be the unvisited node with the smallest


distance value. This would be node 0 _,_ whose distance value is 4 _._ We


visit this node and update the distance values on its unvisited children.


Again, we visit the unvisited node with the smallest distance value. This


time, it’s node 3 _._


263


_Justin Skycak_


Notice that when we update the distance values on its unvisited


children, node 4’s distance value decreases from 8 to 7 _._ Whenever a


distance value decreases like this,itmeans thatthe nodes we’ve traversed


contain a shorter path than a path we found earlier.


8
In our first iteration, we found a path 8 _→_ 4 with distance 8 _._ Now, we

4 2 1
found a path 8 _→_ 0 _→_ 3 _→_ 4 with distance 7 _._


As usual, we visit the unvisited node with the smallest distance value.


This time, we can visit either node 1 or node 4 (they are the unvisited


nodes with the smallest distance values). We’ll arbitrarily choose to visit


node 1 and update the distance values of its children.


264


_Introduction to Algorithms and Machine Learning_


We keep on repeating this same procedure until the “to” node (node 6)


has been visited.


265


_Justin Skycak_


266


_Introduction to Algorithms and Machine Learning_


We’ve visited node 6 _,_ and its distance value is 21 _._ This means that the


distance from node 8 to node 6 is 21 _._

## **Computing Shortest Paths via the** **Shortest-Path Tree**


But what is the specific shortest path from node 8 to node 6 that gives


us this distance of 21?


To find the shortest path, we first construct the **shortest-path**

**tree** by discarding any edge `(a,b)` whose weight does not

match the corresponding difference between distance values,


`b.distance` `-` `a.distance` .


267


_Justin Skycak_


Once we have the shortest-path tree, we’ve effectively reduced our


problem down to a problem that we’ve already solved: finding the


shortest path between two nodes in an unweighted graph.


Indeed, we can see that the shortest path from node 8 to node 6 in the


tree above is given by 8 _→_ 0 _→_ 3 _→_ 2 _→_ 5 _→_ 6 _._ And indeed, in the


weighted graph, the sum of weights along this path is 21 _._


268


_Introduction to Algorithms and Machine Learning_

## **Exercises**


sure to write tests.


269


_Justin Skycak_


270


# **34. Decision Trees**

A **decision tree** is a graphical flowchart that represents a sequence of

nested “if-then” decision rules. To illustrate, first recall the following


cookie data set that was introduced during the discussion of k-nearest


neighbors:


Cookie Type Portion Butter Portion Sugar


Shortbread 0 _._ 15 0 _._ 2


Shortbread 0 _._ 15 0 _._ 3


Shortbread 0 _._ 2 0 _._ 25


Shortbread 0 _._ 25 0 _._ 4


Shortbread 0 _._ 3 0 _._ 35


Sugar 0 _._ 05 0 _._ 25


Sugar 0 _._ 05 0 _._ 35


Sugar 0 _._ 1 0 _._ 3


Sugar 0 _._ 15 0 _._ 4


Sugar 0 _._ 25 0 _._ 35


The following decision tree was algorithmically constructed to classify


an unknown cookie as a shortbread cookie or sugar cookie based on its


portions of butter and sugar.


271


_Justin Skycak_

## **Using a Decision Tree**


To use the decision tree to classify an unknown cookie, we start at the


top of the tree and then repeatedly go downwards and left or right


depending on the values of _x_ and _y._


For example, suppose we have a cookie with 0 _._ 25 portion butter and


0 _._ 35 portion sugar. To classify this cookie, we start at the top of the tree


and then go


1 _._ right (butter _>_ 0 _._ 125) _,_


2 _._ right (sugar _>_ 0 _._ 325) _,_


3 _._ right (butter _>_ 0 _._ 2) _,_


272


_Introduction to Algorithms and Machine Learning_


4 _._ left (butter _≤_ 0 _._ 275) _,_


5 _._ left (sugar _≤_ 0 _._ 375) _,_


reaching the prediction that the cookie is a sugar cookie.

## **Classification Boundary**


Let’s take a look at how the decision tree classifies the points in our data


set:


We can visualize this in the plane by drawing the **classification**

**boundary**, shading the regions whose points would be classified as


273


_Justin Skycak_


shortbread cookies and keeping unshaded the regions whose points


would be classified as sugar cookies. Each dotted line corresponds to a

**split** in the tree.

## **Building a Decision Tree: Reducing** **Impurity**


The algorithm for building a decision tree is conceptually simple. The

goalistomakethesimplesttreesuchthattheleafnodes _pure_ inthesense

thattheyonlycontain data points from one class. So,we repeatedlysplit

_impure_ leaf nodes in the way that most quickly reduces the impurity.


Intuitively, a node has 0 impurity when all of its data points come from


one class. On the other hand, a node has maximum impurity when an


equal amount of its data points come from each class.


To quantify a node’s impurity, all we have to do is count up the


proportion _p_ of the node’s data points that are from one particular


274


_Introduction to Algorithms and Machine Learning_


class and then apply a function that transforms _p_ into a measure of


impurity.


   - If _p_ = 0 or _p_ = 1 _,_ then the node has no impurity since its data


points are entirely from one class.


   - If _p_ = 0 _._ 5 _,_ then thenodehasmaximum impuritysincehalfofits


data points come from one class and the other half comes from


the other class.


Graphically, our function should look like this:


Two commonly used functions that yield the above graph are **Gini**

**impurity**, defined as


_G_ ( _p_ ) = 1 _−_ _p_ [2] _−_ (1 _−_ _p_ ) [2] _,_


and **information entropy**, defined as


275


_Justin Skycak_


_H_ ( _p_ ) = _−p_ log2 _p −_ (1 _−_ _p_ ) log2(1 _−_ _p_ ) _._


Although these functions may initially look a little complicated, note


thattheirforms permitthem to be easilygeneralizedto situations where


we have more than two classes:


     _G_ = 1 _−_ _p_ [2] _i_


_i_


    _H_ = _−_ _pi_ log2 _pi,_

_i_


where _pi_ is the proportion of the _i_ th class. (In our situation we only

have two classes with proportions _p_ 1 = _p_ and _p_ 2 = 1 _−_ _p._ )

## **Worked Example: Split 0**


As we walk through the algorithm for building our decision tree, we’ll


use Gini impurity since it simplifies nicely in the case of two classes,


making it more amenable to manual computation:


_G_ ( _p_ ) = 1 _−_ _p_ [2] _−_ (1 _−_ _p_ ) [2]


= 2 _p_ (1 _−_ _p_ )


276


_Introduction to Algorithms and Machine Learning_


Initially, our decision tree is just a single root node, i.e. a "stump" with


no splits. It contains our full data set, shown below.

## **Worked Example: Split 1**


Remember that our goal is to repeatedly split _impure_ leaf nodes in

the way that most quickly reduces the impurity. To find the split that


most quickly reduces the impurity, we loop over all possible splits and


compare the impurity before the split to the impurity after the split.


The impurity before the split is the same for all possible splits, so we


will calculate it first. In the graph above there are 5 points that represent


shortbread cookies and 5 points that represent sugar cookies, so _p_ =
5 [1]
5 + 5 [=] 2 [and the impurity is computed as]


277


_Justin Skycak_




   - 1
_G_ before = _G_
2








 - 1
= 2
2


= 0 _._ 5 _._



��
1 _−_ [1]

2







Now, let’s find all the possible splits. To find the values of _x_ that could


be chosen for splits, we first find all the distinct values of _x_ that are hit


by points and put them in order:


_x_ = 0 _._ 05 _,_ 0 _._ 1 _,_ 0 _._ 15 _,_ 0 _._ 2 _,_ 0 _._ 25 _,_ 0 _._ 3


The possible splits along the _x_ -axis are the midpoints between


consecutive entries in the list above:


_x_ split = 0 _._ 075 _,_ 0 _._ 125 _,_ 0 _._ 175 _,_ 0 _._ 225 _,_ 0 _._ 275


Performing the same process for _y_ -coordinates, we get the following:


_y_ = 0 _._ 2 _,_ 0 _._ 25 _,_ 0 _._ 3 _,_ 0 _._ 35 _,_ 0 _._ 4


_y_ split = 0 _._ 225 _,_ 0 _._ 275 _,_ 0 _._ 325 _,_ 0 _._ 375


278


_Introduction to Algorithms and Machine Learning_


Let’s go through each possible split and measure the impurity after the


split. In general, the impurity after the split is measured as a weighted


average of the new leaf nodes resulting from the split:


impurity after = (portion data points in _≤_ node) _×_ (impurity of _≤_ node)


+ (portion data points in _>_ node) _×_ (impurity of _>_ node)


The formula above can be represented more concisely as


_G_ after = _p≤G≤_ + _p>G>._


_Possible Split: x_ split = 0 _._ 075


The _x_ _≤_ 0 _._ 05 node would be pure with 2 sugar cookies, giving an


impurity of


279


_Justin Skycak_




   - 0
_G≤_ = 2
2



��2

2




= 0 _._



On the other hand, the _x_ _>_ 0 _._ 05 node would contain 5 shortbread


cookies and 3 sugar cookies, giving an impurity of




   - 5��3
_G>_ = 2
8 8




= [30]

64 _[.]_



The _≤_ node would contain 2 points while the _>_ node would contain



8 points, giving proportions _p≤_ = [2]



10 _[.]_




[2] [=] [8]

10 [and] _[ p][>]_



Finally, the impurity after the split would be


_G_ after = _p≤G≤_ + _p>G>_




 - 2
=
10




- - 8
(0) +
10



��30

64







= 0 _._ 375 _._



280


_Introduction to Algorithms and Machine Learning_


_Possible Split: x_ split = 0 _._ 125



Repeating the same process, we have _p≤_ = [3]



10 [get we]



get the following impurities:




[3] [=] [7]

10 [and] _[ p][>]_




   - 0��3
_G≤_ = 2
3 3


   - 5��2
_G>_ = 2
7 7




= 0


= [20]

49




  - 3   -   - 7
_G_ after = (0) +
10 10


281



��20�

_≈_ 0 _._ 286 _._

49


_Justin Skycak_



_Possible Split: x_ split = 0 _._ 175




   - 2��4
_G≤_ = 2
6 6


   - 3��1
_G>_ = 2
4 4




= [16]

36




= [6]

16




  - 6 ��16
_G_ after =
10 36




- - 4 �� 6
+
10 16


282




_≈_ 0 _._ 417


_Introduction to Algorithms and Machine Learning_


_Possible Split: x_ split = 0 _._ 225




   - 3��4
_G≤_ = 2
7 7


   - 2��1
_G>_ = 2
3 3




= [24]

49




= [4]

9




  - 7 ��24
_G_ after =
10 49




- - 3
+
10


283



��4

9




_≈_ 0 _._ 476


_Justin Skycak_



_Possible Split: x_ split = 0 _._ 275




   - 4��5
_G≤_ = 2
9 9


   - 1��0
_G>_ = 2
1 1




= [40]

81


= 0




  - 9 ��40
_G_ after =
10 81




- - 1
+
10


284




(0) _≈_ 0 _._ 444


_Introduction to Algorithms and Machine Learning_


_Possible Split: y_ split = 0 _._ 225




   - 1��0
_G≤_ = 2
1 1


   - 4��5
_G>_ = 2
9 9




= 0


= [40]

81




  - 1   -   - 9
_G_ after = (0) +
10 10


285



��40

81




_≈_ 0 _._ 444


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 275




   - 2
_G≤_ = 2
3


   - 3
_G>_ = 2
7



��1

3


��4

7


��4

9




= [4]

9




= [4]




= [24]

49




= [24]




  - 3
_G_ after =
10




- - 7
+
10


286



��24

49




_≈_ 0 _._ 476


_Introduction to Algorithms and Machine Learning_


_Possible Split: y_ split = 0 _._ 325




   - 3��2
_G≤_ = 2
5 5


   - 2��3
_G>_ = 2
5 5




= [12]

25




= [12]

25




  - 5 ��12
_G_ after =
10 25




- - 5
+
10


287



��12

25




= 0 _._ 48


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 375




   - 4��4
_G≤_ = 2
8 8


   - 1��1
_G>_ = 2
2 2




= [32]

64




= [2]

4




  - 8 ��32
_G_ after =
10 64




- - 2
+
10


288



��2

4




= 0 _._ 5


_Introduction to Algorithms and Machine Learning_


_Best Split_


Remember that the initial impurity before splitting was _G_ before =

0 _._ 5 _._ Let’s compute how much each potential split would decrease the


impurity:


Split �� _G_ before _−_ _G_ after
_x_ split = 0 _._ 075 �� 0 _._ 5 _−_ 0 _._ 375 = 0 _._ 125

_x_ split = 0 _._ 125 �� 0 _._ 5 _−_ 0 _._ 286 = **0** _._ **214**

_x_ split = 0 _._ 175 �� 0 _._ 5 _−_ 0 _._ 417 = 0 _._ 083

_x_ split = 0 _._ 225 �� 0 _._ 5 _−_ 0 _._ 476 = 0 _._ 024

_x_ split = 0 _._ 275 �� 0 _._ 5 _−_ 0 _._ 444 = 0 _._ 056

_y_ split = 0 _._ 225 �� 0 _._ 5 _−_ 0 _._ 444 = 0 _._ 056

_y_ split = 0 _._ 275 �� 0 _._ 5 _−_ 0 _._ 476 = 0 _._ 024

_y_ split = 0 _._ 325 �� 0 _._ 5 _−_ 0 _._ 48 = 0 _._ 02

_y_ split = 0 _._ 375 �� 0 _._ 5 _−_ 0 _._ 5 = 0


According to the table above, the best split is _x_ split = 0 _._ 125 since it

decreasestheimpuritythemost. Weintegratethissplitintoourdecision


tree:


289


_Justin Skycak_


This decision tree can be visualized in the plane as follows:

## **Worked Example: Split 2**


Again, we repeat the process and split any impure leaf nodes in the tree.


There is exactly one impure leaf node ( _x_ _>_ 0 _._ 125) and it contains 5


shortbread and 2 sugar cookies, giving an impurity of




   - 5
_G_ before = _G_
7








 - 5
= 2
7



��2

7







_≈_ 0 _._ 408


To find the possible splits, we first find the distinct values of _x_ and _y_


that are hit by points in this node and put them in order:


290


_Introduction to Algorithms and Machine Learning_


_x_ = 0 _._ 15 _,_ 0 _._ 2 _,_ 0 _._ 25 _,_ 0 _._ 3


_y_ = 0 _._ 2 _,_ 0 _._ 25 _,_ 0 _._ 3 _,_ 0 _._ 35 _,_ 0 _._ 4


The possible splits are the midpoints between consecutive entries in the


list above:


_x_ split = 0 _._ 175 _,_ 0 _._ 225 _,_ 0 _._ 275


_y_ split = 0 _._ 225 _,_ 0 _._ 275 _,_ 0 _._ 325 _,_ 0 _._ 375


_Possible Split: x_ split = 0 _._ 175


Remember that we are only splitting the region covered by the _x_ _>_


0 _._ 125 node, which contains 7 data points. We can ignore the 3 data


points left of the hard dotted line, since they are not contained within


the node that we are splitting.


291


_Justin Skycak_




   - 2
_G≤_ = 2
3


   - 3
_G>_ = 2
4



��1

3


��1

4




= [6]

16




= [4]

9




= [4]




= [6]




- - 4
+
7



�� 6

16




  - 3
_G_ after =
7



��4

9



_Possible Split: x_ split = 0 _._ 225




   - 3
_G≤_ = 2
4


   - 2
_G>_ = 2
3



��1

4


��1

3




= [6]

16




= [6]




= [4]

9




= [4]




  - 4
_G_ after =
7



�� 6 - - 3

+

16 7


292



��4

9




_≈_ 0 _._ 405


_≈_ 0 _._ 405


_Introduction to Algorithms and Machine Learning_


_Possible Split: x_ split = 0 _._ 275




   - 4
_G≤_ = 2
6


   - 1
_G>_ = 2
1



��2

6


��0

1




= [16]

36




= [16]




= 0




  - 6
_G_ after =
7



��16� - 1

+

36 7


293




(0) _≈_ 0 _._ 381


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 225




   - 1��0
_G≤_ = 2
1 1


   - 4��2
_G>_ = 2
6 6




= 0


= [16]

36




  - 1
_G_ after =
7




- - 6
(0) +
7


294



��16

36




_≈_ 0 _._ 381


_Introduction to Algorithms and Machine Learning_


_Possible Split: y_ split = 0 _._ 275




   - 2
_G≤_ = 2
2


   - 3
_G>_ = 2
5



��0

2


��2

5




= 0


= [12]

25




  - 2
_G_ after =
7




- - 5
(0) +
7


295



��12

25




_≈_ 0 _._ 343


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 325




   - 3��0
_G≤_ = 2
3 3


   - 2��2
_G>_ = 2
4 4




= 0


= [8]

16




  - 3
_G_ after =
7




- - 4
(0) +
7


296



�� 8

16




_≈_ 0 _._ 286


_Introduction to Algorithms and Machine Learning_


_Possible Split: y_ split = 0 _._ 375




   - 4
_G≤_ = 2
5


   - 1
_G>_ = 2
2



��1

5


��1

2




= [8]

25




= [8]




= [1]

2




= [1]




  - 5
_G_ after =
7



�� 8 - - 2

+

25 7


297



��1

2




_≈_ 0 _._ 371


_Justin Skycak_


_Best Split_


The best split is _y_ split = 0 _._ 325 since it decreases the impurity the most.


Split �� _G_ before _−_ _G_ after
_x_ split = 0 _._ 175 �� 0 _._ 408 _−_ 0 _._ 405 = 0 _._ 003

_x_ split = 0 _._ 225 �� 0 _._ 408 _−_ 0 _._ 405 = 0 _._ 003

_x_ split = 0 _._ 275 �� 0 _._ 408 _−_ 0 _._ 381 = 0 _._ 027

_y_ split = 0 _._ 225 �� 0 _._ 408 _−_ 0 _._ 381 = 0 _._ 027

_y_ split = 0 _._ 275 �� 0 _._ 408 _−_ 0 _._ 343 = 0 _._ 065

_y_ split = 0 _._ 325 �� 0 _._ 408 _−_ 0 _._ 286 = **0** _._ **122**

_y_ split = 0 _._ 375 �� 0 _._ 408 _−_ 0 _._ 371 = 0 _._ 037


We integrate this split into our decision tree:


298


_Introduction to Algorithms and Machine Learning_


This decision tree can be visualized in the plane as follows:

## **Worked Example: Split 3**


Again, we repeat the process and split any impure leaf nodes in the tree.


There is exactly one impure leaf node ( _x >_ 0 _._ 125 _→_ _y_ _>_ 0 _._ 325) and


it contains 2 shortbread and 2 sugar cookies, giving an impurity of




   - 2
_G_ before = _G_
4








 - 2
= 2
4


= 0 _._ 5 _._



��2

4







To find the possible splits, we first find the distinct values of _x_ and _y_


that are hit by points in this node and put them in order:


299


_Justin Skycak_


_x_ = 0 _._ 15 _,_ 0 _._ 25 _,_ 0 _._ 3


_y_ = 0 _._ 35 _,_ 0 _._ 4


The possible splits are the midpoints between consecutive entries in the


list above:


_x_ split = 0 _._ 2 _,_ 0 _._ 275


_y_ split = 0 _._ 375


_Possible Split: x_ split = 0 _._ 2


Remember that we are only splitting the region covered by the _x_ _>_


0 _._ 125 _→_ _y_ _>_ 0 _._ 325 node,which contains 4 data points. We can ignore


the 6 data points outside of this region, since they are not contained


within the node that we are splitting.


300


_Introduction to Algorithms and Machine Learning_




   - 0
_G≤_ = 2
1


   - 2
_G>_ = 2
3



��1

1


��1

3




= 0


= [4]

9



��4

9




_≈_ 0 _._ 333




  - 1
_G_ after =
4




- - 3
(0) +
4



_Possible Split: x_ split = 0 _._ 275


      - 1
_G≤_ = 2
3


      - 1
_G>_ = 2
1



��2

3


��0

1




= [4]

9


= 0




  - 3
_G_ after =
4



��4

9




- - 1
+
4


301




(0) _≈_ 0 _._ 333


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 375


      - 1
_G≤_ = 2
2


      - 1
_G>_ = 2
2



��1

2


��1

2




= [2]

4




= [2]

4




  - 2
_G_ after =
4



��2

4




- - 2��2
+
4 4




= 0 _._ 5



_Best Split_


This time, there is a tie for the best split: _x_ split = 0 _._ 2 and _x_ split = 0 _._ 275

both decrease impurity the most.


Split �� _G_ before _−_ _G_ after
_x_ split = 0 _._ 2 �� 0 _._ 5 _−_ 0 _._ 333 = **0** _._ **167**

_x_ split = 0 _._ 275 �� 0 _._ 5 _−_ 0 _._ 333 = **0** _._ **167**

_y_ split = 0 _._ 375 �� 0 _._ 5 _−_ 0 _._ 5 = 0


302


_Introduction to Algorithms and Machine Learning_


When ties like this occur, it does not matter which split we choose. We

will arbitrarily choose the split that we encountered first, _x_ split = 0 _._ 2 _,_

and integrate this split into our decision tree:


This decision tree can be visualized in the plane as follows:


303


_Justin Skycak_

## **Worked Example: Split 4**


Again, we repeat the process and split any impure leaf nodes in the tree.


There is exactly one impure leaf node ( _x_ _>_ 0 _._ 125 _→_ _y_ _>_ 0 _._ 325 _→_


_x_ _>_ 0 _._ 2) and it contains 2 shortbread and 1 sugar cookie, giving an


impurity of




   - 2
_G_ before = _G_
3








 - 2
= 2
3



��1

3







_≈_ 0 _._ 444 _._


To find the possible splits, we first find the distinct values of _x_ and _y_


that are hit by points in this node and put them in order:


_x_ = 0 _._ 25 _,_ 0 _._ 3


_y_ = 0 _._ 35 _,_ 0 _._ 4


The possible splits are the midpoints between consecutive entries in the


list above:


_x_ split = 0 _._ 275


_y_ split = 0 _._ 375


304


_Introduction to Algorithms and Machine Learning_


_Possible Split: x_ split = 0 _._ 275




   - 1
_G≤_ = 2
2


   - 1
_G>_ = 2
1



��1

2


��0

1




= [2]

4


= 0




  - 2
_G_ after =
3



��2

4




- - 1
+
3


305




(0) _≈_ 0 _._ 333


_Justin Skycak_



_Possible Split: y_ split = 0 _._ 375


      - 1
_G≤_ = 2
2


      - 1
_G>_ = 2
1



��1

2


��0

1




= [2]

4


= 0




  - 2
_G_ after =
3



��2

4




- - 1�
+ (0) _≈_ 0 _._ 333
3



_Best Split_


Again, there is a tie for the best split: _x_ split = 0 _._ 275 and _y_ split = 0 _._ 375

both decrease impurity the most.


Split �� _G_ before _−_ _G_ after
_x_ split = 0 _._ 275 �� 0 _._ 444 _−_ 0 _._ 333 = **0** _._ **111**

_y_ split = 0 _._ 375 �� 0 _._ 444 _−_ 0 _._ 333 = **0** _._ **111**


306


_Introduction to Algorithms and Machine Learning_


We will arbitrarily choose the split that we encountered first, _x_ split =

0 _._ 275 _,_ and integrate this split into our decision tree:


This decision tree can be visualized in the plane as follows:

## **Worked Example: Split 5**


There is only one possibility for the next split, _y_ split = 0 _._ 375 _,_ so it may

be tempting to select it outright. But rememberthat we only want splits


307


_Justin Skycak_


that lead to a decrease in impurity. So, it’s still necessary to compute the


decrease in impurity before selecting this split.




   - 1
_G_ before = _G_
2








 - 1
= 2
2


= 0 _._ 5 _._



��1

2








   - 0
_G≤_ = 2
1


   - 1
_G>_ = 2
1



��1

1


��0

1




= 0


= 0




  - 1
_G_ after =
2




- - 1
(0) +
2




(0) = 0



Indeed, the impurity decreases by a positive amount


308


_Introduction to Algorithms and Machine Learning_


_G_ before _−_ _G_ after = 0 _._ 5 _−_ 0


= 0 _._ 5


_>_ 0 _,_


so we select the split and integrate it into our decision tree:


This decision tree can be visualized in the plane as follows:


309


_Justin Skycak_


No more splits are possible, so we’re done.

## **Early Stopping**


Note that when fitting decision trees, it’s common to stop splitting


early so that the tree doesn’t overfit the data. This is often achieved by


enforcing


   - a _maximum depth_ constraint (i.e. skip over any potential splits

that would cause the tree to become deeper than some number


of levels), or


   - a _minimum split size_ constraint (i.e. do not split any leaf node

that contains fewer than some number of data points).


These parameters constrain how far the decision tree can read into


the data, similar to how the degree parameter constrains a polynomial


regression model and how _k_ constrains a k-nearest neighbors model.


Also note that if we stop splitting early (or if the data set has duplicate


pointswithdifferentclasses),weendupwithimpureleafnodes. Insuch


cases, impure leaf nodes are considered to predict the majority class of


the data points they contain. If there is a tie, then we can go up a level


and use the majority class of the parent node.


310


_Introduction to Algorithms and Machine Learning_

## **Random Forests**


A common way to improve the performance ofdecision trees is to select


a bunch of random subsets of the data (each containing, say, 50%


the data), fit a separate decision tree on each random subset, and then

aggregate them together into a hive mind called a **random forest** . The

random forest makes its predictions by


1 _._ allowing each individual decision tree to vote (i.e. make its own


prediction), and then


2 _._ choosing whichever prediction received the most votes.


This general approach is called **bootstrap** **aggregating** or **bagging**

for short (because a random subset of the data is known as a _bootstrap_

_sample_ ). Bootstrap aggregating can be applied to any model, though

random forest is the most famous application.


311


_Justin Skycak_

## **Exercises**


1 _._ Implement the example that was worked out above.


2 _._ Construct a leave-one-out cross-validation curve where a


maximum depth constraint is varied between 1 and the number


of points in the data set. When the maximum depth is 1 _,_ the


resulting decision tree will contain only one node (a decision


“stump” that simply predicts the majority class), and the leave

one-out accuracy will be 0 (since there will be fewer points


in the class of the point that was left out). As usual, the


leave-one-out cross-validation curve should reach a maximum


somewhere between the endpoints (the endpoints correspond


to underfitting or overfitting).


3 _._ Construct a leave-one-out cross-validation curve where a


minimum split size constraint is varied between 1 and one more


than the number of points in the data set. It should look like


a horizontal reflection of the curve for the maximum depth


constraint because increasing the minimum split size has the


same pruning effect as decreasing the maximum depth.


4 _._ Construct a leave-one-out cross-validation curve for a random


forest, where the number of trees in the forest is varied and each


tree is trained on a random sample of 50% of the data. You


should see the performance increase and asymptote off with the


number of trees.


312


_Introduction to Algorithms and Machine Learning_


5 _._ Construct a data set that leads to a decision tree that looks like


the diagram shown below. Be sure to run your decision tree


construction algorithm on the data set to verify the result.


6 _._ Construct a data set that leads to a decision tree that looks like


the diagram shown below. Be sure to run your decision tree


construction algorithm on the data set to verify the result.


313


_Justin Skycak_


314


# **35. Introduction to Neural** **Network Regressors**

It’scommontorepresentmodelsvia _computationalgraphs_ . Forexample,

consider the following multiple logistic regression model:


1
_f_ ( _x_ ) =
1 + _e_ _[−]_ [(] _[a]_ [1] _[x]_ [1][+] _[a]_ [2] _[x]_ [2][+] _[b]_ [)]


This model can be represented by the following computation graph,


where


   - Σ = _a_ 1 _x_ 1 + _a_ 2 _x_ 2 + _b_ is the sum of products of lower-node

values and the edge weights, and


1

   - _σ_ (Σ) = [is the sigmoid function.]
1 + _e_ _[−]_ [Σ]


315


_Justin Skycak_

## **Hierarchy and Complexity**


Loosely speaking, the deeper or more “hierarchical” a computational


graph is, the more complex the model that it represents. For example,


considerthecomputationalgraphbelow,whichcontainsanextra“layer”


of nodes.


316


_Introduction to Algorithms and Machine Learning_


Whereas the first computational graph represented a simple model

_f_ ( _x_ 1 _, x_ 2) = _σ_ ( _a_ 1 _x_ 1 + _a_ 2 _x_ 2 + _b_ ) _,_ this second computational graph

represents a far more complex model:



+ _a_ 212 _σ_ ( _a_ 121 _x_ 1 + _a_ 122 _x_ 2 + _b_ 12)



+ _a_ 213 _σ_ ( _a_ 131 _x_ 1 + _a_ 132 _x_ 2 + _b_ 13)







_a_ 211 _σ_ ( _a_ 111 _x_ 1 + _a_ 112 _x_ 2 + _b_ 11)



_f_ ( _x_ 1 _, x_ 2) = _σ_














+ _b_ 21


The subscripts in the coefficients may look a little crazy, but there is a


consistent naming pattern:


   - _aℓij_ is the weight of the connection from the _j_ th node in the _ℓ_ th

layer to the _i_ th node in the next layer.


   - _bℓi_ is the weight of the connection from the bias node in the _ℓ_ th

layer to the _i_ th node in the next layer. (A **bias** **node** is a node

whose output is always 1 _._ )

## **Neural Networks**


A **neural** **network** is a type of computational graph that is loosely

inspired by the human brain. Each neuron in the brain receives


input electrical signals from other neurons that connect to it, and


the amount of signal that a neuron sends outward to the neurons it


connects to depends on the totalamountofelectricalsignalitreceives as


input. Each connection has a different strength, meaning that neurons


317


_Justin Skycak_


influence each other by different amounts. Additionally, neurons in


key information-processing parts of the brain are sometimes arranged


in layers.


Using neural network terminology, the computational graph above can


be described as a neural network with 3 layers:


1 _._ an **input layer** containing 2 linearly-activatedneurons anda bias

neuron,


2 _._ a **hidden layer** containing 3 sigmoidally-activated neurons and

a bias neuron, and


3 _._ an **output** **layer** containing a single sigmoidally-activated

neuron.


To say that a neuron is _sigmoidally-activated_ means that to get the

neuron’s output we apply a sigmoidal **activation function** _σ_ to the


318


_Introduction to Algorithms and Machine Learning_


neuron’s input. Remember that the input Σ is the sum of products


of lower-node values and the edge weights. By convention, a linear


activation function is the identity function (i.e. the output is the same


as the input).


Neural networks are extremely powerful models. In fact, the _universal_

_approximation_ _theorem_ states that given a continuous function _f_ :

[0 _,_ 1] _[n]_ _→_ [0 _,_ 1] and an acceptable error threshold _ϵ >_ 0 _,_ there exists a


sigmoidally-activated neural network with one hidden layer containing


a finite number of neurons such that the error between the _f_ and the


neural network’s output is less than _ϵ._

## **Example: Manually Constructing a Neural** **Network**


To demonstrate, let’s set up a neural network that models the following


data set:


[(0 _,_ 0) _,_ (0 _._ 25 _,_ 1) _,_ (0 _._ 5 _,_ 0 _._ 5) _,_ (0 _._ 75 _,_ 1) _,_ (1 _,_ 0)]


First,we’lldrawacurvethatapproximatesthedataset. Then,we’llwork


backwards to combine sigmoid functions in a way that resembles the


curve that we drew.


319


_Justin Skycak_


Loosely speaking, it appears that our curve can be modeled as the sum


of two humps.


Notice that we can create a hump by adding two opposite-facing


sigmoids (and shifting the result down to lie flat against the _x_ -axis):


320


_Introduction to Algorithms and Machine Learning_


_h_ ( _x_ ) = _σ_ ( _x_ + 1) + _σ_ ( _−x_ + 1) _−_ 1


Remember that our neural network repeatedly applies sigmoid


functions to sums ofsigmoidfunctions,so we’llhave to applya sigmoid


to the function above. The following composition will accomplish this


while shaping our hump to be the correct width:


_H_ ( _x_ ) = _σ_ (20 _h_ (10 _x_ ) _−_ 5)


Then, we can represent our final curve as the sum of two horizontally

shifted humps (again shifted downward to lie flat against the _x_ axis and


then wrapped in another sigmoid function).


321


_Justin Skycak_


_σ_ (20 _H_ ( _x −_ 0 _._ 25) + 20 _H_ ( _x −_ 0 _._ 75) _−_ 5)


Now, let’s work backwards from our final curve expression to figure


out the architecture of the corresponding neural network.


Our output node represents the expression


_σ_ (20 _H_ ( _x −_ 0 _._ 25) + 20 _H_ ( _x −_ 0 _._ 75) _−_ 5) _,_


sothepreviouslayershouldhavenodeswhoseoutputsare _H_ ( _x−_ 0 _._ 25) _,_


_H_ ( _x −_ 0 _._ 75) _,_ and 1 (the corresponding weights being 20 _,_ 20 _,_ and _−_ 5


respectively).


322


_Introduction to Algorithms and Machine Learning_


Expanding further, we have


_H_ ( _x −_ 0 _._ 25) = _σ_ (20 _h_ (10 _x −_ 2 _._ 5) _−_ 5)


= _σ_ (20( _σ_ (10 _x −_ 1 _._ 5) + _σ_ ( _−_ 10 _x_ + 3 _._ 5) _−_ 1) _−_ 5)


= _σ_ (20 _σ_ (10 _x −_ 1 _._ 5) + 20 _σ_ ( _−_ 10 _x_ + 3 _._ 5) _−_ 25)


_H_ ( _x −_ 0 _._ 75) = _σ_ (20 _h_ (10 _x −_ 7 _._ 5) _−_ 5)


= _σ_ (20( _σ_ (10 _x −_ 6 _._ 5) + _σ_ ( _−_ 10 _x_ + 8 _._ 5) _−_ 1) _−_ 5)


= _σ_ (20 _σ_ (10 _x −_ 6 _._ 5) + 20 _σ_ ( _−_ 10 _x_ + 8 _._ 5) _−_ 25) _,_


so the second-previous layer should have nodes whose outputs are


_σ_ (10 _x −_ 1 _._ 5) _, σ_ (10 _x −_ 6 _._ 5) _, σ_ ( _−_ 10 _x_ + 3 _._ 5) _, σ_ ( _−_ 10 _x_ + 8 _._ 5) _,_ and


1 _._ (In the diagram below, edges with weight 0 are represented by soft


dashed segments.)


323


_Justin Skycak_


We can now sketch our full neural network as follows:


324


_Introduction to Algorithms and Machine Learning_

## **Hierarchical Representation**


There is a clear hierarchical structure to the network. The first hidden


layer transforms the linear intput into sigmoidal functions. The second


hidden layer combines those sigmoids to generate humps. The output


layer combines humps into the desired output.


Hierarchical structure is ultimately the reason why neural networks


can fit arbitrary functions to such high degrees of accuracy. Loosely


speaking, each neuron in the network recognizes a different feature in


thedata,anddeeperlayersinthenetworksynthesizeelementaryfeatures


into more complex features.


325


_Justin Skycak_

## **Exercises**


1 _._ Reproduce the example above by plotting the regression curve


(as well as the data points).


2 _._ Tweak the neural network constructed in the discussion above


so that the output resembles the following curve:


326


_Introduction to Algorithms and Machine Learning_


3 _._ Tweak the neural network constructed in the discussion above


so that the output resembles the following curve. (Hint: shift the


equilibrium, flip one of the humps, and make the humps a little


narrower.)


4 _._ Tweak the neural network constructed in the discussion above


so that the output resembles the following curve. (Hint: put a


sharp peak on top of a wide plateau.)


327


_Justin Skycak_


328


# **36. Backpropagation**

The most common method used to fit neural networks to data is


gradient descent, just like we did have done previously for simpler


models. The computations are significantly more involved for neural

networks, but an algorithm called **backpropagation** provides a

convenient framework for computing gradients.

## **Core Idea**


The backpropagation algorithm leverages two key facts:


1 _._ If you know _[∂]_ [RSS]

_∂σ_ (Σ) [for the output] _[ σ]_ [(Σ)][ of a neuron, then you]



can easily compute _[∂]_ [RSS]



for any weight _w_ that the neuron
_∂w_



receives from a neuron in the previous layer.



2 _._ If you know _[∂]_ [RSS]

_∂σ_ (Σ) [forall neurons in a layer,then you can piggy-]



back off the result to compute _[∂]_ [RSS] [in] [the]

_∂σ_ (Σ) [for all neurons]

previous layer.


329


_Justin Skycak_


With these two facts in mind, the backpropagation algorithm consists


of the following three steps:


1 _._ _Forward_ _propagate_ _neuron_ _activities._ Compute Σ and _σ_ (Σ)

for all neurons in the network, starting at the input layer and


repeatedly piggy-backing off the results to compute Σ and _σ_ (Σ)


for all neurons in the next layer.


2 _._ _Backpropagate neuron output gradients._ Compute _[∂]_ [RSS]

_∂σ_ (Σ) [for all]

neurons,startingwiththeoutputlayerandthenrepeatedlypiggy
backing off the results to compute _[∂]_ [RSS]

_∂σ_ (Σ) [in the previous layer.]



3 _._ _Expand neuron output gradients to weight gradients._ Compute
_∂_ RSS



_∂w_ [for all weights in the neural network by piggy-backing off]



of _[∂]_ [RSS]



_∂σ_ (Σ) [for the neuron that receives the weight.]


## **Forward Propagation of Neuron Activities**

Let’s formalize these steps mathematically. First, we denote the


following quantities:










 are the inputs to the neural network, and _f_ ( _⃗x_ ) is the




- _⃗x_ =







_x_ 1

_x_ 2
...



output of the neural network.


330


_Introduction to Algorithms and Machine Learning_










 are the inputs to the neurons in the _ℓ_ th layer, and




- Σ _[⃗]_ _ℓ_ =


_⃗hℓ_ =







Σ _ℓ_ 1

Σ _ℓ_ 2
...



_hℓ_ 1

_hℓ_ 2
...














 aretheoutputsoftheneuronsinthe _ℓ_ thlayer. Ifthe




                  - _⃗_                   activation function of these neurons is _σ,_ then _[⃗]_ _hℓ_ = _σ_ Σ _ℓ_ _._


- The input layer is the 0th layer,there are _L_ hidden layers between


the input and output layers,and the output layer is the ( _L_ +1)th

layer. Note that this means _[⃗]_ _h_ 0 = _⃗x_ and _hL_ +1 = _f_ ( _⃗x_ ) _._





_aℓ_ 11 _aℓ_ 12 _· · ·_






 is the matrix of connection




- _Aℓ_ =



_aℓ_ 21 _aℓ_ 22 _· · ·_



... ... ...



weights between the non-bias neurons in the _ℓ_ th layer and the







next layer, and _[⃗]_ _bℓ_ =







_bℓ_ 1

_bℓ_ 2
...






 are the connection weights between



the bias neuron in the _ℓ_ th layer and the neurons in the next layer.


331


_Justin Skycak_


The following diagram may aid in remembering what each symbol


represents.


332


_Introduction to Algorithms and Machine Learning_


Using the terminology introduced above, we can state the forward


propagation step as follows:


_⃗_
Σ1 = _A_ 1 _⃗x_ + _⃗b_ 1


_⃗h_ 1 = _σ_ �Σ _⃗_ 1�


_⃗_
Σ2 = _A_ 2 _⃗h_ 1 + _⃗b_ 2

_⃗h_ 2 = _σ_ �Σ _⃗_ 2�


_⃗_
Σ3 = _A_ 3 _⃗h_ 2 + _⃗b_ 3

_⃗h_ 3 = _σ_ �Σ _⃗_ 3�

...


_⃗_
Σ _L_ = _AL⃗hL−_ 1 + _⃗bL_

_⃗hL_ = _σ_ �Σ _⃗_ _L_      

Σ _L_ +1 = _a_ ( _L_ +1)11 _hL_ 1 + _a_ ( _L_ +1)12 _hL_ 2 + _· · ·_ + _b_ ( _L_ +1)1


_f_ ( _⃗x_ ) = _σ_ (Σ _L_ +1)


Note that the last two lines are written as scalars since the output layer

contains only a single neuron, i.e. _the_ output neuron.


333


_Justin Skycak_

## **Backpropagation of Neuron Output** **Gradients**


Now, let’s formalize the backpropagation step for a point ( _⃗x, y_ ) _._ First,


wecomputethegradientwithrespecttotheoutputneuron. Remember


thattheoutputoftheoutputneuronis _f_ ( _⃗x_ ) _,_ whichcanalsobedenoted

as _h_ ( _L_ +1)1 since the output layer is the ( _L_ + 1)th layer.



_∂_ RSS _∂_
=
_∂h_ ( _L_ +1) _i_ _∂h_ ( _L_ +1) _i_


_∂_
=
_∂h_ ( _L_ +1) _i_



�( _f_ ( _⃗x_ ) _−_ _y_ ) [2][�]


�� _h_ ( _L_ +1) _i −_ _y_ �2 [�]



= 2          - _h_ ( _L_ +1) _i −_ _y_          

Then, we backpropagate to the previous layer.


334


_Introduction to Algorithms and Machine Learning_


_∂_ RSS _∂_ RSS

= _·_ _[∂h]_ [(] _[L]_ [+1)1]
_∂hLi_ _∂h_ ( _L_ +1)1 _∂hLi_



_∂_ RSS _∂_
= _·_
_∂h_ ( _L_ +1)1 _∂hLi_




- _σ_ �Σ( _L_ +1)1��



_∂_ RSS _∂_
= _σ_ _[′]_ [ �] Σ( _L_ +1)1� _·_
_∂h_ ( _L_ +1)1 _∂hLi_


_∂_ RSS _∂_
= _σ_ _[′]_ [ �] Σ( _L_ +1)1� _·_
_∂h_ ( _L_ +1)1 _∂hLi_



�Σ( _L_ +1)1�


_a_ ( _L_ +1)11 _hL_ 1 + _a_ ( _L_ +1)12 _hL_ 2
+ _· · ·_ + _b_ ( _L_ +1)1







_∂_ RSS
= _σ_ _[′]_ [ �] Σ( _L_ +1)1� _a_ ( _L_ +1)1 _i_
_∂h_ ( _L_ +1)1


_∂_ RSS
Note that the quantity was already computed, so we do not
_∂h_ ( _L_ +1)1

have to expand it out.


335


_Justin Skycak_


We continue backpropagating using the same approach. Note that


hidden layers contain multiple nodes (unlike the output layer), so we


need a term for each node.



_∂_ RSS
= _[∂]_ [RSS]
_∂h_ ( _L−_ 1) _i_ _∂hL_ 1



_∂hL_ 1

_[∂]_ [RSS] _·_ + _[∂]_ [RSS]

_∂hL_ 1 _∂h_ ( _L−_ 1) _i_ _∂hL_ 2



_∂hL_ 2

_[∂]_ [RSS] _·_ + _· · ·_

_∂hL_ 2 _∂h_ ( _L−_ 1) _i_



= _· · ·_



= _[∂]_ [RSS]



_σ_ _[′]_ (Σ _L_ 2) _aL_ 2 _i_ + _· · ·_
_∂hL_ 2




_[∂]_ [RSS] _σ_ _[′]_ (Σ _L_ 1) _aL_ 1 _i_ + _[∂]_ [RSS]

_∂hL_ 1 _∂hL_ 2



Again, note that the quantities _[∂]_ [RSS]




_[∂]_ [RSS] _,_ _[∂]_ [RSS]

_∂hL_ 1 _∂hL_ 2



_,_ _. . ._ were already
_∂hL_ 2



computed, so we do not have to expand them out.



Also note that we can consolidate into vector form:


336


_Introduction to Algorithms and Machine Learning_









_∂_ RSS

=
_∂_ _[⃗]_ _hL−_ 1


=


=


















_∂_ RSS
_∂h_ ( _L−_ 1)1
_∂_ RSS
_∂h_ ( _L−_ 1)2
...



_aL_ 11 _aL_ 21 _· · ·_

_aL_ 12 _aL_ 22 _· · ·_
... ... ...







_∂_ RSS



_∂_ RSS

_σ_ _[′]_ (Σ _L_ 1) _aL_ 11 + _[∂]_ [RSS]
_∂hL_ 1 _∂hL_ 2







_∂_ RSS



_∂_ RSS

_σ_ _[′]_ (Σ _L_ 1) _aL_ 12 + _[∂]_ [RSS]
_∂hL_ 1 _∂hL_ 2



_σ_ _[′]_ (Σ _L_ 2) _aL_ 21 + _· · ·_
_∂hL_ 2

_[∂]_ [RSS] _σ_ _[′]_ (Σ _L_ 2) _aL_ 22 + _· · ·_

_∂hL_ 2
...











_∂_ RSS



_σ_ _[′]_ (Σ _L_ 1)
_∂hL_ 1





















_∂_ RSS



_σ_ _[′]_ (Σ _L_ 2)
_∂hL_ 2
...



= _A_ _[T]_ _L_




_∂_ RSS  - [�]

_⃗_

_◦_ _σ_ _[′]_ [ �] Σ _L_ _,_
_∂_ _[⃗]_ _hL_



where _◦_ denotes the element-wise product.


We keep backpropagating using the same approach until we reach the



input layer. At that point, we will have computed _[∂]_ [RSS]



neuron in the network.



for every
_∂hℓi_



337


_Justin Skycak_

## **Expansion of Neuron Output Gradients to** **Weight Gradients**


Finally, we expand the neuron output gradients into weight gradients,



i.e. coefficient gradients _[∂]_ [RSS]




[RSS] and bias gradients _[∂]_ [RSS]

_∂aℓij_ _∂bℓi_



_._
_∂bℓi_



_∂_ RSS



_∂_ RSS

= _[∂]_ [RSS]
_∂aℓij_ _∂hℓi_




[RSS]

_·_ _[∂h][ℓi]_
_∂hℓi_ _∂aℓij_



_∂_

= _[∂]_ [RSS] _·_ [ _σ_ (Σ _ℓi_ )]

_∂hℓi_ _∂aℓij_



_∂_

= _[∂]_ [RSS] _σ_ _[′]_ (Σ _ℓi_ ) _·_ [Σ _ℓi_ ]

_∂hℓi_ _∂aℓij_







_∂_

= _[∂]_ [RSS] _σ_ _[′]_ (Σ _ℓi_ ) _·_

_∂hℓi_ _∂aℓij_




_aℓi_ 1 _h_ ( _ℓ−_ 1)1 + _aℓi_ 2 _h_ ( _ℓ−_ 1)2
+ _· · ·_ + _b_ ( _ℓ−_ 1) _i_



= _[∂]_ [RSS] _σ_ _[′]_ (Σ _ℓi_ ) _h_ ( _ℓ−_ 1) _j_

_∂hℓi_


338


_Introduction to Algorithms and Machine Learning_


By the same computation, we get



_∂_ RSS



_σ_ _[′]_ (Σ _ℓi_ ) _._
_∂hℓi_



_∂_ RSS

= _[∂]_ [RSS]
_∂bℓi_ _∂hℓi_



Notice that the expression for _[∂]_ [RSS]



_∂_ RSS

_,_ so we can simplify:
_∂aℓij_



appears in the expression for
_∂bℓi_



RSS

= _[∂]_ [RSS]
_∂bℓi_ _∂hℓi_



_∂_ RSS



_σ_ _[′]_ (Σ _ℓi_ )
_∂hℓi_



_∂_ RSS



_∂_ RSS

= _[∂]_ [RSS]
_∂aℓij_ _∂bℓi_



_h_ ( _ℓ−_ 1) _j_
_∂bℓi_



Again, we can consolidate into vector form:



RSS

= _[∂]_ [RSS]
_∂_ _[⃗]_ _bℓ_ _∂_ _[⃗]_ _hℓ_


RSS

= _[∂]_ [RSS]
_∂Aℓ_ _∂_ _[⃗]_ _b_



_∂_ RSS




_◦_ _σ_ _[′]_ [ �] Σ _⃗_ _ℓ_   _∂_ _[⃗]_ _hℓ_



_∂_ RSS



_⊗_ _[⃗]_ _hℓ−_ 1 _,_
_∂_ _[⃗]_ _bℓ_



where _⊗_ is the outer product.



339


_Justin Skycak_

## **Gradient Descent Update**


Once we know allthe weightgradients,we can update the weights using


the usual gradient descent update:



_Aℓ_ _→_ _Aℓ_ _−_ _α_ _[∂]_ [RSS]




 =
_∂Aℓ_




[RSS] _∂_ RSS

where
_∂Aℓ_ _∂Aℓ_



( _⃗x,y_ )



����( _⃗x,y_ )



_∂_ RSS

_∂Aℓ_



_⃗bℓ_ _→_ _⃗bℓ_ _−_ _α_ _[∂]_ [RSS]




[RSS] _∂_ RSS

where
_∂_ _[⃗]_ _bℓ_ _∂_ _[⃗]_ _bℓ_




 =
_∂_ _[⃗]_ _bℓ_



( _⃗x,y_ )



����( _⃗x,y_ )



_∂_ RSS

_∂_ _[⃗]_ _bℓ_


## **Pseudocode**

The following pseudocode summarizes the backpropagation algorithm


that was derived above.


1. Reset all gradient placeholders


_∀ℓ_ _∈{_ 1 _,_ 2 _, ..., L}_ :











_∂_ RSS

=
_∂Aℓ_







0 0 _· · ·_


0 0 _· · ·_
... ... ...







_∂_ RSS

= _[⃗]_ 0
_∂_ _[⃗]_ _bℓ_


340


_Introduction to Algorithms and Machine Learning_


2. Loop over all data points


_∀_ ( _⃗x, y_ ) :


2.1 Forward propagate neuron activities


_⃗_
Σ0 = _⃗x_


_⃗h_ 0 = _⃗x_


_∀ℓ_ _∈{_ 0 _,_ 1 _, . . ., L}_ :


_⃗_
Σ _ℓ_ +1 = _Aℓ_ +1 _⃗hℓ_ + _⃗bℓ_ +1


_⃗hℓ_ +1 = _σ_ �Σ _⃗_ _ℓ_ +1�


2.2 Backpropagate neuron output gradients


_∂_ RSS
= 2       - _h_ ( _ℓ_ +1)1 _−_ _y_       _∂h_ ( _L_ +1)1


_∀ℓ_ _∈{L, L −_ 1 _, . . .,_ 1 _}_ :



_∂_ RSS

= _A_ _[T]_ _ℓ_ +1
_∂_ _[⃗]_ _hℓ_




_∂_ RSS  - [�]

_◦_ _σ_ _[′]_ [ �] Σ _⃗_ _ℓ_ +1
_∂_ _[⃗]_ _hℓ_ +1



341


_Justin Skycak_


2.3 Expand to weight gradients


_∀ℓ_ _∈{L_ + 1 _, L, . . .,_ 1 _}_ :



_∂_ RSS

_∂_ _[⃗]_ _bℓ_


_∂_ RSS

_∂Aℓ_



_⃗_         
= _[∂]_ [RSS] _◦_ _σ_ _[′]_ [ �] Σ _ℓ_
����( _⃗x,y_ ) _∂_ _[⃗]_ _hℓ_



= _[∂]_ [RSS] _⊗_ _[⃗]_ _hℓ−_ 1
����( _⃗x,y_ ) _∂_ _[⃗]_ _bℓ_ ����( _⃗x,y_ )



_∂_ RSS




[RSS]

+ _[∂]_ [RSS]
_∂Aℓ_ _∂Aℓ_



RSS

_→_ _[∂]_ [RSS]
_∂Aℓ_ _∂Aℓ_



_∂Aℓ_



_∂_ RSS



RSS

_→_ _[∂]_ [RSS]
_∂_ _[⃗]_ _bℓ_ _∂_ _[⃗]_ _bℓ_




[RSS]

+ _[∂]_ [RSS]
_∂_ _[⃗]_ _bℓ_ _∂_ _[⃗]_ _bℓ_



_∂_ _[⃗]_ _bℓ_



����( _⃗x,y_ )

����( _⃗x,y_ )



3. Update weights via gradient descent


_∀ℓ_ _∈{_ 1 _,_ 2 _, ..., L}_ :


_Aℓ_ _→_ _Aℓ_ _−_ _α_ _[∂]_ [RSS]

_∂Aℓ_

_⃗bℓ_ _→_ _⃗bℓ_ _−_ _α_ _[∂]_ [RSS]

_∂_ _[⃗]_ _bℓ_


You might notice that steps 2.2 and 2.3 above can be combined more



efficiently into a single step since _[∂]_ [RSS]




[RSS] _∂_ RSS

= _A_ _[T]_ _ℓ_ +1
_∂_ _[⃗]_ _hℓ_ _∂_ _[⃗]_ _bℓ_ +1



_._ However, we
_∂_ _[⃗]_ _bℓ_ +1



will keep these steps separate for the sake of intuitive clarity. You are



welcome to combine these steps in your own implementation.


342


_Introduction to Algorithms and Machine Learning_

## **Worked Example of a Single Iteration**


Now,let’s walkthroughan concrete example offitting a neuralnetwork


to a data set using the backpropagation algorithm. We will use the same


data set and neural network architecture as the previous chapter:


[(0 _,_ 0) _,_ (0 _._ 25 _,_ 1) _,_ (0 _._ 5 _,_ 0 _._ 5) _,_ (0 _._ 75 _,_ 1) _,_ (1 _,_ 0)]


Because neural networks are hierarchical and high-dimensional (i.e.


they have many parameters that are tightly coupled), they are vastly


more difficult to train as compared to simpler non-hierarchical low

dimensional models like linear, logistic, and polynomial regressions.


343


_Justin Skycak_


Various tricks are often required to prevent the neural network from


getting “stuck” in suboptimal local minima, which we will not cover


here.


To provide a simple example that illustrates the training of a neural


network to a high degree of accuracy while avoiding the need for


more advanced tricks, we will intentionally choose the initial weights


of our network to be similar to the weights that we arrived at when


manually constructing a neural network in the previous chapter. (More


specifically, they will be proportional by a factor of 0 _._ 5 _._ ) This will place


us near a deep valley on the surface of RSS as a function of parameters


of the neural network,and the proximity will allow elementary gradient


descent to lead us down into the valley.


So, we will use the following initial weights:











5








_−_ 0 _._ 75











1 _._ 75







_A_ 1 =


_A_ 2 =








_−_ 5



0 0 10 10




_⃗b_ 2 =



5



_⃗b_ 1 =





_−_ 3 _._ 25




_−_ 5




10 10 0 0



4 _._ 25


- 
_−_ 12 _._ 5


_−_ 12 _._ 5



_A_ 3 = �10 10� _⃗b_ 3 =   - _−_ 2 _._ 5�


Let’s work out the first iteration of backpropagation by hand, using


learning rate _α_ = 0 _._ 01 _._ Note that the values shown are rounded to 6


344


_Introduction to Algorithms and Machine Learning_


decimal places, but intermediate values are not actually rounded in the


implementation.


**Point:** ( _⃗x, y_ ) = ([0] _,_ 0)


_Forward propagation_


Σ _⃗_ 0 = _⃗x_ = �0�


_⃗h_ 0 = _⃗x_ = �0�



 _−_ 0 _._ 75



 _−_ 0 _._ 75















5




- 0 +






=




1 _._ 75




_−_ 3 _._ 25



1 _._ 75



Σ _⃗_ 1 = _A_ 1 _⃗h_ 0 + _⃗b_ 1 =








_−_ 5



5














_−_ 3 _._ 25




_−_ 5









4 _._ 25



4 _._ 25




0 _._ 320821
















 =











0 _._ 851953


0 _._ 037327



0 _._ 985936







_⃗h_ 1 = _σ_ �Σ _⃗_ 1� = _σ_



















_−_ 0 _._ 75

1 _._ 75


_−_ 3 _._ 25



4 _._ 25





0 _._ 320821











0 _._ 851953


0 _._ 037327


0 _._ 985936










+





- _−_ 12 _._ 5�


_−_ 12 _._ 5



Σ _⃗_ 2 = _A_ 2 _⃗h_ 1 + _⃗b_ 2 =




10 10 0 0


0 0 10 10



=




- _−_ 0 _._ 772259


_−_ 2 _._ 267367



_⃗h_ 2 = _σ_ �Σ _⃗_ 2� = _σ_



�� _−_ 0 _._ 772259��


_−_ 2 _._ 267367



=




- 0 _._ 315991


0 _._ 093862




         -         - [�] 0 _._ 315991
Σ _⃗_ 3 = _A_ 3 _⃗h_ 2 + _⃗b_ 3 = 10 10

0 _._ 093862




         -         - [�] 0 _._ 315991
Σ _⃗_ 3 = _A_ 3 _⃗h_ 2 + _⃗b_ 3 = 10 10








  -  -  -  + _−_ 2 _._ 5 = 1 _._ 59852529



_⃗h_ 3 = _σ_ �Σ _⃗_ 3� = _σ_ ��1 _._ 598525�� = �0 _._ 831812�


345


_Justin Skycak_


_Backpropagation_


_∂_ RSS
= 2 ( _h_ 31 _−_ _y_ ) = 2 (0 _._ 831812 _−_ 0) = 1 _._ 663624
_∂h_ 31



�2 _._ 327422�

2 _._ 327422



_∂_ RSS

= _A_ _[T]_ 3
_∂_ _[⃗]_ _h_ 2




- _∂_ RSS - [�]

_◦_ _σ_ _[′]_ [ �] Σ _⃗_ 3 =
_∂_ _[⃗]_ _h_ 3



�10��� - ���

1 _._ 663624 _◦_ _σ_ _[′]_ [ ��] 1 _._ 59852529 =

10



10 0

10 0

0 10

0 10















�� _−_ 0 _._ 772259

_◦_ _σ_ _[′]_

_−_ 2 _._ 267367



���









��2 _._ 327422

2 _._ 327422







_∂_ RSS

= _A_ _[T]_ 2
_∂_ _[⃗]_ _h_ 1




- _∂_ RSS - [�]

_◦_ _σ_ _[′]_ [ �] Σ _⃗_ 2 =
_∂_ _[⃗]_ _h_ 2



=









5 _._ 030502

5 _._ 030502

1 _._ 979515

1 _._ 979515



_Expansion_



= _∂_ RSS _◦_ _σ_ _[′]_ [ �] Σ _⃗_ 3� = �1 _._ 663624� _◦_ _σ_ _[′]_ [ ��] 1 _._ 598525�� = �0 _._ 232742�
�����([0] _,_ 0) _∂_ _[⃗]_ _h_ 3



_∂_ RSS

_∂_ _[⃗]_ _b_ 3


_∂_ RSS


_∂A_ 3


_∂_ RSS

_∂_ _[⃗]_ _b_ 2


_∂_ RSS


_∂A_ 2


_∂_ RSS

_∂_ _[⃗]_ _b_ 1


_∂_ RSS


_∂A_ 1



_∂_ RSS
=
����([0] _,_ 0) _∂_ _[⃗]_ _b_ 3




            
        -        - 0 _._ 315991
�����([0] _,_ 0) _⊗_ _[⃗]_ _h_ 2 = _−_ 0 _._ 000913 _⊗_ 0 _._ 093862





= �0 _._ 073544 0 _._ 021846�



= _∂_ RSS _◦_ _σ_ _[′]_ [ �] Σ _⃗_ 2� =
�����([0] _,_ 0) _∂_ _[⃗]_ _h_ 2



�2 _._ 327422

2 _._ 327422







�� _−_ 0 _._ 772259

_◦_ _σ_ _[′]_

_−_ 2 _._ 267367



��







=



�0 _._ 503050

0 _._ 197951






=




_∂_ RSS
=
����([0] _,_ 0) _∂_ _[⃗]_ _b_ 2



_⊗_ _[⃗]_ _h_ 1 =
�����([0] _,_ 0)



�0 _._ 503050

0 _._ 197951







_⊗_









0 _._ 320821

0 _._ 851953

0 _._ 037327

0 _._ 985936



�0 _._ 161389 0 _._ 428575 0 _._ 018777 0 _._ 495976�

0 _._ 063507 0 _._ 168645 0 _._ 007389 0 _._ 195168






_◦_ _σ′_





















_−_ 0 _._ 75

1 _._ 75

_−_ 3 _._ 25

4 _._ 25

















= _∂_ RSS _◦_ _σ_ _[′]_ [ �] Σ _⃗_ 1� =
�����([0] _,_ 0) _∂_ _[⃗]_ _h_ 1









5 _._ 030502

5 _._ 030502

1 _._ 979515

1 _._ 979515







 [=]







1 _._ 096121


0 _._ 634493

0 _._ 071131

0 _._ 027448






_⊗_ �0� =



346















0

0

0

0



1 _._ 096121

0 _._ 634493

0 _._ 071131

0 _._ 027448



_∂_ RSS
=
����([0] _,_ 0) _∂_ _[⃗]_ _b_ 1



_⊗_ _[⃗]_ _h_ 0 =
�����([0] _,_ 0)








_Introduction to Algorithms and Machine Learning_


**Point:** ( _⃗x, y_ ) = ([0 _._ 25] _,_ 1)


Σ _⃗_ 0 = �0 _._ 25� _⃗h_ 0 = �0 _._ 25�





0 _._ 5











0 _._ 622459


0 _._ 622459


0 _._ 119203


0 _._ 952574










_⃗h_ 1 =








Σ _⃗_ 1 =


Σ _⃗_ 2 =







0 _._ 5


_−_ 2




_−_ 1 _._ 782230




_⃗h_ 2 =



3





_−_ 0 _._ 050813




- 0 _._ 487299


0 _._ 144028



Σ _⃗_ 3 = �3 _._ 813274� _⃗h_ 3 = �0 _._ 978401�



 _−_ 0 _._ 022807







_∂_ RSS
_,_ =

_∂_ _[⃗]_ _h_ 1









_∂_ RSS



=
_∂_ _[⃗]_ _h_ 2



RSS - - _∂_ RSS

= _−_ 0 _._ 043198 _,_
_∂_ _[⃗]_ _h_ 3 _∂_ _[⃗]_ _h_ 2








_−_ 0 _._ 022807


_−_ 0 _._ 011254


_−_ 0 _._ 011254




- 
_−_ 0 _._ 009129


_−_ 0 _._ 009129



_∂_ RSS

_∂_ _[⃗]_ _b_ 3


_∂_ RSS

_∂_ _[⃗]_ _b_ 2


_∂_ RSS

_∂_ _[⃗]_ _b_ 1



=    - _−_ 0 _._ 000913� _∂_ RSS =    - _−_ 0 _._ 000445 _−_ 0 _._ 000131�
�����([0 _._ 25] _,_ 1) _∂A_ 3 ����([0 _._ 25] _,_ 1)



=
�����([0 _._ 25] _,_ 1)


=
�����([0 _._ 25] _,_ 1)










_−_ 0 _._ 005360

_−_ 0 _._ 005360

_−_ 0 _._ 001182

_−_ 0 _._ 000508




- _−_ 0 _._ 002281

_−_ 0 _._ 001125




- _∂_ RSS


_∂A_ 2




- _−_ 0 _._ 001420 _−_ 0 _._ 001420 _−_ 0 _._ 000272 _−_ 0 _._ 002173�

_−_ 0 _._ 000701 _−_ 0 _._ 000701 _−_ 0 _._ 000134 _−_ 0 _._ 001072









=
����([0 _._ 25] _,_ 1)


=
����([0 _._ 25] _,_ 1)


347









_∂_ RSS


_∂A_ 1



 _−_ 0 _._ 001340


_−_ 0 _._ 001340

 _−_ 0 _._ 000295

_−_ 0 _._ 000127


**Point:** ( _⃗x, y_ ) = ([0 _._ 5] _,_ 0 _._ 5)



_∂_ RSS

_∂_ _[⃗]_ _b_ 3


_∂_ RSS

_∂_ _[⃗]_ _b_ 2


_∂_ RSS

_∂_ _[⃗]_ _b_ 1



= �0 _._ 020099� _∂_ RSS
�����([0 _._ 5] _,_ 0 _._ 5) _∂A_ 3



=
�����([0 _._ 5] _,_ 0 _._ 5)


=
�����([0 _._ 5] _,_ 0 _._ 5)









_Justin Skycak_


= �0 _._ 006351 0 _._ 006351�
����([0 _._ 5] _,_ 0 _._ 5)



0 _._ 054794

0 _._ 094659

0 _._ 094659

0 _._ 054794



�0 _._ 043443

0 _._ 043443




 - _∂_ RSS


_∂A_ 2







�0 _._ 037011 0 _._ 013937 0 _._ 013937 0 _._ 037011

0 _._ 037011 0 _._ 013937 0 _._ 013937 0 _._ 037011



0 _._ 027397


0 _._ 047330

0 _._ 047330

0 _._ 027397









=
����([0 _._ 5] _,_ 0 _._ 5)


=
����([0 _._ 5] _,_ 0 _._ 5)



_∂_ RSS


_∂A_ 1









**Point:** ( _⃗x, y_ ) = ([0 _._ 75] _,_ 1)



_∂_ RSS

_∂_ _[⃗]_ _b_ 3


_∂_ RSS

_∂_ _[⃗]_ _b_ 2


_∂_ RSS

_∂_ _[⃗]_ _b_ 1



=    - _−_ 0 _._ 000913� _∂_ RSS
�����([0 _._ 75] _,_ 1) _∂A_ 3



=
�����([0 _._ 75] _,_ 1)


=
�����([0 _._ 75] _,_ 1)









=    - _−_ 0 _._ 000131 _−_ 0 _._ 000445�
����([0 _._ 75] _,_ 1)




_−_ 0 _._ 000508

_−_ 0 _._ 001182

_−_ 0 _._ 005360

_−_ 0 _._ 005360








- _−_ 0 _._ 001125

_−_ 0 _._ 002281




- _∂_ RSS


_∂A_ 2




- _−_ 0 _._ 001072 _−_ 0 _._ 000134 _−_ 0 _._ 000701 _−_ 0 _._ 000701

_−_ 0 _._ 002173 _−_ 0 _._ 000272 _−_ 0 _._ 001420 _−_ 0 _._ 001420



 _−_ 0 _._ 000381


_−_ 0 _._ 000886

 _−_ 0 _._ 004020

_−_ 0 _._ 004020









_∂_ RSS


_∂A_ 1



=
����([0 _._ 75] _,_ 1)


=
����([0 _._ 75] _,_ 1)









**Point:** ( _⃗x, y_ ) = ([1] _,_ 0)



_∂_ RSS

_∂_ _[⃗]_ _b_ 3


_∂_ RSS

_∂_ _[⃗]_ _b_ 2


_∂_ RSS

_∂_ _[⃗]_ _b_ 1



= �0 _._ 232742� _∂_ RSS = �0 _._ 021846 0 _._ 073544�
�����([1] _,_ 0) _∂A_ 3 ����([1] _,_ 0)



=
�����([1] _,_ 0)


=
�����([1] _,_ 0)









0 _._ 027448

0 _._ 071131

0 _._ 634493

1 _._ 096121



�0 _._ 197951

0 _._ 503050




- _∂_ RSS


_∂A_ 2







�0 _._ 195168 0 _._ 007389 0 _._ 168645 0 _._ 063507

0 _._ 495976 0 _._ 018777 0 _._ 428575 0 _._ 161389



0 _._ 027448


0 _._ 071131

0 _._ 634493

1 _._ 096121









=
����([1] _,_ 0)


=
����([1] _,_ 0)









_∂_ RSS


_∂A_ 1



**Weight Updates**



348


_Introduction to Algorithms and Machine Learning_


Summing up all the gradients we computed, we get the following:



_∂_ RSS



RSS - - _∂_ RSS

= 0 _._ 483758
_∂_ _[⃗]_ _b_ 3 _∂A_ 3




    -     = 0 _._ 101165 0 _._ 101165
_∂A_ 3




- 0 _._ 391076 0 _._ 448347 0 _._ 200388 0 _._ 593621


0 _._ 593621 0 _._ 200388 0 _._ 448347 0 _._ 391076



_∂_ RSS

=
_∂_ _[⃗]_ _b_ 2




0 _._ 741038


0 _._ 741038




_∂_ RSS

=
_∂A_ 2




_∂_ RSS





1 _._ 172495





0 _._ 053123















0 _._ 116235


0 _._ 677508



1 _._ 119371



_∂_ RSS

=
_∂_ _[⃗]_ _b_ 1







0 _._ 793742


0 _._ 793742


1 _._ 172495



_∂_ RSS

=
_∂A_ 1



Finally, applying the gradient descent updates _Aℓ_ _→_ _Aℓ_ _−_ _α_ [RSS]



_⃗bℓ_ _→_ _⃗bℓ−α_ [RSS]



and
_∂Aℓ_



with _α_ = 0 _._ 01 _,_ we getthe following updatedweights:
_∂_ _[⃗]_ _bℓ_







4 _._ 999469



 _−_ 0 _._ 761725











1 _._ 742063









_A_ 1 =


_A_ 2 =








9 _._ 996089 9 _._ 995517 _−_ 0 _._ 002004 _−_ 0 _._ 005936


_−_ 0 _._ 005936 _−_ 0 _._ 002004 9 _._ 995517 9 _._ 996089




_−_ 5 _._ 001162



4 _._ 993225




_−_ 3 _._ 257937




_−_ 5 _._ 011194






_⃗b_ 1 =





_⃗b_ 2 =



4 _._ 238275


- _−_ 12 _._ 507410�


_−_ 12 _._ 507410




   -    -    -    _A_ 3 = 9 _._ 998988 9 _._ 998988 _⃗b_ 3 = _−_ 2 _._ 504838


349


_Justin Skycak_

## **Demonstration of Many Iterations**


Repeating this procedure over and over, we get the following results.


Note that the values shown are rounded to 3 decimal places, but


intermediate values are not actually rounded in the implementation.


_Initial_


   - RSS _≈_ 1 _._ 614


   - Predictions _≈_ 0 _._ 832 _,_ 0 _._ 978 _,_ 0 _._ 979 _,_ 0 _._ 978 _,_ 0 _._ 832


(Compare to 0 _,_ 1 _,_ 0 _._ 5 _,_ 1 _,_ 0)







5








_−_ 0 _._ 75















1 _._ 75







_A_ 1 =


_A_ 2 =








_−_ 5



0 0 10 10




_⃗b_ 2 =



5



_⃗b_ 1 =





_−_ 3 _._ 25




_−_ 5




10 10 0 0



4 _._ 25


- 
_−_ 12 _._ 5


_−_ 12 _._ 5




   -   -   -   _A_ 3 = 10 10 _⃗b_ 3 = _−_ 2 _._ 5


350


_Introduction to Algorithms and Machine Learning_


_After_ 1 _iteration_


   - RSS _≈_ 1 _._ 525


   - Predictions _≈_ 0 _._ 812 _,_ 0 _._ 973 _,_ 0 _._ 973 _,_ 0 _._ 972 _,_ 0 _._ 801







4 _._ 999








_−_ 0 _._ 762















1 _._ 742







_A_ 1 =


_A_ 2 =








_−_ 5 _._ 001




_−_ 0 _._ 006 _−_ 0 _._ 002 9 _._ 996 9 _._ 996



4 _._ 993



_⃗b_ 1 =





_−_ 3 _._ 258




_−_ 5 _._ 011




9 _._ 996 9 _._ 996 _−_ 0 _._ 002 _−_ 0 _._ 006



4 _._ 238


- 
_−_ 12 _._ 507


_−_ 12 _._ 507




_⃗b_ 2 =




   -    -    -    _A_ 3 = 9 _._ 999 9 _._ 999 _⃗b_ 3 = _−_ 2 _._ 505


_After_ 2 _iterations_


   - RSS _≈_ 1 _._ 426


   - Predictions _≈_ 0 _._ 789 _,_ 0 _._ 967 _,_ 0 _._ 965 _,_ 0 _._ 962 _,_ 0 _._ 765


351


_Justin Skycak_








_−_ 0 _._ 774











4 _._ 999















_A_ 1 _≈_


_A_ 2 _≈_








_−_ 5 _._ 002




_−_ 0 _._ 012 _−_ 0 _._ 004 9 _._ 991 9 _._ 992



1 _._ 734



4 _._ 986



_⃗b_ 1 _≈_





_−_ 3 _._ 267




_−_ 5 _._ 023




9 _._ 992 9 _._ 991 _−_ 0 _._ 004 _−_ 0 _._ 012



4 _._ 226


- 
_−_ 12 _._ 515


_−_ 12 _._ 515




_⃗b_ 2 _≈_




   -    -    -    _A_ 3 _≈_ 9 _._ 998 9 _._ 998 _⃗b_ 3 _≈_ _−_ 2 _._ 510


_After_ 3 _iterations_


   - RSS _≈_ 1 _._ 320


   - Predictions _≈_ 0 _._ 764 _,_ 0 _._ 959 _,_ 0 _._ 954 _,_ 0 _._ 949 _,_ 0 _._ 725







4 _._ 998








_−_ 0 _._ 787















1 _._ 725







_A_ 1 _≈_


_A_ 2 _≈_








_−_ 5 _._ 004




_−_ 0 _._ 019 _−_ 0 _._ 006 9 _._ 986 9 _._ 988



4 _._ 978



_⃗b_ 1 _≈_





_−_ 3 _._ 276




_−_ 5 _._ 035




9 _._ 987 9 _._ 986 _−_ 0 _._ 006 _−_ 0 _._ 019



4 _._ 213


- 
_−_ 12 _._ 524


_−_ 12 _._ 524




_⃗b_ 2 _≈_




   -   -   -   _A_ 3 _≈_ 9 _._ 997 9 _._ 997 _⃗b_ 3 _≈_ _−_ 2 _._ 516


352


_Introduction to Algorithms and Machine Learning_


_After_ 10 _iterations_


   - RSS _≈_ 0 _._ 730


   - Predictions _≈_ 0 _._ 571 _,_ 0 _._ 844 _,_ 0 _._ 816 _,_ 0 _._ 774 _,_ 0 _._ 478







4 _._ 992








_−_ 0 _._ 873















1 _._ 66







_A_ 1 _≈_


_A_ 2 _≈_








_−_ 5 _._ 015




_−_ 0 _._ 058 _−_ 0 _._ 022 9 _._ 958 9 _._ 959



4 _._ 933



_⃗b_ 1 _≈_





_−_ 3 _._ 331




_−_ 5 _._ 101




9 _._ 957 9 _._ 953 _−_ 0 _._ 022 _−_ 0 _._ 064



4 _._ 142


- 
_−_ 12 _._ 58


_−_ 12 _._ 575




_⃗b_ 2 _≈_




   -    -    -    _A_ 3 _≈_ 9 _._ 99 9 _._ 991 _⃗b_ 3 _≈_ _−_ 2 _._ 557


_After_ 100 _iterations_


   - RSS _≈_ 0 _._ 496


   - Predictions _≈_ 0 _._ 362 _,_ 0 _._ 694 _,_ 0 _._ 730 _,_ 0 _._ 698 _,_ 0 _._ 356


353


_Justin Skycak_

















5 _._ 068




_−_ 0 _._ 936







_⃗b_ 1 _≈_








_A_ 1 _≈_


_A_ 2 _≈_








_−_ 0 _._ 116 _−_ 0 _._ 074 9 _._ 894 9 _._ 921




_−_ 4 _._ 962



1 _._ 696



4 _._ 965




_−_ 3 _._ 249




_−_ 5 _._ 158




9 _._ 920 9 _._ 862 _−_ 0 _._ 064 _−_ 0 _._ 15



4 _._ 164


- 
_−_ 12 _._ 708


_−_ 12 _._ 683




_⃗b_ 2 _≈_




   -    -    -    _A_ 3 _≈_ 9 _._ 978 9 _._ 981 _⃗b_ 3 _≈_ _−_ 2 _._ 735


_After_ 1 000 _iterations_


   - RSS _≈_ 0 _._ 198


   - Predictions _≈_ 0 _._ 199 _,_ 0 _._ 788 _,_ 0 _._ 668 _,_ 0 _._ 788 _,_ 0 _._ 202







5 _._ 491








_−_ 0 _._ 518















2 _._ 008







_A_ 1 _≈_


_A_ 2 _≈_








_−_ 5 _._ 101




_−_ 0 _._ 442 _−_ 0 _._ 301 9 _._ 668 9 _._ 721



5 _._ 343



_⃗b_ 1 _≈_





_−_ 3 _._ 081




_−_ 5 _._ 152




9 _._ 744 9 _._ 666 _−_ 0 _._ 301 _−_ 0 _._ 425



4 _._ 546


- 
_−_ 13 _._ 155


_−_ 13 _._ 170




_⃗b_ 2 _≈_




   -   -   -   _A_ 3 _≈_ 9 _._ 982 9 _._ 98 _⃗b_ 3 _≈_ _−_ 3 _._ 596


354


_Introduction to Algorithms and Machine Learning_


_After_ 10 000 _iterations_


   - RSS _≈_ 0 _._ 0239


   - Predictions _≈_ 0 _._ 068 _,_ 0 _._ 922 _,_ 0 _._ 517 _,_ 0 _._ 915 _,_ 0 _._ 075







6 _._ 96








_−_ 0 _._ 279















2 _._ 766







_A_ 1 _≈_


_A_ 2 _≈_








_−_ 6 _._ 033




_−_ 0 _._ 932 _−_ 0 _._ 806 9 _._ 647 9 _._ 781



6 _._ 632



_⃗b_ 1 _≈_





_−_ 3 _._ 307




_−_ 5 _._ 806




9 _._ 88 9 _._ 555 _−_ 0 _._ 835 _−_ 0 _._ 865



5 _._ 478


- 
_−_ 13 _._ 763


_−_ 13 _._ 804




_⃗b_ 2 _≈_




   -    -    -    _A_ 3 _≈_ 10 _._ 515 10 _._ 542 _⃗b_ 3 _≈_ _−_ 4 _._ 759


_After_ 100 000 _iterations_


   - RSS _≈_ 0 _._ 0020


   - Predictions _≈_ 0 _._ 020 _,_ 0 _._ 979 _,_ 0 _._ 501 _,_ 0 _._ 976 _,_ 0 _._ 023


355


_Justin Skycak_








_−_ 0 _._ 523











8 _._ 407















_A_ 1 _≈_


_A_ 2 _≈_








_−_ 7 _._ 103




_−_ 1 _._ 179 _−_ 1 _._ 311 9 _._ 922 10 _._ 416




_⃗b_ 2 _≈_



3 _._ 289



7 _._ 786



_⃗b_ 1 _≈_





_−_ 3 _._ 906




_−_ 6 _._ 971




10 _._ 437 9 _._ 708 _−_ 1 _._ 367 _−_ 1 _._ 063



6 _._ 412


- 
_−_ 14 _._ 075


_−_ 14 _._ 139




   -    -    -    _A_ 3 _≈_ 11 _._ 607 11 _._ 800 _⃗b_ 3 _≈_ _−_ 5 _._ 433


_After_ 1 000 000 _iterations_


   - RSS _≈_ 0 _._ 0002


   - Predictions _≈_ 0 _._ 006 _,_ 0 _._ 993 _,_ 0 _._ 500 _,_ 0 _._ 993 _,_ 0 _._ 007







9 _._ 527








_−_ 0 _._ 738















3 _._ 651







_A_ 1 _≈_


_A_ 2 _≈_








_−_ 7 _._ 895




_−_ 1 _._ 405 _−_ 1 _._ 730 10 _._ 129 11 _._ 100



8 _._ 602



_⃗b_ 1 _≈_





_−_ 4 _._ 384




_−_ 7 _._ 956




11 _._ 006 9 _._ 855 _−_ 1 _._ 801 _−_ 1 _._ 214




_⃗b_ 2 _≈_



7 _._ 219


- 
_−_ 14 _._ 323


_−_ 14 _._ 440




   -   -   -   _A_ 3 _≈_ 12 _._ 902 13 _._ 223 _⃗b_ 3 _≈_ _−_ 6 _._ 178


356


_Introduction to Algorithms and Machine Learning_


Below is a graph of the regression curves before and after training (i.e.


using the initialweights andusing the weights after 1 000 000 iterations


of backpropagation). The trained network does an even better job of


passing through the leftmost and rightmost points than the network


we constructed manually in the previous section!

## **Exercises**


1 _._ Implement the example that was worked out above.


2 _._ Re-run the example that was worked out above, this time using


initial weights drawn randomly from the normal distribution.


Note that your RSS should gradually decrease but it may get


“stuck” in a suboptimal local minimum, resulting in a regression


curve that is a decent but not perfect fit.


357


_Justin Skycak_


358


# **Part VI** **Games**

359


_Justin Skycak_


360


# **37. Canonical and Reduced** **Game Trees for Tic-Tac-Toe**

A **game tree** is a data structure thatrepresents allthe possible outcomes

of a game. It is a graph where the nodes correspond to the states of


the game, and the edges correspond to actions that cause the game to


transition from one state to another. Game trees are commonly used


when coding up strategies for autonomous game-playing agents.

## **Exercise: Tic-Tac-Toe Tree**


Create a class `TicTacToeTree` that constructs a game tree for tic-tac

toe. Each node in the game tree has corresponds to a state of the game.


The root node represents an empty board. It has 9 children, one for


each move that the first player can make. Each of those 9 children have


8 children (after the first player has moved, there are 8 moves remaining


for the second player). And so on.


361


_Justin Skycak_


There are 255 168 unique ways that a game of tic-tac-toe can play out,

so you can check your tree by verifying that there are 255 168 _leaf nodes_ .


Here are some tips regarding the implementation:


   - Each node should have a state attribute that holds the state of the


tic-tac-toe game, a player attribute that says whose turn it is, and


a winner attribute that says if someone has won.


   - Instead of passing edges into the tree at initialization, you’ll need


to build up your tree algorithmically: start with a tree with a


single node, and then repeatedly create child nodes until they


reach a terminal state (i.e. a state where the game is finished).


   - Ultimately this just comes down to a graph traversal (breadth

first or depth-first, doesn’t matter which). Whenever a node’s


362


_Introduction to Algorithms and Machine Learning_


game state is not terminal, create a child node for each possible


next state.

## **Exercise: Reduced Tic-Tac-Toe Tree**


Once you’ve built your `TicTacToeTree` and verified that it has


the correct number of leaf nodes, the next step is to make it more


efficient. Noticethattherearemanyredundancieswhereseparatenodes


represent the same state:


Although redundancies are included in the canonical conception of a


game tree, we can greatly speed up the construction and reduce the size


of our game tree if we use only one node per game state. To do this,


363


_Justin Skycak_


you’ll need to make a slight tweak to your traversal so that whenever a


node with the desired state already exists, you connect up that existing


node as a child (instead of creating a new node).


_Do not loop over the tree every time to check if a node with the desired_

_child state already exists._ That would be really inefficient! Instead, store

nodes in a dictionary where the key represents the game state. That way,


to check if a node with a particular game state already exists, you just


need to look up that state in the dictionary.


There are 5 478 distinct possible game states in the game of tic-tac-toe,


so you can check your reduced tree by verifying that there are 5 478

nodes _in total_ .


364


# **38. Minimax Strategy**

The **minimax** **strategy** is a powerful game-playing strategy that

operates on game trees. It envisions the worst-case scenario that could


possibly result from any given move, and then chooses the move that


would result in the best (i.e. “least bad”) worst-case scenario.

## **Minimax Algorithm**


The minimax strategy chooses actions according to the following


algorithm:


1 _._ Create a game tree with all the states of the game.


2 _._ Identify each node that represents a terminal state and assign


it a minimax value of 1 _,_ _−_ 1 _,_ or 0 depending on whether it


corresponds to a win, loss, or tie for you.


3 _._ Repeatedly propagate those values up the tree to parent nodes,


assuming that you will try to win (i.e. move into states that


maximize your value) and your opponent will try to make you


lose (i.e. move into states that minimize your value).


365


_Justin Skycak_


**–** If the edge from the parent node corresponds to your turn,

then the parent node’s minimax value is the maximum of


the childvalues (because you wantto maximize yourvalue).


**–** Otherwise, if the edge from the parent node corresponds

to your _opponent’s_ turn, then the parent node’s minimax

value is the _minimum_ of the child values (because your

opponent wants to _minimize_ your value).


   - Always choose the move that takes you to the next possible state


with the highest minimax value. (You can break ties via random


choice.)

## **Worked Example**


To illustrate the minimax algorithm in action, let’s label part of a tic

tac-toe game tree with minimax values,from the perspective of player X


(i.e. supposing we are player X). We always start by labeling the terminal


states.


366


_Introduction to Algorithms and Machine Learning_


Then, we propagate these values up to parent nodes. But we can only


compute the minimax value of a node once we’ve assigned minimax


values to all its children.


Here, there are 3 parents who do not have minimax values but whose


children all do. The edges between these parents and their children all


correspond to moves by X, which is us, and we want to maximize the


minimax value. So, to each of these parents, we assign the maximum


value of its children. (In this case, each of these parents has only one


child, so the maximum value happens to be the only value.)


367


_Justin Skycak_


Now, we repeat the process. Now, there are 2 parents who do not have


minimax values but whose children all do. The edges between these


parents and their children all correspond to moves by O, which is our


opponent,andouropponentwants to minimize the minimax value. So,


to each of these parents, we assign the minimum value of its children.


368


_Introduction to Algorithms and Machine Learning_


Again, we repeat the process. There is a single parent (the top node)


who does not have a minimax value but whose children all do. The


edges between these parents and their children all correspond to moves


by X, which is us, and we want to maximize the minimax value. So we


assign it the maximum value of its children.


369


_Justin Skycak_


We’ve assigned minimax values to all the nodes in this part of the tree.


The minimax value of the highest node is 1 _,_ which tells us that there is


a guaranteed way to win from that game state (all we need to do is place


an X in the bottom-left corner). Indeed, this action is accomplished by


choosing the child node with the maximum value.

## **Exercises**


1 _._ Implement a **minimax** **player** for your tic-tac-toe game that

automatically chooses actions based on the minimax strategy.


(It goes without saying: don’t rebuild and relabel the game tree


on every move. That would be very inefficient and slow. Build


370


_Introduction to Algorithms and Machine Learning_


and label it once at the beginning, and then use the same tree


throughout the rest of the game.)


2 _._ Run your minimax player against a deterministic “top-left


strategy” that always moves into the leftmost open space in the


topmost row. At each of the minimax player’s turns, print out


the possible moves that the minimax player could possibly make


as well as the associated minimax values of the states. Check the


following:


**–** Every minimax value should be either 1 _, −_ 1 _,_ or 0 _._


**–** Each of the minimax player’s chosen moves should be

associated with a maximum-value state.


**–** Towards the end of the game, you should be able to inspect

game states, manually sketch out the section of the game


tree containing their progeny, and then manually compute


and verify the minimax value of each state.


**–** Make sure these checks still hold when the minimax player

goes second.


3 _._ Then,run yourminimax playeragainsta random playerformany


games (alternating who goes first). The minimax player should

_never_ lose. If you encounter any game where the minimax player

loses, then you’ll need to store the sequence of moves and step


through the game to debug what went wrong.


4 _._ Play two minimax players against each other for many games,


alternating who goes first. Every game should result in a tie.


5 _._ Play against the minimax player yourself. You shouldn’t be able


to win.


371


_Justin Skycak_


372


# **39. Reduced Search Depth and** **Heuristic Evaluation for** **Connect Four**

In theory, we could solve any game by building a big game tree, labeling


the terminal states as wins, losses, or ties, and then working backwards


from that information to identify the minimax strategy. But in practice,


game trees get so big so quickly that for all but the most simple games,


game trees are too expensive to store in memory and take too long to


traverse.


For example, consider the game of connect four, which is normally


played on a 7 _×_ 6 board. Whereas tic-tac-toe had 5 478 _,_ valid board


states, connect four has 4 531 985 219 092 _._ Implementing a game tree


of this size is infeasible – if you’re not convinced, try running a simple


“for” loop that loops over the numbers from 1 to 4 531 985 219 092 _._ If


looping over a million numbers takes a few seconds, then looping over


a trillion numbers will take weeks.


373


_Justin Skycak_

## **Reduced Search Depth**


We can’t build a full game tree for connect four. But what we can do


instead is


1 _._ **reduce the search depth** (i.e. build a shortened game tree up to

some maximum depth), and


2 _._ come up with some kind of **heuristic evaluation function** to

rate how good or bad each leaf node state is.


Then we can apply the minimax strategy in an attempt to move in the


direction of the best leaf node state.


This procedure for selecting a move can be outlined more explicitly as


follows:


1 _._ Build a game tree that is _N_ layers deep from the current game

state. (This is called an _N_ **-ply** game tree.)


2 _._ Use the heuristic evaluation function to assign minimax to the


terminal nodes in the game tree.


3 _._ Repeatedly propagate those values up to parent nodes using the


minimax algorithm.


4 _._ Choose your action in accordance with the standard minimax


strategy (i.e. choose the move that takes you to the child state


with the highest minimax value).


374


_Introduction to Algorithms and Machine Learning_


Note that this time, you’ll have to relabel the game tree on every move


because the terminal nodes of the tree will change (thereby changing


theminimaxvaluesoftherestofthetree). Butyoudon’tneedtorebuild


the full game tree on every move – you can take the existing game tree,


prune off nodes that are no longer relevant, and grow the additional


nodes needed to bring you back to a search depth of _N._

## **Heuristic Evaluation Function**


Now, let’s talk about the “secret sauce” in this recipe: the heuristic


evaluationfunction. Ittakesagamestateasinput,andreturnsanumber


between _−_ 1 and 1 that represents how strongly we want or do not


want to be in that game state. To write this function we use our human


intuition about the game. Here are some rough guidelines:


   - If we’re 100% confident that a game state is a win or will result in


a win, then the function should return 1 _._


   - If we think that a win is more likely than a loss,then the function


should return a decimal between 0 and 1 _,_ with higher win


probabilities corresponding to higher decimals.


   - If we have no idea whether a game state will result in a win or


loss, or we think it will result in a tie, then the function should


return 0 _._


   - If we think that a win is less likely than a loss, then the function


should return a decimal between 0 and _−_ 1 _,_ with lower win


probabilities corresponding to more negative decimals.


375


_Justin Skycak_


   - If we’re 100% confident that a game state is a loss or will result in


a loss, then the function should return _−_ 1 _._


For example, here is a simple heuristic function for tic-tac-toe:


1 _._ If the game state is a definite win, tie, or loss, then return 1 _,_ 0 _,_ or


_−_ 1 respectively.


2 _._ Otherwise,countupthenumberofrows,columns,anddiagonals


where you occupy two spaces and the third space is empty. Then,


subtract the number of rows, columns, and diagonals where


your opponent occupies two spaces and the third space is empty.


Finally, divide the result by 8 (which is the total number of rows,


columns, and diagonals).

## **Exercises**


Remember to alternate who goes first in the matchups described below.


1 _._ Implementa 9-plyheuristicminimaxtic-tac-toe player,i.e. ituses


the heuristic evaluation function described above and a search


depth of _N_ = 9 (which happens to be the full tree). Then, run


it against the perfect minimax player that you created previously.


Every game should result in a tie.


2 _._ Implement a 2-ply heuristic minimax tic-tac-toe player. Then,


run it against your 9-ply heuristic player, as well as a purely


random player. The 2-ply player should do better than the


random player but worse than the 9-ply player.


376


_Introduction to Algorithms and Machine Learning_


3 _._ Develop a heuristic minimax connect four player that uses as


many ply as can be computed quickly, and verify that it performs


better than a random player.


4 _._ Verify that your heuristic minimax connect four player performs


better than a “last-minute” player that moves randomly unless


it has an opportunity to capture a win or block a loss on the


next move. (If it doesn’t, then you may need to improve your


heuristic.)


5 _._ Play against your heuristic minimax connect four player yourself.


377


_Justin Skycak_


378


# **40. Introduction to Blondie24** **and Neuroevolution**

Previously, we built strategic connect four players by constructing a


pruned game tree, using heuristics to rate terminal states, and then


applying the minimax algorithm. This was a combination of game

specific human intelligence (heuristics) and generalizable artificial


intelligence (minimax on a game tree).

## **Blondie24**


In the 1990s, a researcher named David Fogel managed to automate


the process of rating states in pruned game trees without relying


on heuristics or any other human input. In particular, he and his


colleague Kumar Chellapilla created a computer program that achieved


expert level checkers-playing ability by learning from scratch. They


played it against other humans online under the username Blondie24,


pretending to be a 24-year old blonde female college student.


379


_Justin Skycak_


Blondie24 was particularly noteworthy because other successful game

playing agents had been hand-tuned and/or trained on human-expert

strategies. Unlike these agents, Blondie24 learned _without_ having any

access to information on human-expert strategies.


To automate the process of rating states in pruned game trees, Fogel


turned it into a regression problem: given a game state, predict its value.


Of course, the regression function is pretty complicated (e.g. changing


one piece on a chess board can totally change the outcome of the game),


so the natural choice was to use a neural network.


However, the usual method of training a neural network,


backpropagation, does not work in this setting. Backpropagation relies


on a dataset of pairs of inputs and outputs – which means that the


model would need a data set of game states along with their correct


rating, totally defeating the purpose of getting the model to learn


this information from scratch. In this setting, the only feedback the


computer gets is at the very end of the game, whether it won or lost (or


tied).

## **Neuroevolution**


To get around this issue, Fogel trained neural networks via **evolution**,

which is often referred to as **neuroevolution** in the context of neural

networks. Starting with a population of many neural networks with


random weights, he repeatedly


1 _._ played the networks against each other,


380


_Introduction to Algorithms and Machine Learning_


2 _._ discarded the networks that performed worse than average,


3 _._ duplicated the remaining networks, and then


4 _._ randomly perturbed the weights of the duplicate networks.


This is analogous to the concept of evolution in biology in which weak


organisms die and fit organisms survive to produce similar but slightly


mutated offspring. By repeatedly running the evolutionary procedure,


Fogel was able to evolve a neural network whose internal mapping from


input state to output rating caused it to play the game of checkers in an


intelligent way, without any sort of human input.

## **Exercise: Evolving a Neural Network** **Regressor**


Before we reimplement Fogel’s papers leading up to Blondie24, let’s


first gain some experience with neuroevolution in a simpler case. As a


toy problem, consider the following data set:


381


_Justin Skycak_





We will fit the above data using a neural network regressor with the


following architecture:


   - _Input Layer:_ 1 linearly-activated node and 1 bias node


   - _First Hidden Layer:_ 10 tanh-activated nodes and 1 bias node


   - _Second Hidden Layer:_ 6 tanh-activated nodes and 1 bias node


   - _Third Hidden Layer:_ 3 tanh-activated nodes and 1 bias node


   - _Output Layer:_ 1 tanh-activated node


Remember that hyperbolic tangent function is defined as


tanh _x_ = _[e][x][ −]_ _[e][−][x]_

_e_ _[x]_ + _e_ _[−][x]_ _[.]_


382


_Introduction to Algorithms and Machine Learning_


To train the neural network, use the following evolutionary algorithm


(which is based on the Blondie24 approach):


1 _._ Create a population of 15 neural networks with weights


randomly drawn from [ _−_ 0 _._ 2 _,_ 0 _._ 2] _._ Additionally, assign a


mutation rate to each net, initially equal to _α_ = 0 _._ 05 _._


2 _._ Each of the 15 parents replicates to produce a single child. The


child is given mutation rate




~~�~~
2 ~~_[√]_~~
_α_ [child] = _α_ [parent] _e_ _[N]_ [(0] _[,]_ [1)] _[/]_



_|W_ _|_



and weights


parent
_wij_ [child] = _wij_ + _α_ [child] _N_ (0 _,_ 1) _,_


where _N_ (0 _,_ 1) is a random number drawn from the standard


normal distribution and _|W_ _|_ is the number of weights in the


network. Be sure to draw a different random number for each


instance of _N_ (0 _,_ 1) _._


3 _._ Compute the RSS for each net and select the 15 nets with the


lowest RSS. These will be the parents in the next generation.


4 _._ Go back to step 2.


Make a plot of the average RSS at each generation, run the algorithm


until the graph levels off to nearly 0 _,_ and then plot the regression curves


corresponding to the first and last generations of neural networks on a


graph along with the data.


383


_Justin Skycak_


(The regression curve plot will contain 60 different curves drawn on


the same plot: one curve from each of the 30 nets in the first generation,


and one curve from each of the 30 nets in the last generation.)


The first generation curves will not fit the data at all (they will appear


flat), but the final generation of regression curves should fit the data


remarkably well. Note that the training process may require on the


order of a thousand generations.

## **Exercise: Hyperparameter Tuning**


Once you’ve got this working, try tuning hyperparameters to get the


RSS to converge to nearly 0 as quickly as possible. You can tweak the


mutation rate, initial weight distribution, number of neural networks,


and neural network architecture (i.e. number of hidden layers and their


sizes).

## **Visualization**


Courtesy of Maia Dimas, below is an illustration of the first and last


generations ofneuralnets,along witha graphofRSS versus the number


of generations.


384


_Introduction to Algorithms and Machine Learning_


Courtesy of Elias Gee, below some intermediate illustrations of a small


population (10 nets) as theylearn to fitthe curve overmanygenerations.


385


_Justin Skycak_


386


_Introduction to Algorithms and Machine Learning_


387


_Justin Skycak_


388


# **41. Reimplementing Fogel’s** **Tic-Tac-Toe Paper**

The goal of this section is to reimplement the paper _Using Evolutionary_


_Programming to Create Neural Networks that are Capable of Playing_

_Tic-Tac-Toe_ by David Fogel in 1993. This paper preceded Blondie24,

and many of the principles introduced in this paper were extended


in Blondie24. As such, reimplementing the paper provides good


scaffolding as we work our way up to reimplement Blondie24.


The information needed to reimplement this paper is outlined below.


389


_Justin Skycak_

## **Neural Network Architecture**


The neural net consists of the following layers:


   - _Input Layer:_ 9 linearly-activated nodes and 1 bias node


   - _Hidden Layer: H_ sigmoidally-activated nodes and 1 bias node

( _H_ is variable, as will be described later)


   - _Output Layer:_ 9 sigmoidally-activated nodes

## **Converting Board to Input**


A tic-tac-toe board is converted to input by flattening it into a vector


and replacing X with 1 _,_ empty squares with 0 _,_ and O with _−_ 1 _._


For example, given a board







X O □







□ X O



 _,_




       -        -        

we first concatenate consecutive rows to flatten the board into the


following 9-element vector:


_⟨_ X _,_ O _,_          - _,_          - _,_ X _,_ O _,_          - _,_          - _,_          - _⟩_ _,_


390


_Introduction to Algorithms and Machine Learning_


Then, we replace X with 1 _,_ empty squares with 0 _,_ and O with _−_ 1 to


get the final input vector:


_⟨_ 1 _, −_ 1 _,_ 0 _,_ 0 _,_ 1 _, −_ 1 _,_ 0 _,_ 0 _,_ 0 _⟩_

## **Converting Output to Action**


The output layer consists of 9 nodes, one for each board square. To


convert the output values into an action, we do the following:


1 _._ Discard any values that correspond to a board square that has


already been filled. (This will prevent illegal moves.)


2 _._ Identify the empty board square with the maximum value. We


move into this square.

## **Evolution Procedure**


The initial population consists of 50 networks. In each network,


the number of hidden nodes _H_ is randomly chosen from the range


_{_ 1 _,_ 2 _, . . .,_ 10 _}_ and the initial weights are randomly chosen from the


range [ _−_ 0 _._ 5 _,_ 0 _._ 5] _._


391


_Justin Skycak_

## **Replication**


A network replicates by making a copy of itself and then modifying the


copy as follows:


   - Each weight is incremented by _N_ (0 _,_ 0 _._ 05 [2] ) _,_ a value drawn from


the normal distribution with mean 0 and standard deviation


0 _._ 05 _._


   - With 0 _._ 5 probability, we modify the network architecture. If we


modify the architecture, then we do so by randomly choosing


between adding ordeleting a hidden node. Ifwe adda node,then


we initialize its associated weights with values of 0 _._


Note that when modifying the architecture, we abort any decision


that would lead the number of hidden nodes to exit the range


_{_ 1 _,_ 2 _, . . .,_ 10 _}._ More specifically:


   - We abort the decision to delete a hidden node if the number of


hidden nodes is _H_ = 1 _._


   - We abort the decision to add a hidden node if the number of


hidden nodes is _H_ = 10 _._


392


_Introduction to Algorithms and Machine Learning_

## **Evaluation**


In each generation, each network plays 32 games against a near-perfect


butbeatableopponent. Theevolvingnetworkisalwaysallowedtomove


first, and receives a payoff of 1 for a win, 0 for a tie, and _−_ 10 for a loss.


The near-perfect opponent follows the strategy below:





Once the totalpayoff (over 32 games againstthe near-perfectopponent)


has been computed for each of the 100 networks (the 50 parents and


their 50 children), a second round of evaluation occurs to select the


networks that will proceed to the next generation and replicate.


In the second round of evaluation, each network is given a score that


represents how its total payoff (from matchups with the near-perfect


opponent) compares to the total payoffs of some other networks in


393


_Justin Skycak_


the same generation. Specifically, each network is compared to 10


other networks randomly chosen from the generation, and its score


is incremented for each other network that has a lower total payoff.


The top 50 networks from the second round of evaluation are selected


to proceed to the next generation and replicate.


**Note:** The actual paper states that the networks with the highest

performance from the second round of evaluation are selected.


Interpreted formally, it would suggest to only select those network(s)


that had the absolute maximum performance. But this would lead the


generationstorapidlyshrinkinsize,resultinginprematureconvergence.


The informal interpretation (top 50 networks) leads the generation


sizes to stay the same, which avoids the issue.


394


_Introduction to Algorithms and Machine Learning_

## **Performance Curve**


Generate a performance curve as follows:


1 _._ Run the above procedure for 800 generations, keeping track of


the maximum total payoff (i.e. the best player’s total payoff) at


each generation.


2 _._ Then repeat 19 more times, for a total of 20 trials of 800


generations each.


3 _._ Finally, plot the mean maximum total payoff (averaged over the


20 trials) as a function of the number of generations.


The resulting curve should resemble the following shape:


Once you’re able to generate a goodperformance curve,store the neural


network parameters for the best player from the last generation so that


you can play it against a random player and verify its intelligence. (It


should beat the random player the vast majority of the time.)


395


_Justin Skycak_

## **Debugging: Sanity Checks**


Before you attempt to run the full 20 trials of 800 generations with 50


parent networks in each generation, run a quicker sanity check (say, 5


trials of 50 generations with 10 parent networks in each generation) to


make sure that the curve looks like it’s moving in the correct direction


(upward).


Given the complexity of this project, your plot will likely not come out


correct the first time you try to run it, even if you feel certain that you


have correctly implemented the specifications of the paper.


If and when this happens, you will need to add plenty of validation to


your implementation. A non-exhaustive list of validation checks and


unit tests are provided below forthe first half of the paperspecifications.


You will need to come up validation checks for the second half on your


own.


1 _._ Each generation, check that each individual neural network has


a valid number of nodes in each layer.


2 _._ Whenever you convert a board to input for a neural network,


check that the resulting entries are all in the set _{−_ 1 _,_ 0 _,_ 1 _}_ add


up to 0 before the neural network player makes its next move.


3 _._ Create a unit test takes a variety of possible board states and


output vectors from the neural network and then verifies that


the player makes the appropriate move.


396


_Introduction to Algorithms and Machine Learning_


4 _._ Check that the initial weights are between _−_ 0 _._ 5 and 0 _._ 5 _,_ no


weightstays the same afterreplication,some weights increase and


some weights decrease after replication (i.e. they don’t all move


in the same direction), and no weight changes by more than 0 _._ 3


(which is 6 standard deviations).


5 _._ Check that after replication, some networks have an additional


hidden layer node, other networks have one less hidden layer


node, and other networks have an unchanged number of hidden


layer nodes.


6 _._ _. . ._


If the plot still doesn’t look right even after your sanity checks are


implemented and passing, then create a log of the results using the


template shown below.


(Sometimes there can be issues that you don’t anticipate in your sanity


checks, that become apparent when you take a birds-eye view and


manually look at concrete numbers.)


397


_Justin Skycak_

















398


_Introduction to Algorithms and Machine Learning_





















399


_Justin Skycak_


400


# **42. Reimplementing** **Blondie24**

Fogel and Chellapilla’s Blondie24 was published over the course of two

papers. Here we shall address the first paper, _Evolving Neural Networks_

_to Play Checkers without Relying on Expert Knowledge_, published in

1999.


This first version of Blondie24 operated under similar principles as


Fogel’s tic-tac-toe player, described previously. However, there are a


number of important differences that are detailed below.


401


_Justin Skycak_

## **Neural Network Architecture**


The neural net consists of the following layers:


   - _Input_ _Layer:_ 32 linearly-activated nodes and 1 bias node

(checkers board has 64 squares but only half of them are used)


   - _First Hidden Layer:_ 40 tanh-activated nodes and 1 bias node


   - _Second Hidden Layer:_ 10 tanh-activated nodes and 1 bias node


   - _Output Layer:_ 1 tanh-activated node


Additionally, there is a special node called a _piece difference node_ whose

activity is the sum of the 32 input nodes. The piece difference node


connects directly to the output node, bypassing all the layers. The


connection, of course, has a variable weight that is learned by the


network.


In total, there are 1742 weights (including the weight of the piece


difference node).

## **Converting Board to Input**


This is similar to tic-tac-toe in that the player’s own regular pieces are


labeled with 1 _,_ empty squares with 0 _,_ and opponent regular pieces with


_−_ 1 _._ However, the player’s own king pieces are labeled with _K,_ and


402


_Introduction to Algorithms and Machine Learning_


the opponent’s with _−K,_ where _K_ is a variable that is learned by the


network.


An action is chosen via the minimax algorithm using the following


heuristic evaluation function. As the network learns, this heuristic


evaluation function will become more accurate.


1 _._ If a board state is a win or a loss, return 1 or _−_ 1 respectively.


2 _._ Otherwise, pass the board state as input to the neural network


and return the activity of the output node.


The search depth is set to _d_ = 4 to allow for reasonable execution times.

## **Evolution Procedure**


The initial population consists of 15 networks with initial weights


randomly chosen from the range [ _−_ 0 _._ 2 _,_ 0 _._ 2] _,_ mutation rates setto _α_ =


0 _._ 05 _,_ and _K_ = 2 _._ Each network is initialized with the same number


of nodes (as described earlier), which remains constant throughout the


course of evolution (i.e. nodes are not added nor deleted).

## **Replication**


The evolution procedure follows the same rules as those described


previously when evolving neural network regressors.


403


_Justin Skycak_


However, in addition to updating the mutation rate and weights, _K_ is


also updated through the following rule:



_√_
_K_ [child] = _K_ [parent] _e_ _[N]_ [(0] _[,]_ [1)] _[/]_



2



Note that _K_ is constrained to the range [1 _,_ 3] _,_ meaning that


   - if _K_ falls below 1 then it is immediately set to 1 _,_ and


   - if _K_ rises above 3 then it is immediately set to 3 _._

## **Evaluation**


Each of the 30 networks in a generation plays a game of checkers


against 5 other networks randomly selected (with replacement) from


the generation. The network is allowed to move first during each game,


and it receives a payoff of 1 for a win, 0 for a tie, and _−_ 2 for a loss. (A


tie is declared after 100 moves by each player with no winner.)


The 15 networkswiththehighesttotalpayoffsareselectedastheparents


of the next generation.


404


_Introduction to Algorithms and Machine Learning_

## **Performance Curve**


In their paper, Fogel and Chellapilla did not create a curve to


demonstrate performance as a function of number of generations.


Instead, they played their final network against human players online


and demonstrated that it achieved an impressive performance rating.


Here, we will create a performance curve by playing the evolving


networks against an external algorithmic strategy and measuring their


performance. This can be accomplished as follows:


1 _._ Develop a heuristic checkers player by hand that plays slightly


intelligently. It should capitalize on obvious opportunities to


move its pieces forward and jump opponent pieces, but it should


not attempt to plan into the future.


2 _._ During each generation of the evolutionary procedure, before


replication, play each of the 15 parent networks against your


heuristic player and compute the average payoff.


3 _._ Keep evolving new generations until the average payoff levels off.


The resulting plot should show that the average payoff increases with


the number of generations (up to some point), demonstrating the that


the evolving networks are learning to play checkers intelligently.


Keep in mind that your hand-crafted heuristic checkers player is


not actually used during the evolution procedure - it is only used


to measure how the evolved networks perform against an external


405


_Justin Skycak_


opponent. So, anything that the evolving networks "learn" is organic


andself-taught,nottailoredtothespecificsofyourhand-craftedplayer.


406


# **43. Reimplementing** **Blondie24: Convolutional** **Version**

Fogel and Chellapilla followed up their 1999 Blondie24 paper with

another paper, _Evolving an Expert Checkers Playing Program without_

_Using Human Expertise_, published in 2001.

## **Convolutional Layer**


This paper was very similar to the 1999 paper, but it had one key


difference that improved the performance of the evolved players: they

inserted a **convolutional layer** between the input layerand first hidden

layer in their neural network.


407


_Justin Skycak_


   - _Input_ _Layer:_ 32 linearly-activated nodes and 1 bias node

(checkers board has 64 squares but only half of them are used)


   - _**Convolutional Layer:**_ one tanh-activatednode foreach _N ×N_

subsquare ofthe checkers boardwith _N_ = 3 _,_ 4 _,_ 5 _,_ 6 _,_ 7 _,_ 8 _._ These


nodes also receive input from the bias node in the input layer.


Also, this convolutional layer contains 1 bias node that connects


to the next layer.


   - _First Hidden Layer:_ 40 tanh-activated nodes and 1 bias node


   - _Second Hidden Layer:_ 10 tanh-activated nodes and 1 bias node


   - _Output Layer:_ 1 tanh-activated node. Note that this node also

receives input from the piece difference node.


Recall that the checkers board has dimensions 8 _×_ 8 _._ So,there is a single


8 _×_ 8 subsquare(namely,theentireboard). Likewise,therearefour 7 _×_ 7


subsquares, nine 6 _×_ 6 subsquares, sixteen 5 _×_ 5 subsquares, sixteen


5 _×_ 5 subsquares, twenty-five 4 _×_ 4 subsquares, and thirty-six 3 _×_ 3


subsquares. Including the bias node, the total number of nodes in the


convolutional layer is


1 + 4 + 9 + 16 + 25 + 36 + 1 = 92 _._


These nodes receive 945 weights from the input layer (including the


input bias node):


408


_Introduction to Algorithms and Machine Learning_




 - 82
1



2 - - 62

+ 9
2 [+ 1] 2



2 - - 72

+ 4
2 [+ 1] 2



2 
2 [+ 1]



2 - - 42

+ 25
2 [+ 1] 2



2 
2 [+ 1]




  - 52
+ 16



2 - - 32

+ 36
2 [+ 1] 2



= 945


The convolutional layer is also known as a _spatial preprocessing layer_

because it allows the network to perceive spatial characteristics of


the board at different levels of “zoom”. Today, most modern image


classification systems leverage convolutional neural networks.


With the addition of the convolutional layer, the total number of


weights in the Blondie24 neural network increases to 5047 _,_ including


the weight from the piece difference node to the output layer. These


weights are all variable and are learned through the process of evolution.

## **King Value Update**


There was one more minor difference in the 2001 paper. The king value


was updated in a slightly different way:


_K_ [child] = _K_ [parent] + _δ_


where _δ_ is randomly chosen from _{−_ 0 _._ 1 _,_ 0 _,_ 0 _._ 1 _} ._ The updated value


of _K_ is still constrained to range [1 _,_ 3] _._


409


_Justin Skycak_

## **Performance Curve**


Generate a performance curve the same way you did for the


previous (non-convolutional) implementation of Blondie24, playing


your evolved networks against your heuristic strategy. The curve should


look fairly similar but should ideally level off to a slightly higher level of


performance.


410


