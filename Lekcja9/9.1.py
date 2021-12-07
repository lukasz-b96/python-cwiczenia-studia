class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        temp = self.head
        out = "[ "
        while (temp != None):
            out += str(temp.data) + " "
            temp = temp.next
        out +="]"
        return out
    
    
    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    
    def remove_tail(self): 
        # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
            
        prev = None
        temp = self.head
        while (temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = None
        self.length -= 1
        self.tail = prev
            
        

    def join(self, other):    # klasy O(1)
        if self.is_empty():
            self.head= other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        other.head = None
        other.lenght = 0
        other.tail = None

    def clear(self):      # czyszczenie listy
        self.head = None
        self.lenght = 0
        self.tail = None

print("a)")
alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
alist.insert_tail(Node(44))         # [22, 11, 33 44]

print(str(alist))
alist.remove_tail()
print(str(alist))

#############

print("b)")
blist = SingleList()
blist.insert_head(Node(1))         # [1]
blist.insert_tail(Node(2))         # [1, 2]
blist.insert_tail(Node(3))         # [1, 2, 3]
print(str(blist))

print("c)")
alist.join(blist)
print(str(blist))
print(str(alist))


print("d)")
clist = SingleList()
clist.join(alist)
print(str(clist))
print(str(alist))


#############
print("e)")
print(clist)
clist.clear()
print(clist)