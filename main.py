import pprint


def cipok_beolvasasa(forras):
    lista = []
    with open(forras, 'r', newline='') as file:
        next(file)
        for sor in file:
            oszlop = sor.strip().split(',')
            adatok = {
                'title': oszlop[0],
                'color': oszlop[1],
                'full price': oszlop[2],
                'current price': oszlop[3],
                'publish date': oszlop[4]
            }
            lista.append(adatok)
    return lista


def cipok_megjelenitese(cipok, opcio):
    print("Cipők rendezése {} alapján:".format(opcio))
    rendezett_cipok = sorted(cipok, key=lambda x: x[opcio])
    pprint.pprint(rendezett_cipok)


def main():
    nike_lista = "sneakers.csv"

    cipok = cipok_beolvasasa(nike_lista)

    print("Válassz rendezési lehetőséget:")
    print("1 - Title")
    print("2 - Color")
    print("3 - Full Price")
    print("4 - Current Price")
    print("5 - Publish Date")

    dontes = input("Adjon meg egy számot a választott rendezési opcióhoz: ")

    if dontes == "1":
        cipok_megjelenitese(cipok, "title")
    elif dontes == "2":
        cipok_megjelenitese(cipok, "color")
    elif dontes == "3":
        cipok_megjelenitese(cipok, "full price")
    elif dontes == "4":
        cipok_megjelenitese(cipok, "current price")
    elif dontes == "5":
        cipok_megjelenitese(cipok, "publish date")
    else:
        print("Hibás választás!")


main()