class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push_right(self, val):
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail = self.head
            self.tail.next = node

            node.prev = self.head
            self.head = node

        self.size += 1

    def pop_right(self):
        if self.head is None:
            raise ValueError("nothing in head. need to push")
        val = self.head.val
        self.size -= 1

        self.head = self.head.prev

        return val

    def push_left(self, val):
        node = Node(val)
        if self.size > 0:
            node.next = self.tail
        self.tail = node

        self.size += 1

    def pop_left(self):
        if self.tail is None:
            raise ValueError("nothing in tail. need to push")
        val = self.tail.val

        self.tail = self.tail.next

        self.size -= 1
        return val


if __name__ == "__main__":
    d = Deque()
    val1 = "first"
    val2 = "second"

    # test basic push/pop right (stack semantics)
    assert d.size == 0
    d.push_right(val1)
    assert d.size == 1
    d.push_right(val2)
    assert d.size == 2
    assert d.pop_right() is val2
    assert d.size == 1
    assert d.pop_right() is val1
    assert d.size == 0

    print("ok1")
    # raise Exception("done")

    # test basic push/pop left (stack semantics on other side)
    d.push_left(val1)
    assert d.size == 1
    d.push_left(val2)
    assert d.size == 2
    assert d.pop_left() is val2
    assert d.size == 1
    assert d.pop_left() is val1
    assert d.size == 0
    # raise Exception("done")

    # test push right, pop left side (queue semantics)
    d.push_right(val1)
    d.push_right(val2)
    assert d.pop_left() is val1
    assert d.pop_left() is val2
    assert d.size == 0
    # raise Exception("done")

    # test push left, pop right side (queue semantics)
    d.push_left(val1)
    d.push_left(val2)
    assert d.pop_right() is val1
    assert d.pop_right() is val2
    assert d.size == 0
    print("ok")
