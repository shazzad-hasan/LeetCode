class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None
        
    def getItem(self):
        return self.item 
    
    def getNext(self):
        return self.next 
    
    def setItem(self, newItem):
        self.item = newItem 
        
    def setNext(self, newNext):
        self.next = newNext
        
    def later_node(self, index):
        if index == 0: return self 
        assert self.next 
        return self.next.later_node(index - 1)
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            node = self.head.later_node(index)
            return node.item
        
    def addAtHead(self, val: int) -> None:
        new_node = Linked_List_Node(val)
        new_node.next = self.head 
        self.head = new_node 
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(len(self), val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            return self.addAtHead(val)
        else:
            new_node = Linked_List_Node(val)
            node = self.head.later_node(index-1)
            new_node.next = node.next 
            node.next = new_node 
            self.size += 1
        
    def delete_first(self):
        self.head = self.head.next 
        self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0: 
            return self.delete_first()
        else:
            node = self.head.later_node(index-1)
            node.next = node.next.next
            self.size -= 1

mylist = MyLinkedList()
mylist.addAtHead(1)
mylist.addAtTail(3)
mylist.addAtIndex(1,2)
mylist.get(1)
mylist.deleteAtIndex(1)
print(mylist.get(1))









