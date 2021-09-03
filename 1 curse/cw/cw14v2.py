import random


class Player:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, value):
        node = Player(value)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while head.next:
                head = head.next
            self.head.next = node
            self.head.

            # old_link = self.head
            # self.head = node
            # self.head.next = old_link

    def get_all(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.value)
            head = head.next
        return nodes
