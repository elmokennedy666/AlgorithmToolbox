n_array = int(input())
array = [int(inp) for inp in input().split()]
max_index_1 = -1
max_index_2 = -1
for i in range(0, n_array):
    if  max_index_1 == -1 or array[i] > array[max_index_1]:
        max_index_1 = i

for j in range(0, n_array):
    if j != max_index_1 and (array[j] > array[max_index_2] or max_index_2 == -1):
        max_index_2 = j

print(array[max_index_1] * array[max_index_2])