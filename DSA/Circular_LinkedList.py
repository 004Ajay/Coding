# Circular Linked List
# Ref: https://hanisahilole.medium.com/linked-list-cheat-sheet-0d74dee3cb53
# A circular linked list is where the last node points back to the first node, forming a cycle.

# * Advantages: Can traverse indefinitely; useful for applications requiring continuous cycling.
# * Disadvantages: More complex to implement; risk of infinite loops if not handled properly.
# * Use Cases: Implementing round-robin scheduling, buffering applications.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    
    def display(self):
        temp = self.head
        if not temp:
            return
        else: print('(Head)', end=' -> ')
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print('(Head)')

circular_linkedlist = CircularLinkedList()

circular_linkedlist.append(10)
circular_linkedlist.append(20)
circular_linkedlist.append(30)
circular_linkedlist.append(40)
circular_linkedlist.append(50)

circular_linkedlist.display()