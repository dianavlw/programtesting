
# 1.1 is_unique

def is_unique(str):
    arr = [False] * 128
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        arr[index] = True
    return True

def is_unique_sorting(str):
    sorted_string = sorted(str)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

# print(is_unique("yolo") == False)
# print(is_unique("rad") == True)
# print(is_unique("yOlo") == True)


# print(is_unique_sorting("yolo") == False)
# print(is_unique_sorting("rad") == True)
# print(is_unique_sorting("yOlo") == True)

""" 
1.2 Given two string, write a method to decide if one is a permutation of the other. 
Can you assume that it isnt a permutation char if one is capital vs a lowercase 
Can you also assume that it doesnt acknoledge spaces making it not a permutation
"""
# Time Complexity : O(n log n)
# Space Complexity : O(1)
# is_permutation_1 = "God"
# is_permutation_2 = "dog"

# not_permutation_1 = "Not"
# not_permutation_2 = "top"

#you can make the strings lower case
# also have to check if the len matches that can be a quick check
#sort them alphabetically 
# also join the str if there are spaces 

def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True
# print(is_perm_1(is_permutation_1, is_permutation_2))
# print(is_perm_1(not_permutation_1, not_permutation_2))

"""
    1.3 URLify: replace all the spaces with "%20" assume that the string has sufficient space

"""

def urlify(s, size):
    s = s[0:size]
    return s.replace(" ", "%20")

def urlify2(s, size):
    new_string = []

    for char in s[0:size]:
        if char == " ":
            temp = "%20"
        else:
            temp = char
        new_string.append(temp)
    converted_string = "".join(new_string)
    return converted_string

# # Driver Code
# s = 'Mr John Smith'
# size = 13
# print(urlify(s, size))
# print(urlify2(s, size))

"""
    1.4 Palindrom Permutation: given a string write a function to check if it is a permutation of a palindrome.  A palindrome is a word which is written the same forwards and backwards EX. 'madam' 'racecar' kayak'. a permutation is an arrangement of letters EX "god" "dog"
"""

# QUESTION : i need to remove the space, as well as make the characters lower case
#  when we have even number of characters example: abab vs odd ababa 
#  if the letter repeats more than once than it is not a palindrome if it only once than it is a palidrome

def is_palindrome_permutation(s):
    s = s.lower().replace(" ", '')

    we want to now make a dictionary to place 
    we need to keep track of the char count

    char_set = {}
    odd_count= 0
    # iterate through the string 

    for char in s:
        if char not in char_set:
            char_set[char] = 1
        else:
            char_set[char] += 1
    
    for item in char_set:
        if char_set[item] % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True



# # Driver Code
# s = 'Tact coa'
# m = 'aljw'
# print(is_palindrome_permutation(s))
# print(is_palindrome_permutation(m))

"""
    1.5 One away: There are 3 types of edits that ca be performed on string: insert character, remove a charater or replace a character. Given two strings, write a function to check if they're one edit(or zero edits) away. 
"""

# replace: pale, bale => true
# insert/delete: ple, pale => true

def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2): #pale, bale replace  the b to p 
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):#ple, pale insert the a
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)  
    return False


def one_edit_replace(s1, s2): #pale, bale replace  the b to p  
    edited = False #nothing was replace 
    for c1, c2 in zip(s1, s2): # zip takes the first itme passes it and is pared and then the second item is paired, if the passed iterators have different lengths the one with least itmes decides the length
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2): #ple, pale insert the a
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

    
# #Driver Code
# print(are_one_edit_different("pale", "ple")) # True 
# print(are_one_edit_different("palks", "pal")) # False
# print(are_one_edit_different("paleabc", "pleabc")) #True
# print(are_one_edit_different("pale", "pas")) #False 



#SOLUTION #2

def oneAwayEqualLength(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            if count > 1:
                return False
    return True

def oneWayDifferent(word1, word2):
    i = count = 0
    
    while i > len(word2):
        if word1[i+count] == word2[i]:
            i += 1
        else:
            count += 1
            if count > 1:
                return False
   return True

def isOneAway(s1, s2):
    s1, s2 = s1.lower(), s1.lower()
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) == len(s2):
        return oneAwayEqualLength(s1, s2)
    elif len(s1) > len(s2):
        return oneAwayDifferent(s1, s2)
    elif len(s1) < len(s2):
        return oneAwayDifferent(s2,s1) 
    
