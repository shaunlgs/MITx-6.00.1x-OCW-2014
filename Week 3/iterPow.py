def iterPower(base, exp):
    """
    base: float or int
    exp: int
    exp >= 0
    Return the answer of base raised to exp.
    """
    summation = 1
    while exp > 0:
        summation *= base
        exp -= 1
    return summation