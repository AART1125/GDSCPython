#This is a program that simulates a hogwarts housing system
#It uses the sum of the unicode value of their first and last name to calculate the house

  
    



























def sort(first, last):
    sum = 0
    for i in first:
        sum += ord(i)
    for i in last:
        sum += ord(i)
    if sum % 4 == 0:
        return "GRYFINDOR!!!"
    elif sum % 4 == 1:
        return "SLYTHERIN!!!"
    if sum % 4 == 2:
        return "HUFFLEPUFF!!!"
    if sum % 4 == 3:
        return "RAVENCLAW!!!"

def main():
    while True:
        first, last = input("What is your name? ").split()
        print(f"Hmmm its seems like your house will be in {sort(first, last)}: ")
        choice = input("Is there still a student to check professor?:(y/n) ")
        if choice == ('y' or 'Y'):
            continue
        elif choice == ('n' or 'N'):
            break
        else:
            print("Wrong Input!!!! Terminating program.....")
            break

main()

#def sort(first, last):
#    sum = 0
#    for i in first:
#        sum += ord(i)
#    for i in last:
#        sum += ord(i)
#    if sum % 4 == 0:
#        return "GRYFINDOR!!!"
#    elif sum % 4 == 1:
#        return "SLYTHERIN!!!"
#    if sum % 4 == 2:
#        return "HUFFLEPUFF!!!"
#    if sum % 4 == 3:
#        return "RAVENCLAW!!!"

#def main():
#    while True:
#        first, last = input("What is your name? ").split()
#        print(f"Hmmm its seems like your house will be in {sort(first, last)}: ")
#        choice = input("Is there still a student to check professor?:(y/n) ")
#        if choice == ('y' or 'Y'):
#            continue
#        elif choice == ('n' or 'N'):
#            break
#        else:
#            print("Wrong Input!!!! Terminating program.....")
#            break

#main()

