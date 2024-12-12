def twoSum(nums: list[int], target: int) -> list[int] | None:
    hasher = {}  # Create a hashmap to store numbers and their corresponding indices

    for index in range(len(nums)):
        complement = target - nums[index]  # Calculate the complement needed to reach the target
        if complement in hasher:  # If the complement is already in the hashmap, return the indices
            return [hasher[complement], index]
        hasher[nums[index]] = index  # Store the current number and its index in the hashmap
    return  # Return None if no solution is found


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))

# Complexity:
# Time: O(n)
# Space: O(n)
