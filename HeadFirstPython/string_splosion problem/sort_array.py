def sort_array(idx):
    return sorted(set(idx))


def sort_array_test():
    print("sort_array_test: begin")
    assert sort_array([]) == [], "FT1"

    assert sort_array([1]) == [1], "FT2"
    assert sort_array([1, 1]) == [1], "FT3"
    assert sort_array([1, 2]) == [1, 2], "FT4"
    assert sort_array([1, 2, 2]) == [1, 2], "FT5"
    assert sort_array([1, 2, 3]) == [1, 2, 3], "FT6"
    
    print("sort_array_test: done")


sort_array_test()
