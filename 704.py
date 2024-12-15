def search(nums: list[int], target: int) -> int:
    p1, p2 = 0, len(nums) - 1  # Initialize two pointers at the start and end of the list

    while p1 <= p2:
        middle = (p1 + p2) // 2  # Pointer at the middle index of the array

        if target < nums[middle]:  # If the target is smaller, search the left half
            p2 = middle - 1
        elif target > nums[middle]:  # If the target is larger, search the right half
            p1 = middle + 1
        else:  # Target found
            return middle
    return -1  # Target not found


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))

# Complexity:
# Time: O(log n)
# Space: O(1)
