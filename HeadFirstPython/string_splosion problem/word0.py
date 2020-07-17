def word0(idx):
    d = {}
    for k in idx:
        if k not in d.keys():
            d[k] = 0
    print(d)
    print(d.items())
    return dict(sorted(d.items()))


def word0_test():
    print("word0_test: begin")
    assert word0(["a", "b", "a", "b"]) == {'a': 0, 'b': 0}, "FT1"
    assert word0(["a", "b", "a", "c", "b"]) == {"a": 0, "b": 0, "c": 0}, "FT2"
    assert word0(["c", "b", "a"]) == {"a": 0, "b": 0, "c": 0}, "FT3"
    assert word0(["c", "c", "c", "c"]) == {"c": 0}, "FT4"
    assert word0([]) == {}, "FT5"
    print("word0_test: done")


word0_test()