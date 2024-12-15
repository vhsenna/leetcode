def validMountainArray(arr: list[int]) -> bool:
    p1 = 0
    p2 = -1

    # Ascending part of the mountain
    while p1 < (len(arr) - 1) and arr[p1] < arr[p1 + 1]:
        p1 += 1
    # Descending part of the mountain
    while p2 > -len(arr) and arr[p2] < arr[p2 - 1]:
        p2 -= 1

    # Check if p1 and p2 meet at the peak, and there is both an ascending and descending part
    # p1 == p2 + len(arr):   p1 and p2 meet at the peak
    # p1 > 0:                Ascending section
    # p2 < -1:               Descending section
    return p1 == p2 + len(arr) and p1 > 0 and p2 < -1


print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
print(validMountainArray([1, 3, 2]))

# Complexity:
# Time: O(n)
# Space: O(1)
