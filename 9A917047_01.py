stars = int(input("請輸入星星數量（請輸入單數）："))

# 上半部分
for i in range(1, stars + 1, 2):
    spaces = (stars - i) // 2
    print(" " * spaces + "*" * i)

# 下半部分
for i in range(stars - 2, 0, -2):
    spaces = (stars - i) // 2
    print(" " * spaces + "*" * i)