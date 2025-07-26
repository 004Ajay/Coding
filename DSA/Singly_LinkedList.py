# ## Singly Linked List
# Ref: https://hanisahilole.medium.com/linked-list-cheat-sheet-0d74dee3cb53
# Each node contains data and a reference to the next node in the sequence. It is unidirectional, meaning traversal is only possible in one direction.

# * Advantages: Uses less memory than doubly linked lists.
# * Disadvantages: Cannot traverse backward; searching requires O(n) time.
# * Use Cases: Implementing stacks and queues.

# ## My notes
# 

class Node:
    """This class creates nodes.A typical singly linkedlist node => [ data | next ]

    Each node has:
    * data: the actual value (eg, 10, 20, etc.)
    * next: a pointer (or link) to the next node in the list. Initially, it's set to 'None' because we don't know the next node yet.
    """
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
    
    def append(self, data):
        new_node = Node(data)
        if not self.head: # if list is empty
            self.head = new_node # set head to this new node
            return
        temp = self.head
        while temp.next: # go to the last node
            temp = temp.next
        temp.next = new_node # link the last node to the new node
    
    def display(self, prefix_txt: str=None):
        if prefix_txt:
            print(prefix_txt, end=" ")

        if self.head == None:
            print("None")
        else:    
            temp = self.head
            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next
            print("None")

print("\n--- SINGLY LINKEDLIST ---\n")

singly_linked_list = SinglyLinkedList()

singly_linked_list.display(prefix_txt="LinkedList without data:")

singly_linked_list.append(10)
singly_linked_list.append(20)
singly_linked_list.append(30)
singly_linked_list.append(40)
singly_linked_list.append(50)

singly_linked_list.display(prefix_txt="LinkedList with data:")