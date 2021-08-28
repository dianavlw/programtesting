"""
class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.array = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def push(self, value, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_full(stack_num):
            raise StackFullError(f"Push failed: stack #{stack_num} is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot pop from empty stack #{stack_num}")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot peek at empty stack #{stack_num}")
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.number_of_stacks:
            raise StackDoesNotExistError(f"Stack #{stack_num} does not exist")

class MultiStackError(Exception):
    """multistack operation error"""

class StackFullError(MultiStackError):
    """the stack is full"""

class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""


"""


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

    def push(self, value):
        self.stack.append(value)
        value = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)
"""
     if not self.stack or value < self.minStack[-1]:
            self.minStack.append(value)
        else:
            self.minStack.append(self.minStack[-1])
        self.stack.append(value)
"""
    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
     
    def getMin(self):
        return self.minStack[-1]


class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        else:
            # if one of the subtree is None, you should return the depth of another subtree.
            # if all of the subtree is not None, you should return the minimum depth of the two subtrees
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1