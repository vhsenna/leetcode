def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


print(containsDuplicate([1, 2, 1, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# Complexity:
# Time: O(n)
# Space: O(n)

# Optimized approach with O(1) space complexity if prioritizing space efficiency
# def containsDuplicate(nums: list[int]) -> bool:
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             return True  # Duplicate found
#     return False  # No duplicates found

# Complexity:
# Time: O(n log n)
# Space: O(1)
