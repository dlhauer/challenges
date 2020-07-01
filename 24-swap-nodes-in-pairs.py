 def swapPairs(self, head: ListNode) -> ListNode:
      head = ListNode(0, head)
      prev = head
      cur_node = head.next
      while cur_node and cur_node.next:
        next_node = cur_node.next
        cur_node.next = next_node.next
        next_node.next = cur_node
        prev.next = next_node
        prev = cur_node
        cur_node = cur_node.next
      return head.next
        