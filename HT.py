import HTTavoiteKirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset sademäärät")
    print("5) Lue ja yhdistä Korkeasaari tiedosto")
    print("6) Kirjoita yhdistetty data tiedostoon")
    print("7) Analysoi viikoittaiset kävijämäärät")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    valinta = 1
    oliolista = []
    tuloslista = []
    tulosteet = []
    
    while valinta != 0:
        valinta = valikko()
        if valinta == 1:
            nimi1 = HTKirjasto.kysyNimi("Anna luettavan tiedoston nimi: ")
            oliolista = HTKirjasto.tiedostoLue(nimi1, oliolista)
        elif valinta == 2:
            if len(oliolista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
            else:
                tuloslista = HTKirjasto.analysoi(oliolista, tuloslista)
                tulosteet = HTKirjasto.muotoilu(tuloslista, tulosteet)
        elif valinta == 3:
            if len(tuloslista) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.\n")
            else:
                nimi2 = HTKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTKirjasto.tiedostoKirjoita(nimi2, tulosteet)
        elif valinta == 4:
            if len(oliolista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
            else:
                nimi3 = HTKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                tulosteet = HTKirjasto.paivittainenAnalyysi(nimi3, oliolista, tulosteet)
                HTKirjasto.tiedostoKirjoita(nimi3, tulosteet)
        elif valinta == 5:
            if len(tuloslista) == 0:
                print("Lue sademäärät ennen kävijämäärätietoja.\n")
            else:
                nimi4 = HTKirjasto.kysyNimi("Anna luettavan tiedoston nimi: ")
                tulosteet = HTKirjasto.lueJaYhdista(nimi4, tuloslista, tulosteet)
        elif valinta == 6:
            if len(tulosteet) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.\n")
            else:
                nimi5 = HTKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTKirjasto.tiedostoKirjoita(nimi5, tulosteet)
        elif valinta == 7:
            if len(tuloslista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
            else:
                tulosteet = HTKirjasto.kategoriaAnalyysi(tuloslista, tulosteet)
                nimi6 = HTKirjasto.kysyNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTKirjasto.tiedostoKirjoita(nimi6, tulosteet)
        elif valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
            
    print("Kiitos ohjelman käytöstä.")
    oliolista.clear()
    tuloslista.clear()
    tulosteet.clear()
    return None

paaohjelma()

#eof

