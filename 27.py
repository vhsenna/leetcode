def removeElement(nums: list[int], val: int) -> int:
    p1 = 0

    for p2 in range(len(nums)):
        if nums[p2] != val:  # Ignore if number is equal to val
            nums[p1] = nums[p2]  # Move the value from position p2 to position p1
            p1 += 1
    return p1


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

# Complexity:
# Time: O(n)
# Space: O(1)
