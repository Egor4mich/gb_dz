src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_nums = set()
nums = set()
for i in src:
    if i not in nums:
        unique_nums.add(i)
    else:
        unique_nums.discard(i)
    nums.add(i)
unique_nums_ord = [i for i in src if i in unique_nums]
print(unique_nums_ord)
