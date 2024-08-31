'''

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2
        mergedList = ListNode(0) 
        ret = mergedList
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    mergedList.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    mergedList.next = ListNode(temp2.val)
                    temp2 = temp2.next
            elif temp1:
                mergedList.next = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp2:
                mergedList.next = ListNode(temp2.val)
                temp2 = temp2.next
            mergedList = mergedList.next

        return ret.next