class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next
    

if __name__ == '__main__':

    ll_head = LinkedList()
    ll_head.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    ll_head.head.next = second
    second.next = third
    third.next = fourth
    
    ll_head.print_list()

