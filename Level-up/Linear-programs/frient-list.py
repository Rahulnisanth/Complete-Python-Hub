# Storage fields :
my_friend = []
friends_friend = []

# Input stream :
n = int(input())
for _ in range(n):
    string = input().split()
    for i in range(len(string)):
        if i == 0: my_friend.append(string[i])
        if string[i].isdigit(): continue
        if i > 0: friends_friend.append(string[i])

# core drive :
for people in friends_friend:
    if people not in my_friend:
        print(people, end=' ')
