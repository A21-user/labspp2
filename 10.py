def unique_list(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] not in lst[:i]]

nums = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", nums)
print("Unique list:", unique_list(nums))
