#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (65.52%)
# Likes:    4993
# Dislikes: 357
# Total Accepted:    1M
# Total Submissions: 1.5M
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
# 
# 
# Constraints:
# 
# 
# 0 <= rowIndex <= 33
# 
# 
# 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]: #type: ignore
        row = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(row) + 1)
            for j in range(len(row)):
                next_row[j] += row[j]
                next_row[j+1] += row[j]
            row = next_row
        return row


        
        
# @lc code=end

