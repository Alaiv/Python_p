class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        count = 1
        element = self.head
        while count <= position:
            if count == position:
                return element
            if element.next is None:
                return None
            element = element.next
            count += 1
        return None

    def insert(self, new_element, position):
        count = 1
        elem = new_element
        prev = None
        val = self.head

        while count < position:
            if count == position - 1:
                prev = val
            val = val.next
            count += 1

        prev.next = elem
        elem.next = val

    def delete(self, value):
        check = True
        val = self.head
        deleted = None

        if value == val.value:
            deleted = val.value
            self.head = val.next
            check = False

        while check:
            if val.next.value == value:
                deleted = val.next.value
                val.next = val.next.next
                check = False
            val = val.next

        return deleted
