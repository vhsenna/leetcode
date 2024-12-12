def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Sort array to simplifies subsequent operations
    solution = []

    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:  # Skip duplicates for the fixed element
            continue

        p1, p2 = index + 1, len(nums) - 1  # Two-pointer approach

        while p1 < p2:  # Iterate by fixing one element (num) and use the two-pointer approach for the remaining elements
            threeSum = num + nums[p1] + nums[p2]
            if threeSum > 0:
                p2 -= 1
            elif threeSum < 0:
                p1 += 1
            else:
                solution.append([num, nums[p1], nums[p2]])  # Found a valid triplet
                p1 += 1
                while nums[p1] == nums[p1 - 1] and p1 < p2:  # Skip duplicate elements for the left pointer
                    p1 += 1

    return solution


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))

# Complexity:
# Time: O(n log n)
# Space: O(n)
