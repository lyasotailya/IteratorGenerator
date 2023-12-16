class F:
    def __init__(self, li):
        self.stack = li

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            cur = self.stack.pop()
            if isinstance(cur, list):
                self.stack.extend(cur[::-1])
            else:
                return cur
        raise StopIteration


list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

for i in F(list_of_lists_2):
    print(i)
