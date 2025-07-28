'''
#Linked List are majorly used for Undo/Redo functionality in Apps, Back/Forward history in Web browsers and 
memory management in OS level, Music/video playlist Etc....'''
#insertAtBeginning()
#insertAtIndex()
#insertAtEnding()

#update_node()

#remove_first_node()
#remove_last_node()
#remove_index_node()
#remove_value_node()

#size_of_ll()
#display_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            new_node = Node(data)
            new_node.next =current_node.next
            current_node.next = new_node
        else:
            print('Index Not Present!')
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is  None:
            self.head = new_node
            return 
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def updateNode(self, val, index):
        current_node = self.head
        position = 0 
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print('Index Not Present!')
            
    def remove_First_Node(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def remove_Last_Node(self):
        if self.head is None:
            return
        
        #If there is only one Node
        if self.head.next is None:
            self.head = None
            return  
         
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        
        
    def remove_index_node(self, index):
        if self.head is None:
            return
        current_Node = self.head
        position = 0
        if index == 0:
            self.remove_First_Node()
        else:
            while current_Node is not None and position < index - 1:
                position += 1
                current_Node = current_Node.next
            if current_Node is None or current_Node.next is None:
                print('Index not present')
            else:
                current_Node.next = current_Node.next.next
                
    def remove_value_node(self, data):
        current_node = self.head
        
        if current_node is not None and current_node.data == data:
            self.remove_First_Node()
            return
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next =current_node.next.next
                return
            current_node = current_node.next
        print("Node with the given data not found") 

        
    def size_Of_ll(self):
        size = 0
        current_node =self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
       
    def display_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



ll = LinkedList()

print("Node Data: ")
ll.insertAtBeginning('A')
ll.insertAtBeginning('B')
ll.insertAtBeginning('G')
ll.insertAtIndex('C',0)
ll.display_list()

l = ll.size_Of_ll()
print('Length of the List:',l)

print('\nUpdating a node: ')
ll.updateNode('e',0)
ll.display_list()

print('\nremoving first Node in List: ')
ll.remove_First_Node()
ll.display_list()

print('\nremoving Last Node in List: ')
ll.remove_Last_Node()
ll.display_list()

print('\n removing by index value')
ll.remove_index_node(0)
ll.display_list()

print('\nremoving by values')
ll.remove_value_node('B')
ll.display_list()

l = ll.size_Of_ll()
print('Length of the List:',l)
