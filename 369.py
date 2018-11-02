#while문 이용
i = 0
while i <=100:
    data = list(str(i))
    if "3" in data or "6" in data or "9" in data:
        print("짝!")
    else:
        print(i)
    i += 1

#for문 이용
for a in range(101):
    data = list(str(a))
    if "3" in data or "6" in data or "9" in data:
        print("짝!")
    else:
        print(a)