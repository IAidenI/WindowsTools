import math
from fractions import Fraction
import random


def menu_s(comp):
    print("[1] Pour simple vérification.")
    print("[2] Pour explication.")
    choix_s = int(input())
    if choix_s == 1:
        print("\n")
        a = int(input("Saisir a."))
        b = int(input("Saisir b."))
        c = int(input("Saisir c."))
        calcul_ss(a, b, c, comp)
    elif choix_s == 2:
        print("\n")
        print("Votre polynôme est de la forme ax² + bx + c (ex : 5x² + x + 9).")
        a = int(input("Veuillez saisir la valeur de a (ex : 5x² + x + 9 --> a = 5)."))
        b = int(input("Veuillez saisir la valeur de b (ex : 5x² + x + 9 --> b = 1)."))
        c = int(input("Veuillez saisir la valeur de c (ex : 5x² + x + 9 --> c = 9)."))
        calcul_se(a, b, c, comp)
    else:
        print("\n")
        print("Mauvais saisie.")
        print("\n")


def menu_a(comp):
    print("[1] Pour simple vérification.")
    print("[2] Pour explication.")
    choix_a = int(input())
    if choix_a == 1:
        print("\n")
        a = int(input("Saisir a."))
        b = int(input("Saisir b."))
        c = int(input("Saisir c."))
        calcul_ss(a, b, c, comp)
    elif choix_a == 2:
        print("\n")
        print("Votre polynôme est de la forme ax² + bx + c (ex : 5x² + x + 9).")
        a = int(input("Veuillez saisir la valeur de a (ex : 5x² + x + 9 --> a = 5)."))
        b = int(input("Veuillez saisir la valeur de b (ex : 5x² + x + 9 --> b = 1)."))
        c = int(input("Veuillez saisir la valeur de c (ex : 5x² + x + 9 --> c = 9)."))
        calcul_se(a, b, c, comp)
    else:
        print("\n")
        print("Mauvais saisie.")
        print("\n")


def calcul_se(a, b, c, comp):
    print("\n")
    print("Etape 1: Calcul du discriminant.")
    delta = pow(b, 2) - 4 * a * c
    print("Δ = ", b, "² - 4 x ", a, " x ", c)
    print("\n")
    print("Etape 2: signe du discriminant.")
    if delta > 0:
        print("Δ = ", delta, " > 0")
        print("Il existe deux racines réelles:")
        print("\n")
        print("Etape 3: Calcule des racines")
        x1 = (-b - math.sqrt(delta)) / 2 * a
        print("x1 = (-b + √Δ) / 2 x a = ", x1)
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print("x2 = (-b - √Δ) / 2 x a = ", x2)
        print("\n")
    elif delta == 0:
        print("delta = ", delta, " = 0")
        print("Il existe une racine possible.")
        print("\n")
        print("Etape 3: Calcule des racines")
        x0 = -b / 2 * a
        print("x1 = -b / 2 x a = ", x0)
        print("x0 = ", x0)
        print("\n")
    else:
        if comp == 0:
            print("delta = ", delta, " < 0")
            print("Il n'y a pas de racine réelles.")
            print("\n")
        else:
            print("A faire.")


def calcul_ss(a, b, c, comp):
    print("\n")
    delta = pow(b, 2) - 4 * a * c
    if delta > 0:
        x1_int = -b - math.sqrt(delta)
        x2_int = -b + math.sqrt(delta)
        x1 = Fraction(x1_int, 2 * a)
        x2 = Fraction(x2_int, 2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
        print("\n")
    elif delta == 0:
        x0 = -b / 2 * a
        print("x0 = ", x0)
        print("\n")
    else:
        if comp == 0:
            print("Il n'y a pas de racine réelles.")
            print("\n")
        else:
            x1 = complex(-b, -math.sqrt(-Fraction(delta)))
            x2 = complex(-b, math.sqrt(-Fraction(delta)))
            a = 2 * a
            print("x1 = ", x1, "/", a)
            print("x2 = ", x2, "/", a)
            print("\n")


choix = 3
while choix != 99:
    print("#########################################################################################")
    print("## Bienveune dans cette algorithme qui permet de résoudre des polynôme du second degré. ##")
    print("##########################################################################################")
    print("Saisir :")
    print("[1]  Pour la résolution sans les complexes")
    print("[2]  Pour la résolution avec les complexes")
    print("[99] Pour quitter")
    choix = int(input())
    if choix == 1:
        print("\n")
        comp = 0
        menu_s(comp)
    elif choix == 2:
        print("\n")
        comp = 1
        menu_a(comp)
    elif choix == 99:
        quit()
    else:
        print("\n")
        print("Mauvaise saisie.")
        print("\n")
