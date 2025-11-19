class Node:
    """
    Represents a single node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the list, or None if it's the last node.
    """
    def __init__(self, data):
        """
        Initializes a new Node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Returns a string representation of the Node for debugging.
        """
        return f"Node({self.data})"

class LinkedList:
    """
    Implements a singly linked list data structure, providing common operations
    like appending, prepending, inserting, deleting, searching, reversing,
    cycle detection, finding middle, removing duplicates, and merging sorted lists.
    """
    def __init__(self):
        """
        Initializes an empty LinkedList.
        """
        self.head = None

    def __str__(self):
        """
        Returns a user-friendly string representation of the linked list.
        e.g., "1 -> 2 -> 3 -> None" or "Empty List"
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None" if elements else "Empty List"

    def __repr__(self):
        """
        Returns a developer-friendly string representation of the linked list.
        """
        return f"LinkedList(head={self.head})"

    def __len__(self):
        """
        Returns the number of nodes in the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        """
        Makes the linked list iterable, yielding the data of each node.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def is_empty(self):
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data):
        """
        Adds a new node with the given data to the end of the linked list.

        Args:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """
        Adds a new node with the given data to the beginning of the linked list.

        Args:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node_data, data):
        """
        Inserts a new node with the given data after the first occurrence
        of a node containing `prev_node_data`.

        Args:
            prev_node_data: The data of the node after which the new node will be inserted.
            data: The data to be added to the new node.

        Raises:
            ValueError: If `prev_node_data` is not found in the list or the list is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot insert after: List is empty.")

        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Node with data '{prev_node_data}' not found in the list.")

    def delete_node(self, key):
        """
        Deletes the first node that contains the given key.

        Args:
            key: The data of the node to be deleted.

        Raises:
            ValueError: If the list is empty or the key is not found.
        """
        if self.is_empty():
            raise ValueError("Cannot delete from an empty list.")

        current = self.head

        # Case 1: Head node itself holds the key
        if current is not None and current.data == key:
            self.head = current.next
            return

        # Case 2: Search for the key, keep track of previous node
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            raise ValueError(f"Node with key '{key}' not found in the list.")

        # Unlink the node from linked list
        prev.next = current.next

    def delete_at_position(self, position):
        """
        Deletes the node at the specified position (0-indexed).

        Args:
            position (int): The 0-indexed position of the node to be deleted.

        Returns:
            Any: The data of the deleted node.

        Raises:
            IndexError: If the position is out of bounds.
            ValueError: If the list is empty or position is invalid.
        """
        if self.is_empty():
            raise ValueError("Cannot delete from an empty list.")
        if not isinstance(position, int) or position < 0:
            raise ValueError("Position must be a non-negative integer.")

        current = self.head

        # Case 1: Deleting the head node (position 0)
        if position == 0:
            deleted_data = current.data
            self.head = current.next
            return deleted_data

        # Case 2: Traverse to the node just before the desired position
        for _ in range(position - 1):
            if current is None or current.next is None:
                raise IndexError("Position out of bounds.")
            current = current.next

        # If current is None here, it means position was out of bounds
        if current is None or current.next is None:
            raise IndexError("Position out of bounds.")

        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def search(self, key):
        """
        Searches for a node with the given key.

        Args:
            key: The data to search for.

        Returns:
            Node or None: The Node object if found, otherwise None.
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def get_node_at_position(self, position):
        """
        Returns the node at the specified position (0-indexed).

        Args:
            position (int): The 0-indexed position of the node.

        Returns:
            Node or None: The Node object at the given position, or None if out of bounds.

        Raises:
            ValueError: If position is not a non-negative integer.
        """
        if not isinstance(position, int) or position < 0:
            raise ValueError("Position must be a non-negative integer.")

        current = self.head
        count = 0
        while current:
            if count == position:
                return current
            count += 1
            current = current.next
        return None # Position out of bounds

    def reverse(self):
        """
        Reverses the linked list in-place.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next # Store next node
            current.next = prev     # Reverse current node's pointer
            prev = current          # Move prev to current node
            current = next_node     # Move current to next node
        self.head = prev # Update head to the new first node

    def has_cycle(self):
        """
        Detects if the linked list contains a cycle using Floyd's Tortoise and Hare algorithm.

        Returns:
            bool: True if a cycle is detected, False otherwise.
        """
        if self.is_empty():
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_middle(self):
        """
        Finds the middle node of the linked list.
        If the list has an even number of nodes, it returns the second of the two middle nodes.

        Returns:
            Node or None: The middle Node object, or None if the list is empty.
        """
        if self.is_empty():
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_duplicates(self):
        """
        Removes duplicate values from the linked list.
        Keeps the first occurrence of each data value.
        """
        if self.is_empty():
            return

        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                # Duplicate found, skip current node
                prev.next = current.next
            else:
                # Not a duplicate, add to seen and move prev
                seen.add(current.data)
                prev = current
            current = current.next

    def get_nth_from_end(self, n):
        """
        Finds the nth node from the end of the linked list (1-indexed).

        Args:
            n (int): The position from the end (1-indexed).

        Returns:
            Node or None: The Node object at the nth position from the end, or None if not found.

        Raises:
            ValueError: If n is not a positive integer.
            IndexError: If n is greater than the length of the list.
        """
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer.")
        if self.is_empty():
            return None

        # Use two pointers: main_ptr and ref_ptr
        main_ptr = self.head
        ref_ptr = self.head

        # Move ref_ptr n nodes ahead
        count = 0
        while count < n:
            if ref_ptr is None:
                raise IndexError(f"n ({n}) is greater than the number of nodes in the list.")
            ref_ptr = ref_ptr.next
            count += 1

        # Move both pointers until ref_ptr reaches the end
        while ref_ptr:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """
        Merges two sorted linked lists into a single sorted linked list.
        The original lists remain unchanged.

        Args:
            list1 (LinkedList): The first sorted linked list.
            list2 (LinkedList): The second sorted linked list.

        Returns:
            LinkedList: A new sorted linked list containing elements from both input lists.

        Raises:
            TypeError: If inputs are not LinkedList objects.
        """
        if not isinstance(list1, LinkedList) or not isinstance(list2, LinkedList):
            raise TypeError("Both inputs must be LinkedList objects.")

        dummy_head = Node(0) # Sentinel node to simplify logic
        tail = dummy_head

        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Append remaining nodes from either list
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        merged_list = LinkedList()
        merged_list.head = dummy_head.next
        return merged_list

