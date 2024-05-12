a = float(input("Enter valua 1 : "))
ope = input("Opareter : ")
b = float(input("Enter valua 2 : "))

if ( ope == '+' ):
    print(a + b)
elif ( ope == '-' ):
    print(a - b)
elif ( ope == '*' ):
    print(a * b)
elif ( ope == '/'):
    print(a / b)
elif ( ope == '//'):
    print(a // b)
elif ( ope == '%'):
    print(a % b)
elif ( ope == '**'):
    print(a ** b)
else:
    print("invelid inpur")