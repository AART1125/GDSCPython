#This python program is a simple calculator that takes in a simple equation and the calculator solves it

def calculate(eq):
    res:float
    res = 0
    if eq[1] == '+':
        res = float(eq[0]) + float(eq[2])
    elif eq[1] == '-':
        res = float(eq[0]) - float(eq[2])
    elif eq[1] == '*':
        res = float(eq[0]) * float(eq[2])
    elif eq[1] == '/':
        res = float(eq[0]) / float(eq[2])
    
    return res

def main():
    while True:
        equation = input("Please input equation: ").split()#<num> <op> <num2> format
        print(f"The answer is {calculate(equation)}")
        choice = input("Do you want to do another equation: ")
        if choice == ('y' or 'Y'):
            continue
        elif choice == ('n' or 'N'):
            break
        else:
            break
        
main()