def max_span(data_list):
    index_dict = {}
    for i, number in enumerate(data_list):
        if number not in index_dict:
            index_dict[number] = []
        index_dict[number].append(i)
    m = 1
    for elem in index_dict:
        current_span = index_dict[elem][-1] - index_dict[elem][0] + 1
        if current_span > m:
            m = current_span
    if len(index_dict) == 0:
        m = 0
    return m


def max_span_test():
    print("max_span_test: begin")
    assert max_span([1, 2, 1, 1, 3]) == 4, 'TF1 Fail'
    assert max_span([1, 4, 2, 1, 4, 1, 4]) == 6, 'TF2 Fail'
    assert max_span([1, 4, 2, 1, 4, 4, 4]) == 6, 'TF3 Fail'
    assert max_span([3, 3, 3]) == 3, 'TF4 Fail'
    assert max_span([3, 9, 3]) == 3, 'TF5 Fail'
    assert max_span([3, 9, 9]) == 2, 'TF6 Fail'
    assert max_span([3, 9]) == 1, 'TF7 Fail'
    assert max_span([3, 3]) == 2, 'TF8 Fail'
    assert max_span([]) == 0, 'TF9 Fail'
    assert max_span([1]) == 1, 'TF10 Fail'
    print("max_span_test: done")


max_span_test()
