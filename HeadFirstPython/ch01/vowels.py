vowels = ['a', 'e', 'i', 'o', 'u']
word = input("単語を入力してください。母音を探します。")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)

phrase = "Don't panic!"
plist = list (phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)