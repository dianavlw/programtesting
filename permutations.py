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