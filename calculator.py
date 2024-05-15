
# # calculator()
def number():
    while True:
        try:
            namber = float(input("Enter number: "))
            return namber
        except ValueError:
            print("write only number")

def choice():
    ch = ("+", "-", "*", "/" ) 
    while True:
        c = input(" +,  -, *, /")
        try:
            if c not in ch:
                raise Exception
        except Exception:
            print("only", ch)
        else:
            return c
        
def result():
    x = number()
    c = choice()
    y = number()

    if c == "+":
        res = x + y
        return f"{x} + {y} = {res}"
    elif c == "-":
        res = x - y
        return f"{x} - {y} = {res}"
    elif c == "*":
        res = x * y
        return f"{x} * {y} = {res}"
    elif c == "/":
        while True:
            try:
                res = x / y
                return f"{x} / {y} = {res}"
            except ZeroDivisionError:
                print("tivy chi vajanvum 0i")
                y = number()

print(result())
        
        

