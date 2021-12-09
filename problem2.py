class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        a = list()
        a1 = list()
        t = list()
        b = ""
        b1 = ""
        while l1 or l2:
            if l1:
                a.append(l1.val)
                l1 = l1.next
            if l2:
                a1.append(l2.val)
                l2 = l2.next
        a.reverse()
        a1.reverse()

        for i in a:
            b = str(b) + str(i)
        for i in a1:
            b1 = str(b1) + str(i)

        c = int(b) + int(b1)
        c = str(c)
        t[:] = c
        t.reverse()

        t = list(map(int, t))
        return t[:]
