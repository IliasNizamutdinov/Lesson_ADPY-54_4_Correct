from itertools import chain

nested_list = ['Start',
	['a', 'b', 'c',['12','22',['33','44']]], 'Midle',
	['d', 'e', 'f', 'h', False, ['Что-то','Когда-нибудь'],[1,2,3,4]],
	[1, 2, None],'End'
]

def flat_generator(v_list):
    size = len(v_list)
    count = 1
    while count <= size:
        iter_val = v_list[count - 1]
        if not isinstance(iter_val,list):
            yield iter_val
        else:
            for it_ins in flat_generator(iter_val):
                yield (it_ins)
        count += 1

class FlatIterator(list):

    def __iter__(self):
        list_iter = iter(self.copy())
        self._list_invite = None
        self._list_global = list_iter
        self._len_list = 0
        self._len_list_iter = 0
        return self
    def __next__(self):
        if self._list_invite == None or (self._len_list != 0 and  self._len_list == self._len_list_iter):
            next_list = next(self._list_global)
        else:
            next_list = next(self._list_invite)
            self._len_list_iter += 1
        if isinstance(next_list,list):
            next_list_invite = chain(next_list)
            self._list_invite = next_list_invite
            self._len_list = len(next_list)
            self._len_list_iter = 1
            return next(self._list_invite)
        else:
            return next_list

def main():
    if not len(nested_list) == 0:
        flat_list = [item for item in FlatIterator(nested_list)]
        print(flat_list)
        for it in flat_generator(nested_list):
            print(it)
    else:
        print("Список должен быть заполнен")
if __name__ == '__main__':
    main()