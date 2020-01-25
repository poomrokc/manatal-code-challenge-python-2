# Exercise 2: Randomness Test

by Poompatai Puntitpong

## Task description

In a lottery game, there is a container which contains 50 balls numbered from 1 to 50. The lottery game consists in picking 10 balls out of the container, and ordering them in ascending order. Write a Python function which generates the output of a lottery game (it should return a list). Also describe which unit tests you could implement to test the output of your function.

## Python and external modules used

    -Python 3.7.4
    -Pytest 5.3.4

## Unit testing ideas

I used two method to test my output. They are not tests for true random but I believe they still worth something. First is to make sure that there are no duplicate output in 2000 consecutive calls. Since the chance of that happening is less than 0.001%. The second one is to check for uniform distribution. In 2000 calls each ball should have been selected around 400 times so the most selected ball should not differs from the least called ball more than 100. More explanation and comments and be found in the test file.