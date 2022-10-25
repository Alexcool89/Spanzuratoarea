

cuvant = "vacanta"
incercari_ramase = 3
litere_alese = []


def Intro():
    """ Afiseaza intro al jocului Spanzuratoarea."""
    print(
        """
    Bine ati venit la incerarea intelectuala binecunoscuta sub numele de Spanzuratoarea.
    Aceasta batalie se va da intre masina reprezentata de un procesor de silicon si om - cel ce a creat procesorul.
    Imbarbateaza-te omule, caci ai nevoie!!! BATALIA incepe!\n""")


def instructiuni():
    """ Afiseaza instructiunile jocului Spanzuratoarea."""
    print("\n\n")
    for e in cuvant:
        if e in litere_alese:
            print(e),
        else:
            print("_"),
    print("\n")
    print("""Poti incerca o completare prin introducerea unei litere.\
 Este permis sa gresesti de 3 ori!
    Numarul de sanse ramase este:\t"""),


def mesaj_final():
    if incercari_ramase > 0:
        print("\n FELICITARI!")
    else:
        print("\n Mai incearca!")


def incearca():
    le = ""
    while not len(le) == 1:
        litera = input(
            "Scrie o litera ce consideri ca exista in cuvantul ales - indiciu academie\t")
        le = litera.lower()
    return le


# main
Intro()
while (incercari_ramase > 0):
    instructiuni()
    print(incercari_ramase)
    litera = incearca()
    if litera in cuvant:
        print(litera, " exista in cuvantul ales de tine")
        litere_alese += [litera]
    else:
        print(litera, " nu exista in cuvantul ales de tine")
        incercari_ramase -= 1
    nr_de_litere_neghicite = 0
    for e in cuvant:
        if e not in litere_alese:
            nr_de_litere_neghicite += 1
    if not nr_de_litere_neghicite:
        break

mesaj_final()

input("\n\nApasa <enter> pt a iesi.")
