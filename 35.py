def searchInsert(nums: list[int], target: int) -> int:
    for index, num in enumerate(nums):
        if num >= target:
            return index

    return len(nums)  # If no element is greater than or equal to the target, return the length of the list


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))

# Complexity:
# Time: O(n)
# Space: O(1)
