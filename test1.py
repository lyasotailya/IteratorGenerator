class FlatIterator:
    def __init__(self, li):
        self.li = li
        self.counter = 0
        self.len = len(self.li)

    def __iter__(self):
        self.el = self.li[self.counter]
        self.el_counter = 0
        self.el_len = len(self.el)
        return self

    def __next__(self):
        if self.counter == self.len:
            raise StopIteration

        if self.el_counter == self.el_len:
            self.counter += 1
            self.el_counter = 0

            if self.counter == self.len:  # Чтобы не выходить за границы переданного списка li, уходим на новый круг
                next(self)

            self.el = self.li[self.counter]
            self.el_len = len(self.el)

        el = self.el[self.el_counter]
        self.el_counter += 1
        return el


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
