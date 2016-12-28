# coding:utf-8
__author__ = '王丰宁'
'''
Given a string, find the length of the longest substring without repeating characters.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lstsstr = ''
        left = 0
        cache = {}
        for index,value in enumerate(s):
            if value in cache and cache[value] >= left:
                left = cache[value] + 1
            cache[value] = index
            if len(lstsstr) < index - left + 1 :
                lstsstr = s[left:index+1]
        return lstsstr


if __name__ == '__main__':
    s = Solution()
    l = 'pwwkew'
    print s.lengthOfLongestSubstring(l)

