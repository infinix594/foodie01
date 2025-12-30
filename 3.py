k1 = list(map(str, input("Enter keys for dict1: ").split()))
v1 = list(map(int, input("Enter values for dict1: ").split()))
d1 = dict(zip(k1, v1))

k2 = list(map(str, input("Enter keys for dict2: ").split()))
v2 = list(map(int, input("Enter values for dict2: ").split()))
d2 = dict(zip(k2, v2))
for i in d2:
    if i in v1:
        print("Not unique")
        break
else:
    print("Unique dictionary")