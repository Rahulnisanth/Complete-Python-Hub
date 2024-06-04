def find_minimum_operations(n) -> int:
    count = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
            count += 1
        else:
            n -= 1
            count += 1
    return count

t = int(input())
for _ in range(t):
    print(find_minimum_operations(int(input())))