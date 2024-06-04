def shifter(num):
    left4sshift = num & 0b11110000
    print(left4sshift)
    print(bin(left4sshift)[2:])
    right4shift = num & 0b00001111
    print(right4shift)
    print(bin(right4shift)[2:])
    left4sshift = left4sshift >> 4
    print(left4sshift)
    print(bin(left4sshift)[2:])
    right4shift = right4shift << 4
    print(right4shift)
    print(bin(right4shift)[2:])
    return left4sshift + right4shift

print(shifter(52))