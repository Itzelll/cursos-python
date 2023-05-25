def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")"""
    return (ketchup and not mustard) or (mustard and not ketchup)

print(exactly_one_sauce(1,0,1))
print(exactly_one_sauce(0,1,1))