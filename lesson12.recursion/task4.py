def definition(x):
    b = x
    return type(x), "mutable" if isinstance(x, (list, dict, set, bytearray)) else "immutable", id(x)


print(definition(1))