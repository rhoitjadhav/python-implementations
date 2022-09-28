class BasicIterator:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < self.end:
            return self.start
        raise StopIteration


for i in BasicIterator(1, 10):
    print(i)

