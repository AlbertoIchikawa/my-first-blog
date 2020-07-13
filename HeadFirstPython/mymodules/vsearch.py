def search4vowels(phrase: str) -> set:
    """母音が見つかったかどうかによってブール値を返す。"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """phrase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
