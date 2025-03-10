#Level 2
# 1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.union(B))

# 2. Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.intersection(B))

# 3. Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.issubset(B))

# 4. Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.isdisjoint(B))

# 5. Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
print(A.symmetric_difference(B))

# 7. Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 27, 30}
del A
del B
