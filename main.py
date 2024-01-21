# coffee machine

from art import logo
from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "eau": 50,
            "cafe": 18,
        },
        "prix": 1.5,
    },
    "latte": {
        "ingredients": {
            "eau": 200,
            "lait": 150,
            "cafe": 24,
        },
        "prix": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "eau": 250,
            "lait": 100,
            "cafe": 24,
        },
        "prix": 3,
    },
}

ressource = {"eau": 300, "lait": 200, "cafe": 100}

choix = ""
profit = 0

def print_report(ress):
    print(f"Quantité d'eau: {ress["eau"]}ml")
    print(f"Quantité de lait: {ress["lait"]}ml")
    print(f"Quantité de café: {ress["cafe"]}g")
    print(f"Argent : {format(profit, '.2f')}$")
    input()
    system('cls')

def fill():
    ressource["eau"] = 300
    ressource["lait"] = 200
    ressource["cafe"] = 100

def check_ress(choix, cafe, ress):
    if cafe["ingredients"]["eau"] <= ress["eau"]:
        if cafe["ingredients"]["cafe"] <= ress["cafe"]:
            if choix != "espresso":
                if cafe["ingredients"]["lait"] <= ress["lait"]:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False


def paiement():
    montant = 0
    montant += int(input("Nombre de cinq sous: ")) * 0.05
    montant += int(input("Nombre de dix sous: ")) * 0.1
    montant += int(input("Nombre de vingt-cinq sous: ")) * 0.25
    return montant

def trx(mnt, prx):
    chng = mnt - prx
    return chng

def majinv(choix, inv):
    ressource["eau"] -= inv["ingredients"]["eau"]
    ressource["cafe"] -= inv["ingredients"]["cafe"]
    if choix != "espresso":
        ressource["lait"] -= inv["ingredients"]["lait"]


while choix != "quit":

    print(logo)
    choix = input("Quel est votre choix (espresso, latte, cappuccino) ? ").lower()

    if choix == "rapport":
        print_report(ressource)

    if choix in MENU:
        if check_ress(choix, MENU[choix], ressource):
            print(f"Le prix de ce café est de {format(MENU[choix]["prix"], '.2f')}$")
            montant = paiement()
            if montant < MENU[choix]["prix"]:
                print(f"Montant insuffisant! On vous retourne votre paiement : {format(montant, '.2f')}$")
                input()
                system('cls')
            else:
                change = trx(montant, MENU[choix]["prix"])
                profit = profit + MENU[choix]["prix"]
                majinv(choix, MENU[choix])
                input(f"Voici votre {choix} et votre monnaie : {format(change,'.2f')}$")
                system('cls')
        else:
            input("Manque d'inventaire! Contacter le fournisseur!")
            system('cls')
    if choix == "fill":
        fill()
        system('cls')
