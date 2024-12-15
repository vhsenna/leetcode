def reverseString(s: list[str]) -> None:
    p1, p2 = 0, len(s) - 1  # Initialize two pointers at the start and end of the list

    while p1 < p2:  # Continue swapping until the pointers meet or cross
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1


print(reverseString(["h", "e", "l", "l", "o"]))
print(reverseString(["H", "a", "n", "n", "a", "h"]))

# Complexity:
# Time: O(n)
# Space: O(1)
