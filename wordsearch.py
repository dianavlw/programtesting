"""
    79. Word Search

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
    word = "ABCCED"
    Output: true

"""

class Solution:
    def exist(self,board,word):
        #numb or boards and columns
        ROWS, COLS = len(board), len(board[0])
        #to add all current values, so we dont revisit the same position twice
        path = set()
        #pass in the position that we are at, and current char that were looking for
        def search(r,c,i):
            if i == len(word):
                return True
                #what if we go out of the board, what if the char in our board not equal to the board we are at, we found the wrong character , and what if (r,c) is inside the path set the same position twice
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            #we found the char we looking for so add the location 
            path.add((r,c))
            #look for the depth for search , looking for all four djacent positions, if one returns true then our result will equal true
            res = (search(r+1, c, i+1)) or (search(r-1, c, i+1)) or (search(r, c+1,i+1)) or (search(r, c - 1, i+1))
            #removing the position we just added to the path, we wont visit it again 
            path.remove((r,c))
            return res

    #brute force
        for r in range(ROWS):
            for c in range(COLS):
                if search(r,c,0): return True
        return False
#Time Complexity
# O(n * m * 4^n)
red = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "ABCCED"

print(Solution().exist(board, word))
