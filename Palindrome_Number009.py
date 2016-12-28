# coding:utf-8
__author__ = '王丰宁'
'''
Given a string, find the length of the longest substring without repeating characters.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        newx = x
        s = 0
        while x != 0 :
            s = 10*s + x%10
            x /= 10
        return newx == s

if __name__ == '__main__':
    s = Solution()
    x = 12332
    print s.isPalindrome(x)