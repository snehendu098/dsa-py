class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if(self.head is not None):
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if (prev_node is None):
            print("Prev node can't be none")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        new_node.prev = prev_node

    def addToLast(self, value):
        temp = self.head
        new_node = Node(value)
        new_node.next = None
        if temp is not None:
            while temp.next != None:
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node
        else:
            new_node.prev = None
            self.head = new_node

    def printList(self, node):
        print("🚀 Start")
        if self.head is not None:
            while node is not None:
                print(node.data)
                node = node.next
        else:
            print("No value")
        print("🚀 Finish")
        print("")

    def deleteOperation(self, key):
        if self.head is None or key is None:
            print("No nodes")
            return
        # case 1
        if self.head == key:
            self.head = key.next

        # case 2
        if key.next is None and key.prev is not None:
            key.prev.next = None

        # case 3
        if key.next is not None and key.prev is not None:
            key.next.prev = key.prev
            key.prev.next = key.next


if __name__ == "__main__":
    dlist = DoublyList()
    # dlist.push(5)
    dlist.push(7)
    dlist.push(2)
    dlist.printList(dlist.head)
    dlist.insertAfter(dlist.head.next, 4)
    dlist.printList(dlist.head)
    dlist.addToLast(3)
    dlist.printList(dlist.head)
    dlist.deleteOperation(dlist.head.next.next.next)
    dlist.printList(dlist.head)
