def addBinary(a: str, b: str) -> str:
    # Convert binary strings a and b to integers
    a_int = int(a, 2)
    b_int = int(b, 2)

    sum_int = a_int + b_int

    # Convert the result back to a binary string and remove the '0b' prefix
    return str(bin(sum_int)[2:])


print(addBinary("11", "1"))
print(addBinary("1010", "1011"))

# Complexity:
# Time: O(max(n, m))
# Space: O(max(n, m))
