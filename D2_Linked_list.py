class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

# node1 = Node(2)

# node2 = Node(3)

# node3 = Node(5)

# print(node1.data, node2.data, node3.data)

# class LinkedList():
#     def __init__(self):
#         self.head = None
        
# list1 = LinkedList()
# list1.head = Node(2)
# list1.head.next = Node(3)
# list1.head.next.next = Node(4)

# print(list1.head.data, list1.head.next.data, list1.head.next.next.data)

# print(list1.head, list1.head.next, list1.head.next.next, list1.head.next.next.next)

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None
            
list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

#print(list1.head.data, list1.head.next.data, list1.head.next.next.data)
print(list2.length())
list2.get_element(0)
list2.get_element(1)
list2.get_element(2)
list2.get_element(3)
list2.show_elements()

def reverse(l):
    if l.head is None:
        return
    
    current_node = l.head # 2
    prev_node = None
    
    while current_node is not None:
        next_node = current_node.next # 3
        
        current_node.next = prev_node # None
        
        prev_node = current_node # 2
        current_node = next_node # 3
    l.head = prev_node
    
list3 = LinkedList()
list3.append(2)
list3.append(3)
list3.append(5)
list3.append(9)

reverse(list3)

list3.show_elements()
