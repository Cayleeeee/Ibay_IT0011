A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. How many elements are there in set A and B
print("Number of elements in A and B:", len(A | B))

# b. How many elements are in B that are not part of A and C
print("Number of elements in B not in A and C:", len(B - (A | C)))

# c. Show the following using set operations:

# i. {h, i, j, k}
print("Set {h, i, j, k}:", C - (A | B))

# ii. {c, d, f}
print("Set {c, d, f}:", A & C)

# iii. {b, c, h}
print("Set {b, c, h}:", (A & B) | {'h'})

# iv. {d, f}
print("Set {d, f}:", A & C - B)

# v. {c}
print("Set {c}:", A & B & C)

# vi. {l, m, o}
print("Set {l, m, o}:", B - (A | C))
