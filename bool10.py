import math

def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Calculate the square root of "a"
    sqrt_a = math.isqrt(a)

    # Check if the square of the square root is equal to "a"
    return sqrt_a * sqrt_a == a
print(main(2))