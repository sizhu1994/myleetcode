# coding:utf-8
__author__ = '王丰宁'
'''
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasbeen ={}
        for index, value in enumerate(nums):
            if target - value in hasbeen:
                return hasbeen[target-value],index+1
            hasbeen[value] = index + 1


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2, 7, 11, 15],9)
