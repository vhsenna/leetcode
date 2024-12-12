def twoSum(numbers: list[int], target: int) -> list[int]:
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        sum = numbers[p1] + numbers[p2]

        if sum > target:  # The array will be traversed from start to end and end to start
            p2 -= 1       # simultaneously and the result will be found by traversing only once
        elif sum < target:
            p1 += 1
        else:
            return [p1 + 1, p2 + 1]

    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))

# Complexity:
# Time: O(n)
# Space: O(1)
