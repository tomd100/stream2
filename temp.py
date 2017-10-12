str = "abcdefghijkl"

# print(str[len(str)-2:])
# print(str[:len(str)-2])

# print(str[:2])
# print(str[0:2])
# print(str[1:3])

# for i in range(0,20,2):
#     print(i)

# dict1 = {}

# dict1[1]="hello"
# dict1[2]="you"


# dict2 = {}

# dict2[1]="you"
# dict2[2]="hello"

# print(sorted(dict1) == sorted(dict2))

grid = {(0, 1): 'B', (1, 0): 'C', (0, 0): 'A', (1, 1): 'D'}

path=[(0, 1)]

neighbours = {
(0, 1): [(0, 0), (1, 0), (1, 1)], 
(1, 0): [(0, 0), (0, 1), (1, 1)], 
(0, 0): [(0, 1), (1, 0), (1, 1)], 
(1, 1): [(0, 0), (0, 1), (1, 0)]
}

print("path: ", path)
print("path[-1]: ", path[-1])
print ("neighbours[path[-1]]: ", neighbours[path[-1]])
for next_pos in neighbours[path[-1]]:
    print("next_pos: ", next_pos)
    print("[next_pos]: ", [next_pos])
    print("path + [next_pos]: ", path + [next_pos])

print(''.join([grid[p] for p in path]))

# if next_pos not in path:
#     do_search(path + [next_pos])