#Driver Code
s1 = 'pales'
s2 = 'pale'
print(isOneAway(s1, s2)

"""
    1.6 Compress String: Given a String, return a string with the characters and the count of the characters ex: "aabbcccc" => a2b2c4. If the compressed string is not smaller than the original string, return the original string.
"""

def stringCompression(string):
    dic = {} #create a dic with char and count the value of the dic 
    newStr = '' #this will contain char and count

    for char in string: #for loop 
        if not char in dic: # if the key is not in the dic then count is 1 if it is then increment the count
            dic[char] = 1
        else:
            dic[char] += 1
    
    for key, value in dic.items(): # iterate through the dic to create new str
        newStr += key 
        newStr += str(value) # value is an integer convert to a string

    if len(string) == len(newStr): # create an if statement to check the len 
        return string
    else:
        return newStr

# print(stringCompression("aabcccccaaa")) # a5b1c5
# print(stringCompression("aabb")) # aabb will return the original string
# print(stringCompression("aaa")) #a3
      
#SOLUTION #2
      
def stringCompression(s):
      s_comp = ""
      count = 1
      for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i -1]:
            count += 1
      else:
            s_comp += s[i+1] + str(count)
            count = 1
      return s_count if len(s_comp) <= len(s) else s
      
      # vs
      
      if len(s) < len(s_comp):
        return s
      else:
        return s_comp
#DRIVER CODE
s = 'abbccc'
print(stringCompression(s))

      
"""
1.7 Rotate Matrix: Given an image represented by N X N matrix, where each prizel 
in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place? 
"""

def rotateCounterClockWise(mat):
      for i in range(len(mat)):
          mat[i] = mat[i][::-1]
      
      for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
     return mat
      
      
def rotateClockWise(mat):   
      for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
      
      for i in range(len(mat)):
          mat[i] = mat[i][::-1]
      
      return mat
      
      
#DRIVER CODE

 mat = [[1,2,3], [4,5,6], [7,8,9]]
 print(mat)
 
 print(rotateCounterClockwise(mat))
 mat = [[1,2,3], [4,5,6], [7,8,9]]
 print(rotateClockwise(mat))
      
      
       
"""
1.8 Zero Matrix: Write an algorithm such that if an element in the M xN matrix is 0, 
its entire row and column are set to 0.
https://www.youtube.com/watch?v=loMUFyjROW4&list=PLe3prZPgkqR1ddczYNwC24IxA_EwBbbjw&index=16
O(M +N)
"""     
 
def setZeroes(matrix):
      row_arr = [1] * len(matrix)
      col_arr = [1] * len(matrix[0])
      
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_arr[i], col_arr[j] = 0, 0
      
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):    
           if row_arr[i] == 0 or col_arr[j] == 0:
             matrix[i][j] = 0
     
      return matrix
      
      
      
# O(1) contast space
def setZeroes(matrix):
    col0 = 1
      
    for i in range(0, len(matrix)):
      if(matrix[i][0] == 0): col0 = 0
      for j in range(1, len(matrix[i)):
        if matrix[i][j] == 0:
            matrix[0][j] = matrix[i]= 0
                                   
    for i in reversed(0, len(matrix)):
      for j in reversed(range(1, len(matrix[i))):
        if matrix[i][j] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0
        if (col0 == 0): mat[i][j] = 0 
    
   return matrix
                                 
      
 #https://www.youtube.com/watch?v=8cxpwEjeElY&list=PLe3prZPgkqR1ddczYNwC24IxA_EwBbbjw&index=17
                                            
                                            
"""
1.9 String Rotation: Assume you have a method isSubstring which check if one word is a substring of another.
Given two strings, s1, and s2, write code to check if s2 is a rotation of s1 using only 
one call to isSubstring(e.g., 
waterbottle" is a rotation of "erbottlewat"'

"""
def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False
                                            
---------------------------------
                                           
#Solution 2. 
 #Optimize:
  
def isSubstring(s1, s2):
  return (s1 in s2)                                     
      
def rotateString(s1, s2):
  return (len(s1) == len(s2)) and (isSubstring(s2, s1+s1))                                            
                                            
                                            
#a bit longer                                            
                                            
def isSubstring(s1, s2):
  if s1 in s2:
    return True
 else:
    return False                                        
      
def rotateString(s1, s2):
  if len(isSubstring(s2, s1+s1):                     
      return True
  else:    
      return False
      
      
      
#Leetcode 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (len(s) == len(goal) and goal in s+s)         
         
         
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (len(s) == len(goal) and self.isSubstring(goal, s+s)
    def isSubstring(self, string1, string2):
        return (string1 in string2)
      
