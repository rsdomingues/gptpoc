# Solve the N Queen problem

## Intention
For this test, I wanted to check the ability of chat gpt to solve a complex computational problem, a complex but very known problem, that way I can have a baseline of comparison and can give some feedback on the algorithm structure, etc. These are only my perceptions, not necessarily the full code complexity analysis.

I wanted to keep the instructions simple but more directive this time. Given it is a know computational problem.

I've selected the N Queen problem because it is one of my favorite algorithms, it is a simple solution to a very complex scenario. And it always spoke to me as an engineer.

## Method
To create and run this example I opened the chat gpt online page, and my visual studio code, I was copying code from the page to the visual studio code, since it was the easiest way to do this initial test.

## Prompts
This is the following prompt used and my comments on the code that was generated for me.

> Describe the n queen computational problem
*My goal here was to start from a solid perspective so I wanted to check what chat gpt "understood" as the n queen problem. The description was textbook, which gave a good idea that I did not need to express in detail what are the constraints for this specific problem (I need to test with more domain-specific problems). Let's move on and ask it to create a code to solve this for us. I'll ask it to do a microservice, I want to be able to call this from an API*

> Create a python microservice that can solve the n queen computational problem. Receiving N as a parameter and returning the full matrix of the queen's position.

*The code created was a function on the first try, It used the backtracking algorithm which is trying all combinations and if it fails goes back and tries a different placement. This algorithm is effective but slow on bigger boards. Complexity is around N^N, which is not good, but for my testing, it looked good.

The code was very clear, with well-named variables, clear responsibility methods, and even some small comments to allow me to understand it better. And it had given me the output that I wanted with the full matrix, some code just give the position of the queens, but I wanted to check the full matrix, it made it easier for me to test it out and visually/manually check the result.

There was one part of the algorithm that I did not recognize on the is_valid method, (that I normally call is_safe), it was not fully checking the Diagonals, instead, it was checking an arithmetic correlation between the column and row, I had to think about this, and to my surprise, this is an improvement over the basic algorithm, The correlation of diagonals is always an arithmetic constant, so I can't check on that. After researching this is a common improvement, but I did not remember it. Nice chat gpt.

The only problem was that it did not create this as a microservice, as I requested, but I was so happy with the results that I decided to move on.

As always I need to have proof that it is working using a unit test. So I've asked chat gpt to help me with that.

> create a unit test for the code above
*Again the code generated was easy to read, I liked that it gave me just one test case with multiple subtests to check different scenarios, a way cleaner way to test in this case. Also, I liked how it presented the result in a matrix format, which made it much easier for me to see what it was trying to check, so good code readability.

This time it was not everything great, chatgpt had not included the call unittest.main(), so when I've tried to run the test it did nothing, I've tried 2 or 3 more times, with no different results. So I've decided to add it myself and move forward.

When the test ran, I got that one scenario was broken (the scenario with 8 queens), and I had to check it out. So first of all I printed the results from the algorithm and manually check them, they were fine. I've checked them 3 times just to make sure. So I had to check the test data that it was using and to my surprise the test data was incorrect. This is the matrix it was compared to:*

0:[1, 0, 0, 0, 0, 0, 0, 0],
1:[0, 0, 0, 1, 0, 0, 0, 0],
2:[0, 0, 0, 0, 0, 0, 1, 0],
3:[0, 0, 0, 0, 0, 0, 0, 1],
4:[0, 1, 0, 0, 0, 0, 0, 0],
5:[0, 0, 0, 0, 1, 0, 0, 0],
6:[0, 0, 0, 0, 0, 0, 0, 1],
7:[0, 0, 1, 0, 0, 0, 0, 0]

*There are multiple problems with this test data queens 2 and 3, are on diagonals, queens 3 and 6 are on the same row, and queens 5 and 7 are on diagonals. 

But the algorithm response was great, so I've just adjusted the test data and moved on. But it was fun to see that that chat gpt used different methods to generate the test and the algorithm.

This was a fun experiment, but I wanted to be able to tell chat gpt where I wanted the first queen positioned, that way I can have some more playing with this algorithm*

> change the original algorithm to allow me to inform the position of the first queen

*The ability of chat gpt to understand the context and use previous answers is very good, it understood my input and did the exact change I was expecting it to do.

More than that, I've noticed now that it did a defensive move and added a null condition for the first queen, that was interesting to notice since in my previous interaction with it, it had not done that (division by zero).

I've tested the code manually and it was working fine, the adjustment worked as I expected since I've only locked 1 queen, and the algorithm is always able to respond, it basically will end up swapping rows, if we lock more than 1 we can have scenarios with no solution

To wrap it up I wanted to check the test case. No surprise there, it generated 3 subtests (good structure on the code), but again the test data for the 8 queens was bad. I've just done it manually and considered this interaction done.*


## My considerations

This was a fun exercise I got to remember solutions for this fun problem and also was able to learn a new optimization from it. Which I was not expecting to, not on this know problems.

The generated code was very clean, and easy to understand, good namings for variables and methods/functions helped a lot and gave a sense of security to the code that I was presented to. Even the way it handled the scenarios was very easy to read. I have read much worst code and even generated the worst code sometimes.

The fact that the test date was not good, was something weird, but at the same time it gave some security in the sense that it was not using the algorithm it had generated to generate the response of the test, it had generated it separately, which is a good thing, considering it could have created a bad algorithm.

The other topic is that I asked it to create a microservice for me, but it had not done that specific part, it is not a very complex item, and I'm sure with two more prompts I could have done it. But I decided not to for this test. 

In general, I was impressed with the quality of the code in a more complex scenario, but still, the developer was necessary here, to take a look at what was generated and make sure we could count on the result.

It took me less than 10 minutes to reach the end of my test. But I have to be honest if I went to solve this problem without help from Google, It would have taken me easily a 1hr to remember the paths, and I'll probably have ended up with a less optimized solution. That is why I know the overall solution to this problem, but if someone does not know it can take a lot more (In college it took me almost 1 week to sort this out, it was one of my first attempts to use recursion but still).

I found this very interesting, that chat gpt can help us with complex problems in our day to day, it can help us to solve problems but more than that learn faster. One topic that is still in my mind is that we need the engineer here, not only to properly create the prompts but also to evaluate the results, there were elements that I had to change on the test code, to make sure it was working, and I had to take a look at algorithm also. 

So far great results!