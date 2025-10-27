class double_node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# তিনটা নোড তৈরি
a = double_node(10)
b = double_node(20)
c = double_node(30)

# নোডগুলো লিঙ্ক করা
a.next = b
b.prev = a
b.next = c
c.prev = b

head = a  # প্রথম নোড
tail = c  # শেষ নোড

# --- Forward traversal ---
def traverse_forward(head):
    curr = head
    print("Forward Traversal:")
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")

# --- Backward traversal ---
def traverse_backward(tail):
    curr = tail
    print("\nBackward Traversal:")
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.prev
    print("None")

# --- Function call ---
traverse_forward(head)
traverse_backward(tail)

