def reverse(x: int) -> int:
    reverse = int(str(abs(x))[::-1])  # Reverse the digits of the absolute value of the number

    if x < 0:  # If the original number is negative, restore the negative sign
        return - reverse
    return reverse  # Return the reversed number for positive input


print(reverse(123))
print(reverse(-123))
print(reverse(120))

# Complexity:
# Time: O(n)
# Space: O(n)
