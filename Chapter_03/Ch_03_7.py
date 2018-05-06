# Management of name card
import pickle


class NameCardNode:
    def __init__(self, name, corp, tel):
        self.name = name
        self.corp = corp
        self.tel = tel
        self.next = -1


class NameCardList:
    def __init__ (self):
        self.head = NameCardNode("", "", -1)
        self.tail = NameCardNode("", "", -1)
        self.head .next = self.tail
        self.tail.next = self.tail

    def inputCard(self, name, corp, tel):
        newNameCard = NameCardNode(name, corp, tel)
        newNameCard.next = self.head.next
        self.head.next = newNameCard

    # Delete card which has input name
    def deleteCard(self, name):
        p = self.head
        t = p.next
        while name != t.name and t != self.tail:
            p = p.next
            t = t.next
        if t == self.tail:
            return None
        else:
            # Delete current node (t)
            p.next = t.next
            return True

    # Search card which has input name
    def searchCard(self, name):
        t = self.head.next
        while name != t.name and t != self.tail:
            t = t.next
        if t == self.tail:
            return None
        else:
            return t

    def saveCard(self, fileName):
        fd = open(fileName, 'wb')
        t = self.head.next
        while t != self.tail:
            # Use pickle to save "object" itself
            pickle.dump(t.name, fd)
            pickle.dump(t.corp, fd)
            pickle.dump(t.tel, fd)
            t = t.next
        fd.close()

    def deleteNodeAll(self):
        t = self.head
        t.next = self.tail

    def loadCard(self, fileName):
        try:
            fd = open(fileName, 'rb')
        except FileNotFoundError:
            print("Error : \"%s\" file can't be found" % fileName)
            return False

        while True:
            # Use pickle to load "object" itself
            try:
                name = pickle.load(fd)
                corp = pickle.load(fd)
                tel = pickle.load(fd)
                self.inputCard(name, corp, tel)
            except EOFError:
                break
        fd.close()
        return True

    def printCard(self, card):
        print("Name             : ", card.name)
        print("Corporation      : ", card.corp)
        print("Telephone number : ", card.tel)

    def printCardAll(self):
        t = self.head.next
        while t != self.tail:
            self.printCard(t)
            t = t.next

def selectMenu():
    print("")
    print("Namecard Manager")
    print("-------------------------------------")
    print("1. Input  Namecard")
    print("2. Delete Namecard")
    print("3. Search Namecard")
    print("4. Load   Namecard")
    print("5. Save   Namecard")
    print("6. List   Namecard")
    print("7. End    Program")
    while(True):
        print("")
        # Try to handle only integer
        try:
            i = int(input("Select operation -> "), 10)
        except ValueError:
            pass
        else:
            if i > 0 and i < 8:
                break
    return i


# main() function
if __name__ == "__main__":
    fileName = "Namecard.dat"
    # Initialize namecard class
    nameCard = NameCardList()
    while(True):
        menuNum = selectMenu()
        # End program
        if menuNum == 7:
            break

        # Input namecard
        if menuNum == 1:
            print("Input namecard menu : ")
            name = input("     Input name : ")
            corp = input("     Input corporation : ")
            tel = input("     Input telephone number : ")
            if name == "":
                print("Name in mandatory. Please input name.")
                continue
            else:
                nameCard.inputCard(name, corp, tel)

        # Delete namecard
        elif menuNum == 2:
            name = input("Input name to delete ->")
            results = nameCard.deleteCard(name)
            if results is None:
                print("Can't find that name.")

        # Search namecard
        elif menuNum == 3:
            name = input("Input name to search ->")
            results = nameCard.searchCard(name)
            if results is None:
                print("Can't find that name.")
            else:
                nameCard.printCard(results)

        # Load namecard
        elif menuNum == 4:
            if nameCard.loadCard(fileName) == True:
                print("Load namecard done!!")

        # Save namecard
        elif menuNum == 5:
            nameCard.saveCard(fileName)
            print("Save namecard done!!")

        # List namecard
        elif menuNum == 6:
            nameCard.printCardAll()
