# coding:utf-8
__author__ = '王丰宁'
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def setListNode(s):
    rel = ListNode(s[0])
    if len(s) == 1:
        return rel
    tail = rel
    for i in range(1,len(s)):
        tail.next = ListNode(s[i])
        tail = tail.next
    return rel

def getListNode(l):
    s = ''
    while l != None:
        s += l.val
        l = l.next
    return s

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur != None and count != k:
            cur = cur.next
            count += 1
        if count == k :
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                head.next, cur, head = cur, head, head.next
                count -= 1
            head = cur
        return head

if __name__ == '__main__':
    s = Solution()
    l1 = setListNode('123456')
    l2 =  s.reverseKGroup(l1,3)
    print getListNode(l2)