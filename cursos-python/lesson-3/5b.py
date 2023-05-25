def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings."""
    return not ketchup and not mustard and not onion

print(wants_plain_hotdog(1,1,1))
print(wants_plain_hotdog(1,0,1))
print(wants_plain_hotdog(0,0,0))