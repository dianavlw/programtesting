
# is_unique

# def is_unique(str):
#     arr = [False] * 128
#     for char in str:
#         index = ord(char)
#         if arr[index]:
#             return False
#         arr[index] = True
#     return True

# def is_unique_sorting(str):
#     sorted_string = sorted(str)
#     last_character = None
#     for char in sorted_string:
#         if char == last_character:
#             return False
#         last_character = char
#     return True

# print(is_unique("yolo") == False)
# print(is_unique("rad") == True)
# print(is_unique("yOlo") == True)


# print(is_unique_sorting("yolo") == False)
# print(is_unique_sorting("rad") == True)
# print(is_unique_sorting("yOlo") == True)

""" 
Given two string, write a method to decide if one is a permutation of the other. 
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

# def is_perm_1(str_1, str_2):
#     str_1 = str_1.lower()
#     str_2 = str_2.lower()

#     if len(str_1) != len(str_2):
#         return False
#     str_1 = ''.join(sorted(str_1))
#     str_2 = ''.join(sorted(str_2))

#     n = len(str_1)
#     for i in range(n):
#         if str_1[i] != str_2[i]:
#             return False
#     return True
# print(is_perm_1(is_permutation_1, is_permutation_2))
# print(is_perm_1(not_permutation_1, not_permutation_2))

"""
    URLify: replace all the spaces with "%20" assume that the string has sufficient space

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

# Driver Code
s = 'Mr John Smith'
size = 13
print(urlify(s, size))
print(urlify2(s, size))