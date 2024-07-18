# MINIMUM JUMPS TO REACH THE END OF THE ARRAY :
def find_min_steps(steps):
    jumps = current_max = max_far = 0
    for i in range(len(steps) - 1):
        max_far = max(max_far, i + steps[i])
        if i == current_max:
            jumps += 1
            current_max = max_far
    return jumps

# Input :
steps = list(map(int, input().split()))
print(find_min_steps(steps))