# NUMBER OF STEPS TO REDUCE THE BINARY NUMBER TO 1 :
def numSteps(s) -> int:
    def helper(num, steps):
        if num == 1:
            return steps
        if num % 2 != 0:
            num += 1
            return helper(num, steps + 1)
        if num % 2 == 0:
            num //= 2
            return helper(num, steps + 1)
    num = int(s, 2)
    return helper(num, 0)

print(numSteps("1101"))
print(numSteps("10"))
print(numSteps("1"))