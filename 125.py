def isPalindrome(s: str) -> bool:
    s = s.lower()

    # Ask if the string contains any non-alphanumeric characters

    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:  # Iterate through s until p1 and p2 meet at the middle of the sentence
        if not s[p1].isalnum():
            p1 += 1
        elif not s[p2].isalnum():
            p2 -= 1
        elif s[p1] != s[p2]:  # If mismatch, it's not a palindrome
            return False
        else:  # If p1 is equal to p2
            p1 += 1
            p2 -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))

# Complexity:
# Time: O(n)
# Space: O(n)
