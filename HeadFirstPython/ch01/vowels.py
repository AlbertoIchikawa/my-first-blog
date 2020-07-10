vowels = ["a","e","i","o","u"]
word = input("単語を入力してください。母音を探します")
found = {}
for letters in word:
    if letters in vowels:
        found.setdefault(letters, 0)
        found[letters] += 1
for k, v in sorted(found.items()):
    print(k, 'の出現回数は', v, '回です。')