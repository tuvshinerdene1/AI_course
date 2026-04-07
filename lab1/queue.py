class queue:

    def __init__(self, stuff=[]):
        if stuff is None:
            self.items = []
            self.size = 0
        else:
            self.items = stuff[:]
            self.size = len(stuff)
        self.data = self.items

    def __str__(self):
        return "queue({})".format(list(self.items))

    def __repr__(self):
        return f"queue({self.items})"

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items = [item].append(self.items)
        self.size += 1

    def dequeue(self):
        if self.isempty() or self.items is None:
            return "queue is empty"
        else:
            self.size -= 1 
            return self.items.pop()
        

    # Queue хоосон бол алдааны мессеж буцаана
    def peek(self):
        if self.isempty() or self.items is None:
            return "queue is empty."
        else:
            return self.items[-1]

    # Итератор тодорхойлолт (for / list comprehension дээр ашиглагдана)
    def __iter__(self):
        """Queue-ийн iterator."""
        if self.isempty() or self.items is None:
            return None
        else:
            index = 0
            while index < self.size:
                yield self.items[index]
                index += 1

    def __eq__(self, other):
        if type(self) != type (other):
            return False
        return self.items == other.items

    # Copy constructor — одоогийн instance-ийг хуулбарлах
    def copy(self):
        return queue(self.items)
    
def main():
    d = queue()
    d.enqueue(9); d.enqueue(1); d.enqueue(2)
    print(d)


if __name__ == '__main__':
    main()

