# Katanator
Runs this problem every day to practice a kata problem to solve... 

#usage: python katanator.py

#Example output
Langugage: python, Problem: Implement insert, merge, and quick sort to sort an array of integers.

#Details
When you run Katanator one problem is selected from the file problems.json.  
Maintain a list of ~ 10 problems that can be solved in about 30 minutes.  These should be practice problems intended to sharpen your coding skills.

Katanator also outputs a random language from the file languages.json.
languages.json should include a few languages that you wish to practice.

Each key in the json files have a weight property.  This is used to increase the probability of getting a problem/language that may be a focus of yours.
Note: a weight value of 0 will exclude the key from the selection process.  Useful for disabling a problem/language that you may want to return to in the future.

#Tips for good problems:
Problems should be interesting but manageable.  You should be able to solve them without looking up anything on the internet or relying on code completion.  
For me, repition is key.  If I practice an algorithm once, I will likely forget it.  e.g. if I want to sharpen my graph traversal skills,
I will leave a simple problem that requires a breadth first and depth first search in problems.json for months, that way I encounter it many times. 

#Tips for solving problems:
As a polyglot programmer, it is easy to forget syntax or library usage e.g Ruby's if - elsif vs Python's if - elif.  For me, if I look up syntax on the internet
everytime I get hung up, I never remember it.  Do don't look anything up and don't rely on code completion.

