#This python program creates a simple database that takes in the nickname of a user and their hobbies
names = []
hobbies = []

def readfile():
    try:
        with open("NamesandHobbies.txt", "r") as file:
            for line in file:
                name, hobby = line.split(" ")
                names.append(name)
                hobbies.append(hobby)
    except FileNotFoundError:
        print("ERROR FILE NOT FOUND!!!!")
    
def appendtofile(name, hobby):
    with open("NamesandHobbies.txt", "a") as file:
        string = name + " " + hobby
        file.write(f"{string}\n")
        file.close()
        
def main():
    readfile()
    
    i = 0
    print("Items in Database: ")
    while i < len(names):
        print(names[i], hobbies[i], sep=" ")
        i+=1
    
    while True:
        name = input("Input your nickname: ")
        hobby = input("Input your hobby: ")
    
        appendtofile(name, hobby)
        
        choice = input("Do you want to add another to the database?(y/n): ")
        
        if choice == ('y' or 'Y'):
            continue
        elif choice == ('n' or 'N'):
            break
        else:
            print("Wrong input!!! Terminating program")
            break
        
main()