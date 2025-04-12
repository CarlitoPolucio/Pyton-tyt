from _collections_abc import Iterable


def __zip(*args: Iterable): #-> tuple:
    return tuple((tuple(iter_obj[i]) for iter_obj in enumerate(args)) for i in range(len(args)))


if __name__ == '__main__':
    nums = [1, 2, 3]
    sym = ("s", "a", "t")
    sas = [False, True, False]
    boom = {"a": 5, "b": 4, "c": 2}
    print(tuple(zip(nums,sym,sas,boom)))







