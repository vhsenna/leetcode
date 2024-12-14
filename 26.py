def removeDuplicates(nums: list[int]) -> int:
    k = 1  # At least one unique number exists (the first element)

    # Iterate through the list starting from index 1
    for p in range(1, len(nums)):  # p starts at index 1
        if nums[p] != nums[p - 1]:  # Look at p and compare it with the previous value
            k += 1
    return k


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# Complexity:
# Time: O(n)
# Space: O(1)
