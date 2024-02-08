#types of linked list
'''
-singly linked list
-circular singly linked list
-doubly linked list
-circular doubly linked list

singly linked list = singly linked list head have address of first node and at last tail have address of last node
and last node have null value in address.

circular singly linked list=in circular linked list last node have address of first node
head=first node
tail=last node.

doubly linked list=in doubly linked list node have 1 value and 2 address where 1 address show previous one and 
2 address shoe second one and last node have null value in 2 address.

circular doubly linked list=in circular doubly linked list last node 2 address have first node address.

'''
class node:
    def __init__(self,value):
        self.value=value
        self.next=None

new_node = node(10)
print(new_node.value)
