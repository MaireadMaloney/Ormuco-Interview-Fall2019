# Ormuco-Interview-Fall2019
Interview questions answered for Ormuco job application.

To answer questions A and B, I made files qa.py and qb.py. These can be run with the command python qa.py or qb.py in your terminal. When you run these files, the terminal will prompt you to enter information (line segments for qa, version numbers for qb). They allow
you to test my code with any input you desire! I also made a test file, where I call the methods that compute the result only, from qaTest.py and qbTest.py using various test values (these files contain the same methods as their qa.py and qb.py counterparts, however they do not ask for any user inputs). 

## Question A: Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
To answer this question I wrote an overlap method that simply checks the values of the points that creates the line segnments in order to see if they overlap. There is more info on this in the qa.py comments. 
Before doing so however, I do check to make sure x1 is smaller than x2 and x3 is smaller than x4, to make sure the test or user line segments follow the typical (x1, x2) notation.

 

## Question B: The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
For this question, I first wrote a method that eliminates the "." in the version string. From there, I compare the length of the strings, in order to know how many digits (var eF) are in each version number. Once this is done, I cast the strings to ints and multiply them by a factor of
10 which makes each the same number of digits (the one with less digits originally will have 0s at the end). Finally, I compare the value of the 2 ints. The larger value is the most recent/the greater version, I return a string where this is declared.


## Question C: At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
    1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire 

For question C, I was quite stumped as I have never dealt with caches before, let alone implementing one. However, with alot of Googling and using my understanding of data structures,
I was able to implement a basic LRU-Cache which returns an error message if it takes more than a certain amount of time for the insert or retrieve operations to complete. This code is written
in Java as the question was more difficult and Java was the language I learned data structures with. I did not attempt to find a solution for geo-distribution or real-time writes. I am very eager to 
learn more about how to implement such features at Ormuco! Perhaps I could start by learning my way around Docker and Kubernetes as a first step towards this part of the problem.

Thanks again for your consideration of my application!

Mairead Maloney
 


