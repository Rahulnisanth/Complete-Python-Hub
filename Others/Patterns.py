'''
Cube Number Pattern : N = 4 >>>
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
Triangular Number Pattern : N = 3 >>>
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
X Star Pattern : N = 3 >>>
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

