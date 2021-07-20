
class UserInputProcessor():

    def readUserInputInteger(self, maxNumber, minNumber):
        choice = int(input("Enter your choice here: "))
        if type(choice) != int:
            print("Choice is an invalid type, please use integers...\n")
        elif choice < minNumber and choice > maxNumber:
            print("Choice", choice, "is out of range, choose again...")
        else:
            return choice
