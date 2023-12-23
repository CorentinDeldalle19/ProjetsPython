from getpass import getpass

def afficher_pendu(erreurs):
    pendu_ascii = [
        "   ------\n   |    |\n       |\n       |\n       |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n       |\n       |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n   |    |\n       |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n  /|    |\n       |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n  /|\\   |\n       |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n  /|\\   |\n  /     |\n       |\n      ---\n",
        "   ------\n   |    |\n   O    |\n  /|\\   |\n  / \\   |\n       |\n      ---\n"
    ]

    print(pendu_ascii[erreurs])

def main():
    mot = getpass("Entrez le mot")

    liste = []
    yourList = []

    for i in mot:
        liste.append(i)
        yourList.append("*")
        
    print("".join(yourList))

    nbErrors = 0

    while nbErrors < 9:
        letter = input("Entrez une lettre")
        
        if len(letter) > 1:
            if letter == mot:
                print("Bravo ! vous avez trouvé !")
                break
        
        if letter in liste:
            for (index, y) in enumerate(liste):
                if y == letter:
                    yourList[index] = y
            v = "".join(yourList)
            print("Bonne lettre !", v)

            if liste == yourList:
                print("Vous avez trouvé !")
                break
        else:
            nbErrors += 1
            print("Mauvaise lettre, il vous reste %s essai(s)"%(9-nbErrors))
            afficher_pendu(nbErrors)
            
    if nbErrors == 9:
        print("Vous avez perdu !")