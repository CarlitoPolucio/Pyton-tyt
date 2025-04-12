from _collections_abc import Iterable


def __zip(*args: Iterable):
    min_tup = min(len(tuple(iter_obj)) for iter_obj in args)
    return tuple(tuple(tuple(iter_obj)[i] for iter_obj in args) for i in range(min_tup))


if __name__ == '__main__':
    nums = [1, 2, 3]
    sym = ("s", "a", "t")
    sas = [False, True, False]
    boom = {"a": 5, "b": 4, "c": 2}
    print((__zip(nums, sym, sas, boom)))

    for nums, sym, sas, boom in __zip(nums, sym, sas, boom):
        print(nums, sym, sas, boom)







