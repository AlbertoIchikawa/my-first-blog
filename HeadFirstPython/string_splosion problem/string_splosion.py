def string_splosion(str):
    s = ''
    for x in range(len(str)):
        for y in range(x):
            s = s + str[y]
        s = s + str[x]
    return s


def string_splosion_test():
    print("string_splosion_test: begin")
    assert string_splosion("Code") == "CCoCodCode", "TC1 Fail"
    assert string_splosion("abc") == "aababc", "TC2 Fail"
    assert string_splosion("ab") == "aab", "TC3 Fail"
    assert string_splosion("x") == "x", "TC4 Fail"
    assert string_splosion("fade") == "ffafadfade", "TC5 Fail"
    assert string_splosion("There") == "TThTheTherThere", "TC6 Fail"
    assert string_splosion("Kitten") == "KKiKitKittKitteKitten", "TC7 Fail"
    assert string_splosion("Bye") == "BByBye", "TC8 Fail"
    assert string_splosion("Good") == "GGoGooGood", "TC9 Fail"
    assert string_splosion("Bad") == "BBaBad", "TC10 Fail"
    print("string_splosion_test: done")


string_splosion_test()
