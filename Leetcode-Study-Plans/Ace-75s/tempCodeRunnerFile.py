def singleNumber(nums):
    nums.sort()
    xor = 0
    for num in nums:
        xor ^= num
    print("xor => ", xor)
    right_most_bit = xor & -xor
    print( "right_most_bit => " , right_most_bit)
    setA = set()
    setB = set()
    for num in nums:
        if num & right_most_bit:
            setA.add(num)
        else:
            setB.add(num)
    return [list(setA)[0], list(setB)[0]]
print(singleNumber([1,2,1,2,3,5]))
print(singleNumber([-1,0]))
print(singleNumber([0,1]))