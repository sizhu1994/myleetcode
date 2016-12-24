# coding:utf-8
__author__ = '王丰宁'
'''
https://leetcode.com/problems/add-two-numbers/
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def setListNode(n):
    rel = ListNode(0)
    tail = rel
    while True:
        tail.val = n%10
        n /= 10
        if n != 0:
            tail.next = ListNode(0)
            tail = tail.next
        else:
            return rel
def getListNode(l):
    sums = 0
    pows = 1
    while l != None:
        sums += l.val * pows
        pows *= 10
        l = l.next
    return sums



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rel = ListNode(0)
        tail = rel
        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            tail.val = sum % 10
            sum /= 10
            if ( l1 != None ) or ( l2 != None ) or ( sum != 0 ):
                tail.next = ListNode(0)
                tail = tail.next
            else :
                return rel

if __name__ == '__main__':
    s = Solution()
    l1 = setListNode(342)
    l2 = setListNode(465)
    l3 =  s.addTwoNumbers(l1,l2)
    print getListNode(l3)

