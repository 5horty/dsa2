class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Singleylinkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, data):
        if not self.head:
            return False
        else:
            current = self.head
            while current:
                if current.data == data:
                    return True
                current = current.next
        return False

    def delete(self,data):
        if not self.head:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.data == data:
                current.next = current.next.next
                return
            current = current.next
    def traversal(self):
        current = self.head
        while current:
            print(f"val {current.data}")
            current = current.next

    def swap_nodes(self,a,b):
        temp = a.data 
        a.data = b.data
        b.data = temp

    def bubble(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                if curr.data > curr.next.data:
                    self.swap_nodes(curr, curr.next)
                    swapped = True
                curr = curr.next

    def reversal(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def delete_nth_node_from_end(self,n):
        dummy = Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy
        for i in range(n+1):
            if first is None:
                return
            first = first.next
        while first:
            first = first.next
            second = second.next
        if second.next:
            second.next = second.next.next
        self.head = dummy.next

    def merge(self,ll1,ll2):
        ll3 = Singleylinkedlist()
        n1 = ll1.head
        n2 = ll2.head
        while n1 is not None and n2 is not None:
            if n1.data > n2.data:
                ll3.insert(n2.data)
                n2 = n2.next
            else:
                ll3.insert(n1.data)
                n1 = n1.next
        while n1 is not None:
            ll3.insert(n1.data)
            n1 = n1.next
        while n2 is not None:
            ll3.insert(n2.data)
            n2 = n2.next
        return ll3

    def split(self, pivot):
        less = Singleylinkedlist()
        greater = Singleylinkedlist()

        current = self.head

        while current:
            if current.data < pivot:
                less.insert(current.data)
            else:
                greater.insert(current.data)
            current = current.next

        return less, greater

        
            
            





def main():
    x = Singleylinkedlist()
    x.insert(5)
    x.insert(10)
    x.insert(7)
    x.insert(8)
    x.insert(9)
    print("search 5:",x.search(5)) #will true
    print("search 4:",x.search(4)) #will false
    x.delete(5)
    print("search 5:",x.search(5)) #will false
    x.traversal()
    y = Singleylinkedlist()
    y.traversal()
    x.bubble()
    print()
    x.traversal()
    x.reversal()
    x.traversal()
    print()
    x.traversal()
    x.delete_nth_node_from_end(1)
    x.traversal()
    list1 = Singleylinkedlist()
    list1.insert(1)
    list1.insert(4)
    list1.insert(10)
    list1.insert(0)
    list1.bubble()
    list2 = Singleylinkedlist()
    list2.insert(2)
    list2.insert(5)
    list2.insert(-3)
    list2.insert(-6)
    list2.bubble()
    print("\nList 1:")
    list1.traversal()
    print("\nList 2:")
    list2.traversal()
    print("\nMerged list:")
    list3 = list1.merge(list1, list2)
    list3.traversal()
    x1, x2 = x.split(9)
    print("2")
    x1.traversal()
    print()
    x2.traversal()











if __name__ == "__main__":
    main()

        








