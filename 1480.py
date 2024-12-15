def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):  # Iterate from the second element
        nums[i] = nums[i - 1] + nums[i]

    return nums


print(runningSum([1, 2, 3, 4]))
print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([3, 1, 2, 10, 1]))

# Complexity:
# Time: O(n)
# Space: O(1)
