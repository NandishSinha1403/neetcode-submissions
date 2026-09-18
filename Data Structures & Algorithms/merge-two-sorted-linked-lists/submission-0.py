# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # temp = 
        # if list1.val <= list2.val:
        #     head = list1
        #     if list1.next is not None: 
        #         list1 = list1.next
        #     else 
        #         while(list2 is not None)
        #             head.next = list2
        #             head =head.next
        #             list2 = list2.next

        # else :
        #     head = list2
            
        #     if list2.next is not None: 
        #         list2 = list2.next
        #     else 
        #         while(list1 is not None)
        #             head.next = list1
        #             head =head.next
        #             list1 = list1.next
        #         return

        
        
        
        # while(list1.next != None or list2.next != None):
        #     if (list1.val <= list2.val):
        #         head.next = list1
        #         head =head.next
        #         list1 = list1.next
                
        #     else :
        #         head.next = list2
        #         head =head.next
        #         list2 = list2.next
        # return temp
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            temp = list1
            list1 = list1.next
        else:
            temp = list2
            list2 = list2.next


        head = temp
        while list1 is not None and list2 is not None :
            if (list1.val <= list2.val):
                temp.next = list1
                temp =temp.next
                list1 = list1.next
                
            else :
                temp.next = list2
                temp =temp.next
                list2 = list2.next

        if list1 is None :
            temp.next = list2 
        else :
            temp.next = list1

        return head

