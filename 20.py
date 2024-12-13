def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in closeToOpen:  # Every key in the hashmap is always a close parenthesis
            if stack and stack[-1] == closeToOpen[c]:  # Check if the last opened bracket matches
                stack.pop()  # Remove the matching opening bracket from the stack
            else:
                return False  # Parenthesis don't match
        else:
            stack.append(c)

    if not stack:  # If stack is not empty
        return True
    return False


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))

# Complexity:
# Time: O(n)
# Space: O(n)
