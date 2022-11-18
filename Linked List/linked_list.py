class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        # creating the value
        new_node = Node(new_value)
        # pointing the next value towards null
        new_node.next = self.head
        # pointing the head to the new node
        self.head = new_node

    def insertAt(self, prev_node, new_value):
        if prev_node is None:
            print("Previous node seems to be empty")

        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_node = Node(new_value)

        # check if the linked list is empty or not
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        # traverse through the list
        while(last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def deleteNode(self, key):
        temp = self.head

        # case 1
        if (temp is not None):
            if (temp.data == key):
                # head = next node of the temp
                self.head = temp.next
                temp = None
                return

        # case 2
        while (temp is not None):
            if temp.data == key:
                print("temp data", temp.data)
                break
            prev = temp
            print("previous", prev.data)
            temp = temp.next

        # case 3: Temp is none
        if (temp == None):
            return

        print("Previous 📄", prev.data)
        prev.next = temp.next
        temp = None

    def deleteList(self):
        temp = self.head
        while(temp):
            nextEl = temp.next
            del temp.data
            temp = nextEl

    def getNodeCount(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        print("🦁 Count:", count)
        return count

    def reverseList(self):
        prev = None
        next = None
        curr = self.head

        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            # print("prev")
            curr = next
            # print("next", next)
        self.head = prev

    def convertToCircular(self):
        temp = self.head
        if temp:
            while temp.next is not None:
                temp = temp.next
            temp.next = self.head
            print("done")


if __name__ == "__main__":
    list = LinkedList()

    list.push(3)
    list.append(5)
    list.append(8)
    list.append(7)
    list.insertAt(list.head.next.next, 4)
    print("Before Delete 🚀")
    list.printList()

    list.deleteNode(4)

    print("After Delete 🚀")
    list.printList()

    print("Node Count")
    list.getNodeCount()

    print("🦁 Reversed")
    list.reverseList()
    list.printList()
    list.convertToCircular()
