def findNumbers(nums: list[int]) -> int:
    count = 0

    # A number has an even number of digits if it falls within the ranges [10, 99], [1000, 9999], or is exactly 100000
    for num in nums:
        if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
            count += 1

    return count

# Complexity:
# Time: O(n)
# Space: O(1)
