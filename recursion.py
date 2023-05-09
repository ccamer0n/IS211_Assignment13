def fibonnaci(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fibonnaci(n-1) + fibonnaci(n-2)
    return x


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))

def compareTo(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1

if __name__ == "__main__":
    print(fibonnaci(8))
    print(gcd(42, 120))