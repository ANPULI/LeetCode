# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return num2node(node2num(l1) + node2num(l2))


def num2node(num):
    res = ListNode(num % 10)
    tmp = res
    num //= 10
    while num:
        val = num % 10
        tmp.next = ListNode(val)
        tmp = tmp.next
        num //= 10
    return res

def node2num(node):
    return list2num(node2list(node))

def node2list(node):
    res = []
    while 1:
        res.append(node.val)
        if node.next:
            node = node.next
        else:
            break
    res.reverse()
    return res

def list2num(lst):
    N = len(lst)
    res = 0
    for i in range(N):
        power = N - 1 - i
        res += (10 ** power) * lst[i]
    return res