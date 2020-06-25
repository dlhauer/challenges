 def getDecimalValue(head: ListNode) -> int:
      val = head.val
      while head:
        head = head.next
        if head:
          val *= 2
          val += head.val
      return val