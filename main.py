import types
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.main_list_index = 0
        self.nested_list_index = -1
        return self

    def __next__(self):
        self.nested_list_index += 1
        if self.nested_list_index == len(self.list_of_lists[self.main_list_index]):
            self.main_list_index += 1
            self.nested_list_index = 0
        if self.main_list_index == len(self.list_of_lists):
            raise StopIteration
        return self.list_of_lists[self.main_list_index][self.nested_list_index]
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

def flat_generator(list_of_lists):
    for list in list_of_lists:
        for i in range(len(list)):
            yield list[i]


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
