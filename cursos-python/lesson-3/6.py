def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog."""
    return (ketchup + mustard + onion) == 1

print (exactly_one_topping(1,0,0))
print (exactly_one_topping(1,0,1))