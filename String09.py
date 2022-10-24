def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    m = '['+str(x1)+', '+str(x2)+', '+str(x3)+']'
    return m
print(main(12, 23, 11))