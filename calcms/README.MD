# Microservice to execute basic arithmetic functions

## Intention
Create a simple python microservice that can solve base arithmetic operations. For this scenario I'll try to be as vague as possible, I want to test the capacity of chatgpt not only to solve the problem but to understand what I need.

## Method
To create and run this example I opened the chatgpt online page, and my visual studio code, I was coping code from the page to the visual studio code, since it was the easiest way to do this initial test.

## Prompts
This is the following prompt used and my comments on the code that was generated for me.


> Create a python microservice that is able to execute aritimetic operations in two numbers that are received as path parameters and return a json with the two inputs and the result

*The code that was generated solved the base scenarios for all operations, to be sure I had to create the unit test, lets's see what chat get can generate as a unit test*

> Create unit test for this microservice

*The generated unit test covers four basic scenarios, but there was no test case for division by zero, and also no case for negative numbers so we had to change that. So I had to change that. The other aspect that I've noticed is that the code is calling the MS live, so it is not setting up a test server, for the purse of this first test I'll leave it be for now*

> On the unit test above add the following cases, dividing by zero, add a negative number and multipling two negative numbers

*The ability of chatgpt to understand the specific changes that I want is remarkable, but now we have one problem, the new unit tests are broken, lets ask chatgpt to fix this.*

> On the microservice code add a condition to handle division by zero

*Again the ability to change the specific piece of code was remarkable. it handled very well and just add a condition to validate the division, for this basic element I did not have to describe what was the condition it deducted from the restrictions of base arithmetic functions. now we need to allow it to handle negative numbers*

>change the code to accept negative numbers as input parameters

*This was interesting, Flask has a specific condition to receive negative numbers you have to configure the flask converter to accept signed numbers it is as simple as adding (signed=True) on the converter, but chapgpt did not know or consider this specific element, I've tried multiple times with different prompts, but ultimately I had to add it by hand. And on my final review, I noticed that the program was not accepting decimal points, just integer numbers, a simple limitation, that we can remediate*

>change the parameter to allow decimal numbers also

*The code generated was changed from int to float, but again not added the ability to accept negative numbers, so I've added manually the configuration and moved on. But now the test was to simple not considering floating numbers so I had to ask chatgpt to change our unit test to consider this scenario.*

>change the unit test to now use decimal numbers on the testing

*The final adjustment was executed with no problems on the code but for some reason, I faced a different challenge, I had to ask ChatGpt to generate the response 3 times, due to it not giving me the complete code all the time. I don't know if it was a network issue or a small bug. Anyway, when it was able to generate the complete code everything worked great.*

## My considerations
This was a valid experiment, chatgpt was able to handle my vague inputs like a champ, and it was able to deduct easily the problems that I was talking about, more than that every time it generated the code it also generated the details for me, like install flask dependencies with pip, and a brief explanation of each part of the code. I was very impressed.

There were issues regarding details of implementation, like the ability to consider negative numbers, or not generating some important unit test scenarios. So far I think it is a great tool, but there is still an important component which is the developer behind it to make sure the final results come out as expected.

This scenario took me 10-15m to complete, if I would do it myself I would take at least double that time, considering unit testing, and implementation details. 

Another topic that is worth mentioning is the ability it had to handle typos on the input, I've left them here so you can see, but it understood my intention regardless of it.

So far great results!