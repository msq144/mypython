a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
"""if a>b and a>c:
    print("a is big")
elif b>a and b>c:
    print("b is big")
elif c>a and c>b:
    print("c is big")
else:
    print("all are equal")"""
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")
