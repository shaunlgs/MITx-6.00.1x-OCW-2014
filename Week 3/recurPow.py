def recurPower(base, exp):
    """
    base: float or int
    exp: int
    exp >= 0
    Return the answer of base raised to exp.
    """
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)