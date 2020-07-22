import re


def sum_numbers(my_string):
    number = re.findall(r'\d+', my_string)

    return sum(int(num) for num in number)


def sum_numbers_test():
    print("num_string_test: begin")
    assert sum_numbers("abc123xyz") == 123
    assert sum_numbers("aa11b33") == 44
    assert sum_numbers("7 11") == 18
    assert sum_numbers("Chocolate") == 0
    assert sum_numbers("5hoco1a1e") == 7
    assert sum_numbers("5$$1;;1!!") == 7
    assert sum_numbers("a1234bb11") == 1245
    assert sum_numbers("") == 0
    assert sum_numbers("a22bbb3") == 25
    print("num_string_test: done")


sum_numbers_test()
