def tri_recursion(l, index=0, depth=0):
    global max_depth
    if index >= len(l):
        return max_depth
    if l[index] == "[":
        depth += 1
        if depth > max_depth:
            max_depth = depth
    elif l[index] == "]":
        depth -= 1
    return tri_recursion(l, index + 1, depth)

max_depth = 0
l = input("Enter nested brackets : ")
print("Nesting Level:", tri_recursion(l))