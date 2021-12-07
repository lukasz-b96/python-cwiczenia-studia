def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                print("tozsamosc")
            else:
                print("brak rozwiazan")
        else:
            if c == 0:
                print("y = 0")
            else:
                out = -c/b
                print("y = ", out)
    else:
        if b == 0:
            if c == 0:
                print("x = 0")
            else:
                out = -c/a
                print("x = ",out)
        else:
            if c == 0:
                out = -a/b
                print("y = ", out,"x")
            else:
                out1 = -a/b
                out2 = -c/b
                print("y = ", out1,"x",out2)
            
        
solve1(0,0,0)
solve1(0,0,5)

solve1(0,5,0)
solve1(0,5,3)


solve1(1,0,0)
solve1(1,0,5)

solve1(1,5,0)
solve1(1,5,3)

