class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        cur_node = ListNode

        cur_node = headA

        memory = {}

        while cur_node:
            memory[id(cur_node)] = id(cur_node)
            cur_node = cur_node.next

        cur_node = headB

        while cur_node:
            if id(cur_node) in memory:
                return cur_node
            else:
                cur_node = cur_node.next