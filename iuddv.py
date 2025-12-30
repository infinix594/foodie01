
d = {}
n = int(input("Enter number of items: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("\nOriginal Dictionary:")
print(d)

def get_value(item):
    return item[1]  

sorted_items = sorted(d.items(), key=get_value)

sorted_d = dict(sorted_items)

print("\nSorted Dictionary:")
print(sorted_d)
