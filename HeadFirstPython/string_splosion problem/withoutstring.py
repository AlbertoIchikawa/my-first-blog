def withoutString(base, remove):
    idx = base.lower().find(remove.lower())
    if idx >= 0:
        return (base[:idx] if base[:idx] != ' ' else '') + withoutString(base[idx + len(remove):len(base)], remove)
    else:
        return base


def withoutString_test():
    print("withoutString_test: begin")
    assert withoutString("Hello there", "llo") == "He there", "FT1"
    assert withoutString("Hello there", "e") == "Hllo thr"
    assert withoutString("Hello there", "x") == "Hello there"
    assert withoutString("This is a FISH", "IS") == "Th a FH"
    assert withoutString("THIS is a FISH", "is") == "TH a FH"
    assert withoutString("THIS is a FISH", "iS") == "TH a FH"
    assert withoutString("abxxxxab", "xx") == "abab"
    assert withoutString("abxxxab", "xx") == "abxab"
    assert withoutString("abxxxab", "x") == "abab"
    assert withoutString("xxx", "x") == ""
    assert withoutString("xxx", "xx") == "x"
    assert withoutString("xyzzy", "Y") == "xzz"
    assert withoutString("", "x") == ""
    assert withoutString("abcabc", "b") == "acac"
    assert withoutString("AA22bb", "2") == "AAbb"
    assert withoutString("1111", "1") == ""
    assert withoutString("1111", "11") == ""
    assert withoutString("MkjtMkx", "Mk") == "jtx"
    assert withoutString("Hi HoHo", "Ho") == "Hi "
    print("withoutString_test: done")


withoutString_test()
