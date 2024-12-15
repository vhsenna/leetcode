def lengthOfLastWord(s: str) -> int:
    words = s.split()  # Split the string into words (ignores extra spaces)

    # Return the length of the last word if it exists, otherwise return 0
    if words:
        return len(words[-1])
    else:
        return 0


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))

# Complexity:
# Time: O(n)
# Space: O(k)
