lists = [[1, 2, 3], [], [], [4], [5]]

for nums in lists:
    result = 0            # reset sum for each sublist
    for char in nums:
        result += char
    print(result)
