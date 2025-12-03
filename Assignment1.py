# NAME:OGUNLEYE FAVOUR ADEYOSALA
# MATRIC NO: 230502041

# ==============================
#   LINKED LIST IMPLEMENTATION
#   File type: .py (Python)
# ==============================

# A node is a small container that stores data and a pointer to the next node.
class Node:
    def __init__(self, data):
        self.data = data      # store the value
        self.next = None      # pointer to the next node


# A LinkedList is a sequence of nodes connected by pointers
class LinkedList:
    def __init__(self):
        self.head = None      # start with an empty list

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:    # empty list
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Deleting a node
    def delete_node(self, key):
        temp = self.head

        # Case 1: head is the node to delete
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Case 2: search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    # Displaying list
    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ------------------ Testing the Linked List -------------------

if __name__ == "__main__":

    # Create list
    lst = LinkedList()

    # Insert 5 values
    lst.insert_at_beginning(10)
    lst.insert_at_end(20)
    lst.insert_at_end(30)
    lst.insert_at_beginning(5)
    lst.insert_at_end(40)

    # Delete one value
    lst.delete_node(20)

    # Display final list
    lst.display_list()

    #What is the difference between arrays and linked lists?
    #Array:
#Stored in contiguous memory, fixed size, fast random access but slow insertion/deletion (needs shifting).

#Linked List:
#Stored in non-contiguous memory, dynamic size, fast insertion/deletion but slow random access (must traverse).

#What is the time complexity of insertion in a linked list?

    #O(1) when inserting at the head or when the pointer to the insertion spot is already known.
#O(n) if you must traverse the list to find the location.
#(Write whichever fits the question — but usually they expect O(1).)


#What are the key differences between primitive data types and ADTs?

#Primitive data types: Built-in basic types like int, float, char; store simple values; operations are predefined by the language.
#ADTs (Abstract Data Types):
#Specify what operations can be performed (e.g., push, pop), not how they are implemented. Examples: Stack, Queue, List.

#Why are arrays considered static, and linked lists dynamic?

#Arrays are static because their size is fixed at creation and cannot grow or shrink.

#Linked lists are dynamic because nodes can be added or removed at any time, allowing the structure to grow or shrink as needed.

#In what situations would you prefer a linked list over an array?

#Use a linked list when:
#you expect frequent insertions or deletions, especially at the beginning or middle.
#Memory allocation must be dynamic.
#You don’t need fast random access.
#Examples: playlist manipulation, undo lists, queues with unknown length.

#Give real-world examples where each of the following would be useful:
#a) Stack (LIFO)
#Undo button in MS Word
#Browser back button
#Call stack during function calls
#Stacked plates in kitchen

#b) Queue (FIFO)
#Bank line
#Printer job processing
#Customer service ticket system
#CPU scheduling (Round Robin)

#c) Linked List
#Music playlist where you can add/remove songs anywhere
#Train coaches attached one after the other
#Navigating through browser history (as a doubly linked list)
#To-do apps that allow inserting tasks anywhere