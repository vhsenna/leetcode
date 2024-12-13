def isPalindrome(x: int) -> bool:
    reverse = 0
    xCopy = x  # Copy of x for later comparison

    while x > 0:
        d = x % 10  # Extract the last digit of x
        reverse = reverse * 10 + d  # Add last digit d to reverse
        x = x // 10  # Remove the last digit from x

    if xCopy == reverse:
        return True
    else:
        return False


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))

# Complexity:
# Time: O(n)
# Space: O(1)
