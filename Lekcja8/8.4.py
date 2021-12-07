import math

def heron(a, b, c):
    p = (a+b+c)/2
    if p - a < 0 or p - b < 0 or p - c < 0:
        raise ValueError("nie da sie")
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)

print("Poprawny trójkąt")
print(heron(3, 4, 5))
print("Niepoprawny trójkąt:")
print(heron(3, 5, 9))