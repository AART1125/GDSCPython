#This is a simple cashiering problem that will calculate the total of the customer's order based from the menu
#A dictionary is used to assign a value with a given key for the menu

#reading the file for the values in the dict
def initmenu() -> dict:
    menu = {}
    file = open("itemsandprice.csv", "r")
    for line in file:
        item, price = line.split(", ")
        menu[str(item)] = float(price)
    file.close()
    return menu

    #with open("itemsandprice.csv") as file:
    #    menu = dict(line.split(", ") for line in file)
    #return menu


def gettotal(menu, choices):
    sum = 0
    for i in choices:
        sum += getprice(menu, i.capitalize())
    return sum 

def getprice(menu, item):
    return menu.get(item)

def main():
    menu = initmenu()
    print("Menu:")
    for i in menu:
        print(f"{i} : {getprice(menu, i)}")
    choices = input("\nWhat will be your order?: ").split()
    print(f"\nYour Total will be {gettotal(menu, choices)}")
    
main()