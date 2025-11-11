'''
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    print(i)
'''

for i in range(1, 21):
    if i == 16:
        break
    print(i)

for i in range(0, 30):
    if i % 2 == 0:
        continue
    print(i)

for i in range(5, 0, -1):
    if i == 2:
        pass         # continue to skip 2
    print(i)

for i in range(10, 0, - 1):
    if i == 5:
        continue
    print(i)

numbers = [5, 4, 3, 2, 1, 0, -1]
sum = 0
for num in numbers:
    if num < 0:
        break
    sum += num 
    print(sum)