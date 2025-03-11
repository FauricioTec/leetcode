#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (80.27%)
# Likes:    17949
# Dislikes: 299
# Total Accepted:    2.4M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        
        def backtracking(index, s=[]):
            sets.append(s)
            for i in range(index, len(nums)):
                backtracking(i+1, s + [nums[i]])
                
        backtracking(0)

        return sets
        
# @lc code=end

