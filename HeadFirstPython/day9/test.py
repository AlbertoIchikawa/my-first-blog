import sys

args = sys.argv

print(args)
print("第1引数：" + args[1])
print("第2引数：" + args[2])
print("第3引数：" + args[3])

# リスト[0]にはファイル名が入る。
print(args[0])
print(len(args))