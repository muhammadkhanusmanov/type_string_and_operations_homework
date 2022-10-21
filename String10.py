def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    m = f'({x}+{y})*2={(x+y)*2}'
    return m 
print(main(2,5))