import math
op = input("operation")
x = float(input("Number one"))
y = float(input("Number two(при sqr и sqrtx - не учитывается, введите любую цифру)"))
z = float(input("Stepen'"))


result = None
if op == "+":
    result = x+y
    print(result)
elif op == "-":
    result = x-y
    print(result)
elif op == "*":
    result = x *y
    print(result)
elif op == "/":
    result = x / y
    print(result)
elif op == "sqrtx":
    result = math.sqrt(x)
    print(result)
elif op == "sqr":
    result = x**z
    print(result)
elif op == "cosx":
    result = math.cos(x)
    print(result)
elif op == "sinx":
    result = math.sin(x)
elif op == "log":
    result = math.log(x,y)
    print(result)
input(" ")


#elif op == "-":
  #  result = x - y











