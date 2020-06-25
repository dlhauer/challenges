class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode()
    great_head = ListNode()
    less = less_head
    great = great_head

    while head:
    if head.val < x:
        less.next = head
        less = less.next
    else:
        great.next = head
        great = great.next
    head = head.next

    great.next = None
    less.next = great_head.next
    return less_head.next
