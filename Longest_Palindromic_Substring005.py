# coding:utf-8
__author__ = '王丰宁'
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
class Solution(object):
    def palindrome(self,s,left,right):
        while s[left] == s[right] :
            left -= 1
            right += 1
            if left<0 or right >= len(s):
                break
        return s[left+1:right]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxs = ''
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                sm = self.palindrome(s,i,i+1)
                if len(maxs) < len(sm):
                    maxs = sm
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                sm = self.palindrome(s,i,i+2)
                if len(maxs) < len(sm):
                    maxs = sm
        return maxs


if __name__ == '__main__':
    s = Solution()
    l = 'cbbd'
    print s.longestPalindrome(l)
