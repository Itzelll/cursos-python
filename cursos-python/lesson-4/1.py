def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None."""
    if len(L) < 2:
        return None
    else:
        return L[1]

print(select_second(L=[4,5,9,3]))
print(select_second(L=[4]))