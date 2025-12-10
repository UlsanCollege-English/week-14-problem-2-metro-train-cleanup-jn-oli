class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_cars(head, target):
    """
    Remove all nodes whose value equals target.
    Return the new head of the linked list.
    """

    # Skip all leading nodes equal to target
    while head is not None and head.value == target:
        head = head.next

    # If list becomes empty
    if head is None:
        return None

    current = head

    # Traverse and remove nodes
    while current is not None and current.next is not None:
        if current.next.value == target:
            current.next = current.next.next   # skip the node
        else:
            current = current.next

    return head
