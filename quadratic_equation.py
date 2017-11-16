from math import sqrt

def get_first_root(a, b, discriminant):
    first_root = (-b - sqrt(discriminant)) / (2 * a)
    return first_root

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        root1 = get_first_root(a, b, discriminant)
        return root1, None
    elif discriminant > 0:
        root1 = get_first_root(a, b, discriminant)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant < 0:
        return None, None
