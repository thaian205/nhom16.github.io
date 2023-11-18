import random
total_count = 0
for _ in range(10):
    b, c = '', ''
    a = random.choice(['H', 'T'])
    count = 0
    while not (a == b == c):
        a = random.choice(['H', 'T'])
        count += 1
        print(a, end=' ')
        if a == b == c:
            break
        b = random.choice(['H', 'T'])
        count += 1
        print(b, end=' ')
        if a == b == c:
            break
        c = random.choice(['H', 'T'])
        print(c, end=' ')
        count += 1
    total_count += count
    print('(', count, ')')
average_count = total_count / 10
print('Số lần tung trung bình:', average_count)