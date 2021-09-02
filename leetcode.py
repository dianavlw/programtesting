import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

            # Testing
            
"""
        46. Permutations

        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
        Example 1:

        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

class Solution:
    def permute(self, nums):
        result = []
        
        if(len(nums) == 1):
            return [nums[:]] # vs copy() this will make your code slow
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms) #The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
            nums.append(n)
            
        return result

nums = [1,2,3]       
print(Solution().permute(nums)) # expected output = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]


 """
    47. Permutations II

    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
    
    Example 1:
    Input: nums = [1,1,2]
    Output:
            [[1,1,2], [1,2,1],[2,1,1]]

    Thought process:

        1,2,3
        3*2*1 n!
        
        3 permutation: list itself is one
        backtracking
        hashmap
        We have two 1's
        and we have one 2's
        num |cout
        ----------
        1     2
        _________
        2     1
        
        res = []
        perm = []
        count = { n:0 for n in nums}
        for n in nums:
            count[n] += 1

class Solution(object):
    def permuteUnique(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[List[int]]
                
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    count[n] += 1
                    perm.pop()
                    
        dfs()
        return res
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """       
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
#second solution

class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
        for x in range(len(nums)):
            #[2,3]
            #path =[1,_,_]
            self.backtrack(nums[:x] + nums[x+1], path+[nums[x]])

# third solution

def permutations(word):
    if len(word) == 1:
        return [word]
    
    perms = permutations(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:1] + char + perm[i:])

    return result
print(permutations('abs'))



LeetCode - 15 - 3Sum
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

    SOlUTION 1: https://www.youtube.com/watch?v=jzZsG8n2R9A
   TIME: O (nlogn) + o(n) =
    O(n^2)
    SPACE: o(1) or O(N) bcof the sorting
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res
    
    SOLUTION 2: https://www.youtube.com/watch?v=8uWRUyWpy8M&t=316s
        class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        
        for a in range(len(nums) -1):
            if nums[a] > 0: break
            if a > 0 and nums[a] == nums[a-1]: continue
            l, r = a+1, len(nums)-1
            
            while(l < r):
                if nums[a] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[a]+ nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    output.append([nums[a], nums[l], nums[r]])
                    while l > r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l+=1
                    r-=1
        return output
    
    
    
2. Add Two Numbers: https://www.youtube.com/watch?v=wgFPrzTjm7s
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        #one of them could be null, set a digit to v1 to l1 only if l1 is notnull then set it to 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        # compute new digit 
        # edge case with carry 8 + 7 (our carry will be one) our loop will stop and we will 
        # forget about our carry so if our carry is not null continue
            val = v1 + v2 + carry
        # if 15 a two digit num we need to get the carry
            carry = val // 10
        # we only want the ones place
            val= val % 10 
        #insert the value into our new list node()
            cur.next = ListNode(val)
        # update our current to the next one
            cur = cur.next
        # pointers too only if theyre not null

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
       return dummy.next


SOLUTION 2; https://www.youtube.com/watch?v=mAGn6qQTu4g&t=709s

def addTwoNumbers(self, L1, L2):
    dummy = ListNode(0)
    carry = 0
    
    while l1 or l2:
        if l1:
            l1.val = l1.val
        else:
            l1_val = 0
        if l2:
            l2.val = l2.val
        else:
            l2.val = 0
            
        sum_ = l1_val + l2.val + carry
        
        curr.next = ListNode(sum_ % 10)
        cur = cur.next
        carry = sum_ // 10 (integer division to avoid floating value)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if carry:
           curr.next = ListNode(carry)
        
        return dummy
        
        
Binary Tree Maximum Path Sum: https://www.youtube.com/watch?v=Hr5cWUld4vU
    
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
    1
   / \
  2   3
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
  
   -10
   / \
  9   20
      /\
    15  7
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
    
