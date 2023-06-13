from src.ListNode import ListNode
class LinkedListNumberAdder(object):
    def addTwoNumbers(self, l1, l2):
        head_l1 = l1
        num1 = 0
        index = 0
        while (head_l1 is not None):
            num1 += head_l1.val * pow(10, index)
            index += 1
            head_l1 = head_l1.next
        head_l2 = l2
        num2 = 0
        index = 0
        while (head_l2 is not None):
            num2 += head_l2.val * pow(10, index)
            index += 1
            head_l2 = head_l2.next
        num = num1 + num2
        num_list = [int(x) for x in str(num)]
        num_list.reverse()
        head = None
        for x in num_list:
            node = ListNode(x)
            if (head is None):
                head = node
                continue
            else:
                self.attachToNext(head, node)
        return head
    
    def attachToNext(self, node, new_node):
        if (node.next is None):
            node.next =  new_node
        else:
            self.attachToNext(node.next, new_node)               