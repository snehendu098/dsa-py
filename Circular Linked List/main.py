class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = self.head

        if (self.head is not None):
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
        print("next", self.head.next.data)

    def printList(self):
        temp = self.head
        if (self.head is not None):
            while (True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break
        else:
            print("No value")
        print("🚀 Done")

    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.data == value and curr == self.head:
                # case 1: Head is the only element
                if (curr.next == self.head):
                    curr = None
                    self.head = None
                    return
                # case 2: head is not the only element
                else:
                    # traverse and update head -> delete head
                    while(curr.next != self.head):
                        curr = curr.next
                    curr.next = self.head.next
                    self.head = self.head.next
                    curr = None
                    return
            elif (curr.data == value):
                prev.next = curr.next
                curr = None
                return
            prev = curr
            curr = curr.next

    def countNode(self):
        curr = self.head
        count = 0
        if (curr):
            count += 1
            while (curr.next != self.head):
                count += 1
                curr = curr.next
        print(count)


if __name__ == "__main__":
    clist = CircularList()
    clist.push(5)
    print("printing list")
    clist.printList()
    clist.delete(5)
    clist.printList()
    clist.countNode()
