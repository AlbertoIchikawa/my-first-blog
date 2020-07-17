def max_span(data_list):
    result = []
    numlist = []
    spanlist = []
    # 配列の中の番号種類の取得
    for i, e in enumerate(data_list):
        if e not in numlist:
            numlist.append(e)

    # 次にそれぞれの番号のインデックス値を取得してresultに入れる。
    # それぞれの数字のインデックス値を使ってspanの計算（最後のインデックス値から最初のインデックス値を引いて＋１するとspanがわかる。）
    for num in numlist:
        result = [i for i, e in enumerate(data_list) if e == num]
        spanlist.append(result[-1] - result[0] + 1)

    # spanlistに値がないとき、０を入れる。
    if not spanlist:
        spanlist.append(0)

    return max(spanlist)


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
