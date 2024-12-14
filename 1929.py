def getConcatenation(nums: list[int]) -> list[int]:
    nums *= 2
    return nums


print(getConcatenation([1, 2, 1]))
print(getConcatenation([1, 3, 2, 1]))

# Complexity:
# Time: O(n)
# Space: O(n)
