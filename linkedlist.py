#firstly we create the very simple linked list
#where only one node exist and both head and tail point to that node
#only one node means node have address null

class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
  def __init__(self,value):
    new_node = node(value)
    self.head=new_node
    self.tail=new_node
    self.length = 1

new_linked_list=LinkedList(10)
print(new_linked_list.length) 
