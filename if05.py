def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    b=n//1000%10
    c=n//100%10
    d=n//10%10
    f=n%10
    if a>b and a>c and a>d and a>f:
        return a
    if b>a and b>c and b>f:
        return b
    if c>b and c>a and c>d and c>f:
        return c
    if d>a and d>b and d>f and d>c:
        return d
    if f>a and f>b and f>c and f>d:
        return f
print(main(56789))
