#insertion in Linked List in Memory
'''
1.At the beginning of the linked list
2.After a node in the middle of linked list
3.At the end of the linked list
'''
class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node=self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

new_linked_list = linkedlist()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
