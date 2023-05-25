from a1 import round_to_two_places

print(round_to_two_places(9.9999))

x = -10
y = 5
 # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)


def f(x):
    y = abs(x)
    return y

print(f(5))