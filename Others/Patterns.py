'''
4444444
4333334
4322234
4321234
'''
def print_cube_pattern(N):
    for i in range(N):
        for j in range(2 * N - 1):
            if j < i:
                print(N - j, end='')
            elif j < 2 * N - 1 - i:
                print(N - i, end='')
            else:
                print(j - N + 2, end='')
        print()


'''
1 
2 3
4 5 6
4 5 6
4 5
4
'''
def print_triangle_pattern(N):
    buff = 1
    for i in range(1, N + 1):
        for j in range(i):
            print(buff, end=' ')
            buff += 1
        print('')
    buff -= 1
    for i in range(N, 0, -1):
        buffer = buff - i + 1
        for j in range(i):
            print(buffer + j, end=' ')
        buff -= i
        print('')


'''
*   *
 * *
  *
 * *
*   *
'''
def print_X_pattern(N):
    for i in range(N):
        for j in range(2 * N - 1):
            if j == i or j == 2 * N - 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(N-2, -1, -1):
        for j in range(2 * N - 1):
            if j == i or j == 2 * N - 2 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


'''
0 1 2 3 
4 5 6 
7 8 
9
9
8 7
6 5 4
3 2 1 0
'''
def print_sandbox_pattern(N):
    count = 0
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            print(count, end=' ')
            count += 1
        print('')
    count -= 1
    for i in range(N):
        for j in range(i + 1):
            print(count, end=' ')
            count -= 1
        print(' ')


'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
def print_sandbox_pattern(N):
    for i in range(N):
        for j in range(i):
            print(" ", end="")
        for j in range(N - i):
            print("* ", end="")
        print()
    for i in range(N):
        for j in range(N - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("* ", end="")
        print()


'''
1 b c d
e 6 g h
i j 11 l
m n o 16
'''
def print_cubic_num_alpha_pattern(n):
    flag = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                print(flag, end=" ")
            else:
                print(chr(ord('a') + flag - 1), end=" ")
            flag += 1
        print()


'''
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
'''
def print_pattern(N):
    num = 1
    for i in range(1, N + 1):
        for j in range(i):
            if j < i - 1:
                print(f"{num}*", end='')
            else:
                print(f"{num}", end='')
            num += 1
        print('')
    for i in range(N , 0, -1):
        start = num - i 
        curr = start
        for j in range(i):
            if j < i - 1:
                print(f"{curr}*", end='')
            else:
                print(f"{curr}", end='')
            curr += 1
        num -= i
        print("")
