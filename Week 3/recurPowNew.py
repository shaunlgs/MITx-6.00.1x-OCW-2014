def recurPowerNew(base, exp):
    """
    base: float or int
    exp: int
    exp >= 0
    Return the answer of base raised to exp.
    """
    if exp == 0:
        return 1
    # if the exponent is even
    elif exp % 2 == 0:
        return (base * base) * recurPowerNew(base, exp - 2)
    # if the exponent is odd
    else:
        return base * recurPowerNew(base, exp - 1)