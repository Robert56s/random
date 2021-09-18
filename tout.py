from random import seed
from random import randint

from turtle import *


def borne_default():
    seed()

    nombre_essay = 0

    value = randint(0, 100)

    #print(value)

    guess = int(input("Entrez votre nombre:"))

    for i in range (0,1000):

        while guess > value :
            guess = int(input("Votre nombre est plus grand que le nombre secret. Esayer encore \nreponse:"))
            nombre_essay = nombre_essay + 1

        while guess < value :
            guess = int(input("Votre nombre est plus petit que le nombre secret. Esayer encore \nreponse:"))
            nombre_essay = nombre_essay + 1

        if guess == value:

            nombre_essay = nombre_essay + 1
            print("Bravo, vous avez trouver le nombre secret!\nNombre d'essay:",nombre_essay)

            recommencer = (input("Voulez vous recomencere? (oui/non)\nreponse:" ))

            if recommencer == "oui" :
                script()
            elif recommencer == "non" :
                print("Merci et au revoir…")
            else:
                print("error")

            break


def borne_custom():
    seed()

    nombre_essay = 0

    borne_minimale = int(input("choisisser borne_minimale:" ))
    borne_maximale = int(input("choisisser borne_maximale:"))


    value = randint( borne_minimale , borne_maximale)

    #print(value)

    guess = int(input("Entrer votre nombre:"))

    for i in range (0,1000):

        while guess > value :
            guess = int(input("Votre nombre est plus grand que le nombre secret. Esayer encore \nreponse:"))
            nombre_essay = nombre_essay + 1

        while guess < value :
            guess = int(input("Votre nombre est plus petit que le nombre secret. Esayer encore \nreponse:"))
            nombre_essay = nombre_essay + 1

        if guess == value:

            nombre_essay = nombre_essay + 1
            print("Bravo, vous avez trouver le nombre secret!\nNombre d'essay:",nombre_essay)

            recommencer = (input("Voulez vous recomencer? (oui/non)\nreponse:"))

            if recommencer == "oui":
                script()
            elif recommencer == "non":
                print("Merci et au revoir")
            else:
                print("error")

            break


def script():

    print("Boujour aux jeux des devinettes! Votre but est de trouver un nombre généré aléatoirement avec le moins d'essai")
    question_borne = (input("Voulez vous prendre le default de 0 a 100 ou choisir les borne minimal et maximal custom (d/c) \nreponse:"))

    if question_borne == "c" :
        borne_custom()

    elif question_borne == "d" :
        borne_default()

    else:
        print("error")



def sapin():




    shape("turtle")

    color("brown")
    begin_fill()

    for i in range(0, 4):  # carré brun
        forward(50)
        right(90)
    end_fill()

    # aller plus loin pour faire les epine du sapin
    up()
    backward(70)
    down()

    # variable pour que les epines du sapin raptice a chaque foi qu'ils monte pour imiter un vrai sapin
    taille = 200

    # commencer les epine

    for i in range(0, 4):
        color("green")

        begin_fill()

        for i in range(0, 3):
            # C'est la ou la variable va
            forward(taille)
            left(120)

        end_fill()

        forward(15)
        taille = taille - 30

        up()
        left(90)
        forward(60)
        right(90)
        down()

    # cacher la tortue
    ht()



def cartier_nuageux():
    # créé par Robert Nelea en 2020
    # quartier nuageux

    print("Bienvenue sur http.generateurdequartier.com")


    shape("turtle")

    def maison():  # fonction
        begin_fill()
        color("brown")
        for i in range(0, 3):  # toit de maison
            left(120)
            forward(60)
        end_fill()

        begin_fill()
        color("green")
        for x in range(0, 4):  # corp de la maison
            right(90)
            forward(60)
        end_fill()

        up()
        right(90)
        forward(60)
        right(90)
        forward(20)
        down()

        begin_fill()  # porte de maison
        color("black")
        forward(20)
        right(90)
        forward(30)
        right(90)
        forward(20)
        right(90)
        forward(30)
        end_fill()
        left(90)

    def nuage():  # fonction
        begin_fill()
        color("grey")
        for i in range(0, 2):  # formation du nuage
            forward(120)
            right(90)
            forward(50)
            right(90)
        end_fill()

    nombre_maison = int(input(
        "Combien de maisons voulez vous dans votre quartier?"))  # variable de la question pour savoir le nobre de maison qu'ils veulent

    nombre_nuage = int(input(
        "Combien de nuages voulez vous dans votre quartier?"))  # variable de la question pour savoir le nobre de nuage qu'ils veulent

    for a in range(0, nombre_maison):  # pour metre les maison de facon random
        import random
        x = random.randint(-300, 300)
        y = random.randint(0, 0)

        up()

        goto(x, y)
        down()

        maison()

        # cacher la tortue

    for a in range(0, nombre_nuage):  # pour metre les nuage de facon random
        import random
        x = random.randint(-300, 300)
        y = random.randint(100, 300)

        up()

        goto(x, y)
        down()

        nuage()

    ht()


def script2():
    seed()

    print("Bienvenue a dice")

    money = int(input("Entrez votre montant d'argent:"))

    spend_money = int(input("Entrez votre pari:"))

    for i in range(1000):

        moche = int(input("entrer 1 pour parier, entrer 2 pour rajouter de l'argent, entrer 3 pour changer le montant du pari, entrer 4 pour quiter:"))

        if moche == 1:
            value2 = randint(0, 100)

            if value2 > 50:
                money = money + spend_money
                print("vous avez gagner:", spend_money, "$")
                print("votre balance:", money)
                moche = 0

            else:
                money = money - spend_money
                print("vous avez perdue:", spend_money, "$")
                print("votre balance:", money)
                moche = 0

        elif moche == 2:
            new_money = int(input("Entrez le montant que vous vouler rajouter"))
            money = money + new_money


        elif moche == 3:
            spend_money = int(input("Entrez votre nouveau pari:"))

        elif moche == 4:
            quit()


        else:
            print("error")




print("Bonjour sur ma compilation de jeux amusant!")

choix = (input("Les jeux: devinette(d), sapin(s), cartier nuageux(cn), et les dés(ld)\nreponse: "))

if choix == 'd':
    script()
elif choix == 's':
    sapin()
elif choix == 'cn':
    cartier_nuageux()
elif choix == 'ld':
    script2()

else:
    print("error")