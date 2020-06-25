def middleNode(self, head: ListNode) -> ListNode:
      follow = head
      front = head.next
      while front:
        front = front.next
        if front:
          front = front.next
        follow = follow.next
      return follow
      