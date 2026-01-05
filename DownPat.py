def is_Pat(string):
    # Base case: single letter is a pat
    if len(string) == 1:
        return True

    n = len(string)
    for i in range(1, n):
        left = string[:i]
        right = string[i:]
        rev_left = left[::-1]
        rev_right = right[::-1]
        if is_Pat(rev_left) and is_Pat(rev_right):
            if all(l > max(right) for l in left):
                return True

    return False

s1, s2 = input().split()
print("YES" if is_Pat(s1) else "NO")
print("YES" if is_Pat(s2) else "NO")
print("YES" if is_Pat(s1 + s2) else "NO")
