from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        l1_sum = self.listnode_to_int(l1)
        l2_sum = self.listnode_to_int(l2)
        total_node_sum = l1_sum + l2_sum

        sumastr = str(total_node_sum)
        first_node = ListNode(int(sumastr[-1]), next=None)
        current_node = first_node

        for index in range(len(sumastr) - 2, -1, -1):
            next_node = ListNode(int(sumastr[index]))
            current_node.next = next_node
            current_node = next_node

        return first_node

    def listnode_to_int(self, node):
        current_power = 0
        node_sum = 0
        while True:
            node_sum += node.val * 10 ** current_power
            if node.next:
                node = node.next
                current_power += 1
            else:
                break

        return node_sum


# sol = Solution()
# l13 = ListNode(2)
# l12 = ListNode(4, l13)
# l11 = ListNode(3, l12)
# l23 = ListNode(4)
# l22 = ListNode(6, l23)
# l21 = ListNode(5, l22)
# res = sol.addTwoNumbers(l11, l21)
