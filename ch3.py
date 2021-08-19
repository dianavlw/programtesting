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

    def pop(self):
        #the last stack and the last element [-1][-1]
        # you can pop from an empty stack ex. [1,2][] the second stack is empty 
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        else: # hold the last element
            #[6,7,8],[9,10], len is 1 delete the whole stack  
            popped_data = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stack[-1]
            else:
                #[[1,2,3], [4,5,6][7,8,9]]
                #New Array [[1,2,3],[4,5,6],[7,8]]
                del self.stacks[-1][-1]
            return popped_data


"""
 3.1 Min Stack
 Youtube video for reference from NeetCode: https://www.youtube.com/watch?v=qkLl7nAwDPo
 Github Cracking the coding interview:  https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_03/p02_stack_min.py

 ALso Algo Expert is a great source to have Ive been using it and its been great learning resource: https://www.algoexpert.io/questions/Min%20Max%20Stack%20Construction
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def pust(self, value):
        self.stack.append(value)
        value = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
     
    def getMin(self):
        return self.minStack[-1]
