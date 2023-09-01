from itertools import tee, zip_longest, chain

def pairwise_offset(sequence, fillvalue='*', offset=0):
    it1, it2 = tee(sequence, 2)
    return zip_longest(it1, chain(fillvalue * offset, it2), fillvalue=fillvalue)


print(list(pairwise_offset([1, 2, 3, 4], offset=2)))