def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums.sort()

    previous = 0.5  # Set to 0.5 to ensure it doesn't coincide with any integer values in the array
    longest = 1
    current = 1

    for num in nums:
        if num == previous:
            continue

        if num == previous + 1:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

        previous = num

    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

# Complexity:
# Time: O(n log n)
# Space: O(n)
