def sort_array(idx):
    found = []
    found = sorted(set(idx))

    return sorted(found)


def sort_array_test():
    print("sort_array_test: begin")
    assert sort_array([]) == [], "FT1"
    assert sort_array([1]) == [1]
    assert sort_array([1, 1]) == [1]
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([1, 2, 2]) == [1, 2]
    assert sort_array([1, 2, 3]) == [1, 2, 3]
    print("sort_array_test: done")


sort_array_test()
