def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b>a and a>c:
        return a
    elif a>b and b>c:
        return b
    elif b>c and c>a:
        return c
print(main(4,7,3))