def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
        return 1
    if b>a and b>c and b>f and b>d:
        return 2
    if c>b and c>a and c>d and c>f:
        return 3
    if d>a and d>b and d>f and d>c:
        return 4
    if f>a and f>b and f>c and f>d:
        return 5
print(main(45678))
