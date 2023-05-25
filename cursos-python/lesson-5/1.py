def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7."""
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
        
print(has_lucky_number([7,4,9,2]))
print(has_lucky_number([4,9,2]))

##########

def has_lucky_numbers(nums):
    return any([num % 7 == 0 for num in nums])


print(has_lucky_number([7,4,9,2]))
print(has_lucky_number([4,9,2]))
