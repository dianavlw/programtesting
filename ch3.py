"""
    Chapter 3 of Cracking coding interview by Gaylee L.

    3.1 Three to one: Describe how you could use a single array to implement three stacks.
    Youtube help video: https://www.youtube.com/watch?v=Mkuhyz6jD1w
    Code help by Colorful Codes : https://colorfulcodesblog.wordpress.com/2018/01/23/stack-of-plates-cracking-the-code-python/
    Cracking the Coding Interview in Python GitHub : https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_03/p01_three_in_one.py

"""

class StackOfPlates:
    def __init__(self, capacity):
        self.stacks = [] # representing an empty stack, list
        if capacity < 1:
            raise NameError("A stack is greater than one.")
        else: 
            self.capacity = capacity
    def push(self, item):
        if self.stack == []:
            self.stacks.append([item]) #nested array 
        else: #else if not empty:
            #creating a new stack adding it to a new stack, checking the last stack to see if it has room
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else: # [[9, 10, newItem]] its going to append it
                self.stacks[-1].append(item)         