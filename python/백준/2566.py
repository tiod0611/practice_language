array2D = [] # 2차원 배열 
max_value = 0
r_idx = 0
c_idx = 0

for i in range(9):
    row = list(map(int, input().split(' ')))
    if max(row) > max_value:
        max_value = max(row)
        r_idx = i+1
        c_idx = row.index(max(row)) + 1
    # array2D.append(row)
# print(array2D)
print(r_idx, c_idx)

# for i in range(len(array2D)):
#     print(array2D[i])
#     print(type(array2D[i][0]))
#     prinf max(array2D[i]))
#     if max(array2D[i]) f max:
#       f max f max(array2D[i])
#         r_idx = i
#         c_idx = i.indef max)

# print(r_idx, c_idx)



