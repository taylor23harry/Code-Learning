import random

def binarysearch(data, target):
    """A binary search algorithm that returns True if target is in data, else False."""
    low = 0
    high = len(data) - 1
    while high >= low:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid -1
    return False

def bubblesort(data):
    p = 0
    while True:
        changed = False
        for i in range(0, len(data) -1):
            if data[i] > data[i+1]:
                storage = i+1
                data[i+1], data[i] = data[i], data[storage]
                changed = True
            else:
                pass
        if changed == False:
            print(f"Finished, after {p} passes.")
            break
        else:
            p += 1

num = []

for i in range(200000):
    if i % 3 == 0:
        if len(num) > 2:
            num.insert(random.randint(0, len(num)-1), i)
        else:
            num.append(i)
print("Generating numbers complete\n")
print(num)
bubblesort(num)
print("-------------------------------------------------------------------\n")
print(num)