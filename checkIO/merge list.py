import itertools
list2d = [[1,2,3],[4,5,6], [7], [8,9]]


a = [[1,2,3]]
b = [1,[2,2,2],4]
c = [[[2]],[4,[5,6,[6],6,6,6],7]]

merged = list(itertools.chain.from_iterable(b))

print (merged)