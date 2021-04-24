class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # head = self.head
            # while head.next:
            #     head = head.next
            # self.head.next = node

            old_link = self.head
            self.head = node
            self.head.next = old_link

    def dele(self, value):
        temp = self.head
        while temp:
            old = temp
            if self.head.value == value:
                self.head.next = None
                break
            if temp.next.value == value:
                temp = temp.next
                temp.




    def get_all(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.value)
            head = head.next
        return nodes
