# Doubly Linked List
# Ref: https://hanisahilole.medium.com/linked-list-cheat-sheet-0d74dee3cb53
# Each node contains data, a pointer to the next node, and a pointer to the previous node. This allows traversal in both directions.

# * Advantages: Can be traversed forward and backward.
# * Disadvantages: Uses more memory due to extra pointers.
# * Use Cases: Browser history, undo-redo functionality in applications

class DoublyNode:
    """This class creates nodes. A typical doubly linkedlist node => [ prev | data | next ]

    Each node has:
    * data: the actual value (eg, 10, 20, etc.)
    * next: a pointer (or link) to the next node in the list. Initially, it's set to 'None' because we don't know the next node yet.
    * prev: a pointer (or link) to the previous node in the list. Initially, it's set to 'None' because we don't know the previous node yet.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def display(self, prefix_txt: str=None):
        if prefix_txt:
            print(prefix_txt, end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print('None')


print("\n--- DOUBLY LINKEDLIST ---\n")

doubly_linkedlist = DoublyLinkedList()

doubly_linkedlist.display(prefix_txt="LinkedList without data:")

doubly_linkedlist.append(10)
doubly_linkedlist.append(20)
doubly_linkedlist.append(30)
doubly_linkedlist.append(40)
doubly_linkedlist.append(50)

doubly_linkedlist.display(prefix_txt="LinkedList with data:")
