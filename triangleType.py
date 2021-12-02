import sys

def getTriangleTypeFromLengths(a, b, c):
    if isinstance(a, int) is not True:
        raise TypeError(f"Value of 'a' equals {a} but must be an integer.")
    if isinstance(b, int) is not True:
        raise TypeError(f"Value of 'b' equals {a} but must be an integer.")
    if isinstance(c, int) is not True:
        raise TypeError(f"Value of 'c' equals {a} but must be an integer.")
    if a <= 0:
        raise ValueError(f"Value of 'a' equals {a} but must be > 0.")
    if b <= 0:
        raise ValueError(f"Value of 'b' equals {b} but must be > 0.")
    if c <= 0:
        raise ValueError(f"Value of 'c' equals {b} but must be > 0.")
    maxValue = max([a,b,c])
    others = [a,b,c]
    others.remove(maxValue)
    if maxValue >= sum(others):
        raise ValueError(f"Highest length must be lower the sum of lower ones.")
    if a == b and b == c:
        return "equilateral"
    elif a != b and b != c and a != c:
        return "scalene"
    else:
        return "isosceles"

if __name__ == "__main__":
    try:
        a = int(input("Please provide value of a: "))
        b = int(input("Please provide value of b: "))
        c = int(input("Please provide value of c: "))
    except ValueError:
        raise TypeError(f"One of provided values is not an integer.")
    print(getTriangleTypeFromLengths(a,b,c))