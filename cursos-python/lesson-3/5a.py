def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions."""
    return ketchup and mustard and not onion


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)"""
    return ketchup and mustard and onion


print(onionless(1, 1, 0))
print(onionless(1, 1, 1))
print(wants_all_toppings(1, 1, 1))