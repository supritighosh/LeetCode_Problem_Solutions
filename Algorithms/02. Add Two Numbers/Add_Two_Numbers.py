#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. 
#You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

# Definition for singly-linked list. 

class ListNode(object): 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next          

def printList(nodeStart): 
    print(nodeStart.val) 
    if nodeStart.next == None: 
        return 
    else: 
        printList(nodeStart.next) 
  
class Solution(object): 
    def addTwoNumbers(self, l1, l2): 
        """ 
        :type l1: ListNode 
        :type l2: ListNode 
        :rtype: ListNode 
        """        
        if l1 == None: 
            return l2 

        if l2 == None: 
            return l1   

        sval = l1.val + l2.val 
        if sval < 10: 
            ansNode = ListNode(sval) 
            ansNode.next = self.addTwoNumbers(l1.next, l2.next) 
            return ansNode 

        else: 
            rval = l1.val + l2.val-10 
            ansNode = ListNode(rval) 
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next)) 
            return ansNode          

lst1 = ListNode(2) 
sec1 = ListNode(4) 
thd1 = ListNode(3)

lst1.next = sec1 
sec1.next = thd1 

lst2 = ListNode(5) 
sec2 = ListNode(6) 
thd2 = ListNode(4) 

lst2.next = sec2 
sec2.next = thd2 

ans = Solution() 

printList(ans.addTwoNumbers(l1=lst1, l2=lst2)) 