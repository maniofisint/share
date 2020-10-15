class Memory:
    def __init__(self, max = 999):
        self.memory = [None] * max
        self.__avail = []
        self.__avail.append((0, max-1))

    def allocate(self):
        if len(self.__avail) == 0:
            raise Exception ("memory is full")
        temp = self.__avail.pop()
        if temp[0]+5 <= temp[1]:
            self.__avail.append((temp[0]+3, temp[1]))
        return temp[0]

    def free(self, p):
            self.__avail.append((p, p+2))
            self.__avail.sort()
            self.memory[p] = self.memory[p+1] = self.memory[p+2] = None


m = Memory()
    
class doublyLinkedList:

    def __init__(self):
        self.__header = self.__Node(None, None, None)
        self.__trailer = self.__Node(None, None, None)
        self.__set_next(self.__header, self.__trailer)
        self.__set_prev(self.__trailer, self.__header)
        self.__size = 0
        self.__deleted = False          #TO be used later 
    
    def __Node(self, prev, element, next):
        index = m.allocate()
        m.memory[index] = prev
        m.memory[index + 1] = element
        m.memory[index + 2] = next
        return index

    
    def __prev(self, p):
        return p

    def __element(self, p):
        return p+1

    def __next(self, p):
        return p+2

    def __set_prev(self, p, prev):
        m.memory[self.__prev(p)] = prev

    def __set_element(self, p, element):
        m.memory[self.__element(p)] = element

    def __set_next(self, p, next):
        m.memory[self.__next(p)] = next

    def __get_prev(self, p):
        return m.memory[self.__prev(p)]  

    def __get_element(self, p):
        return m.memory[self.__element(p)]

    def __get_next(self, p):
        return m.memory[self.__next(p)]

    def __len__(self):
        return self.__size

    def __insert_after(self, e, p):
        temp = self.__get_next(p)
        self.__set_next(p, self.__Node(p, e, self.__get_next(p)))
        self.__set_prev(temp, self.__get_next(p))
        self.__size += 1

    def __delete_after(self, p):
        temp = self.__get_next(p)
        if self.__get_next(temp) is not None:
            self.__set_prev(self.__get_next(temp), p)
        self.__set_next(p, self.__get_next(temp))
        m.free(temp)
        self.__size -= 1

    def is_empty(self):
        return self.__size == 0 

    def insert_first(self, e):
        self.__insert_after(e, self.__header)

    def insert_last(self, e):
        self.__insert_after(e, self.__get_prev(self.__trailer))

    def first(self):
        if not self.is_empty():
            return self.__get_element(self.__get_next(self.__header))
        else:
            raise Exception('list is empty')

    def at(self, index):
        """indexing from 0"""
        p = self.__get_next(self.__header)
        for _ in range(index):
            p = self.__get_next(p)
        return self.__get_element(p)

    def delete_first(self):
        if self.is_empty():
            raise Exception('NO more elements')
        self.__delete_after(self.__header)

    def delete_last(self):
        self.__delete_after(self.__get_prev(self.__get_prev(self.__trailer)))

    def delete(self):
        self.erace()
        m.free(self.__header)
        m.free(self.__trailer)

    def delete_at(self, index):
        p = self.__header
        for _ in range(index):
            p = self.__get_next(p)
        self.__delete_after(p)

    def erace(self):
        for _ in range(self.__size):
            self.delete_first()

    def __str__(self):
        lis = []
        p = self.__header
        for _ in range(self.__size):
            p = self.__get_next(p)
            lis.append(self.__get_element(p))
        return str(lis)
        



if __name__ == "__main__":

    l1 = doublyLinkedList()
    l2 = doublyLinkedList()
    l3 = doublyLinkedList()
    
    print()
    print(l1)
    print(l2)
    print(l3)

    for i in range(20):
        l1.insert_last(2*i)
        l2.insert_last(3*i)
        l3.insert_last(l2.at(i) - l1.at(i))
    
    print()
    print(l1)
    print(l2)
    print(l3)

    for i in range(5):
        l1.delete_first()
        l2.delete_last()
        l3.delete_at(i)             # deleting 0, 2, 4, 6, 8

    print()
    print(l1)
    print(l2)
    print(l3)
