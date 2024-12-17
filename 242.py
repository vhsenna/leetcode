def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):  # If lengths don't match, they can't be anagrams
        return False

    counter = {}

    for char in s:  # Count occurrences of each character in s
        counter[char] = counter.get(char, 0) + 1

    for char in t:  # Verify t matches the character counts in s
        if char not in counter or counter[char] == 0:   # Char is missing or has no remaining count
            return False
        counter[char] -= 1  # Decrease the count for each occurrence of the character

        # If s and t are anagrams, the counts for each character will cancel each other out,
        # resulting in a dictionary with all zeros as values

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

# Complexity:
# Time: O(n)
# Space: O()
