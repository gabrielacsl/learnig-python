n = int(input())
fat = 1
i = 2
while i <= n:
    fat = fat*i
    i = i + 1

print("{}".format(fat))