def _run_linked_list_demo():
    """
    Demonstrates the usage of the LinkedList class and its various methods.
    This function is intended for testing and demonstration purposes.
    """
    print("--- Linked List Demonstration ---")

    # 1. Initialization and Appending
    ll = LinkedList()
    print(f"Initial list: {ll}")
    print(f"Is empty: {ll.is_empty()}")

    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(f"After appending 10, 20, 30: {ll}")
    print(f"Length: {len(ll)}")
    print(f"Is empty: {ll.is_empty()}")

    # 2. Prepending
    ll.prepend(5)
    print(f"After prepending 5: {ll}")

    # 3. Inserting after
    try:
        ll.insert_after(20, 25)
        print(f"After inserting 25 after 20: {ll}")
        ll.insert_after(50, 55) # This should raise an error
    except ValueError as e:
        print(f"Error inserting after non-existent node: {e}")

    # 4. Deleting a node by key
    try:
        ll.delete_node(10)
        print(f"After deleting node 10: {ll}")
        ll.delete_node(100) # This should raise an error
    except ValueError as e:
        print(f"Error deleting non-existent node: {e}")

    # 5. Deleting at position
    try:
        deleted_data = ll.delete_at_position(0)
        print(f"After deleting at position 0 (data: {deleted_data}): {ll}")
        deleted_data = ll.delete_at_position(2)
        print(f"After deleting at position 2 (data: {deleted_data}): {ll}")
        # ll.delete_at_position(10) # Uncomment to test IndexError
    except (ValueError, IndexError) as e:
        print(f"Error deleting at invalid position: {e}")

    # 6. Searching
    node_25 = ll.search(25)
    print(f"Search for 25: {node_25}")
    node_100 = ll.search(100)
    print(f"Search for 100: {node_100}")

    # 7. Reversing the list
    print(f"Original list before reverse: {ll}")
    ll.reverse()
    print(f"After reversing: {ll}")

    # 8. Finding middle
    ll_middle = LinkedList()
    ll_middle.append(1)
    ll_middle.append(2)
    ll_middle.append(3)
    ll_middle.append(4)
    ll_middle.append(5)
    print(f"\nList for middle (odd): {ll_middle}, Middle: {ll_middle.find_middle()}")
    ll_middle.append(6)
    print(f"List for middle (even): {ll_middle}, Middle: {ll_middle.find_middle()}")

    # 9. Cycle detection
    ll_cycle = LinkedList()
    ll_cycle.append(1)
    ll_cycle.append(2)
    ll_cycle.append(3)
    print(f"\nList for cycle detection: {ll_cycle}")
    print(f"Has cycle (no cycle): {ll_cycle.has_cycle()}")
    # Create a cycle: 3 -> 2
    if ll_cycle.head and ll_cycle.head.next and ll_cycle.head.next.next:
        ll_cycle.head.next.next.next = ll_cycle.head.next
    print(f"Has cycle (with cycle): {ll_cycle.has_cycle()}")
    # Note: Printing a list with a cycle will result in an infinite loop if __str__ is called.
    # Avoid calling __str__ on a list known to have a cycle.

    # 10. Remove duplicates
    ll_dup = LinkedList()
    ll_dup.append(1)
    ll_dup.append(2)
    ll_dup.append(2)
    ll_dup.append(3)
    ll_dup.append(1)
    ll_dup.append(4)
    print(f"\nList with duplicates: {ll_dup}")
    ll_dup.remove_duplicates()
    print(f"After removing duplicates: {ll_dup}")

    # 11. Get Nth from end
    ll_nth = LinkedList()
    for i in range(1, 6):
        ll_nth.append(i * 10) # 10 -> 20 -> 30 -> 40 -> 50
    print(f"\nList for Nth from end: {ll_nth}")
    try:
        print(f"2nd from end: {ll_nth.get_nth_from_end(2)}") # Should be Node(40)
        print(f"5th from end: {ll_nth.get_nth_from_end(5)}") # Should be Node(10)
        # print(f"6th from end: {ll_nth.get_nth_from_end(6)}") # Uncomment to test IndexError
    except (ValueError, IndexError) as e:
        print(f"Error getting Nth from end: {e}")

    # 12. Merge two sorted lists
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    ll2.append(7)

    print(f"\nList 1 for merging: {ll1}")
    print(f"List 2 for merging: {ll2}")
    merged_list = LinkedList.merge_sorted_lists(ll1, ll2)
    print(f"Merged sorted list: {merged_list}")

    ll_empty = LinkedList()
    ll_single = LinkedList()
    ll_single.append(100)
    merged_empty_single = LinkedList.merge_sorted_lists(ll_empty, ll_single)
    print(f"Merged empty and single: {merged_empty_single}")

if __name__ == "__main__":
    _run_linked_list_demo()