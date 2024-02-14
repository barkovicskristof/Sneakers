import pprint


def beolvas_cipok(forras_fajl):
    cipok = []
    with open(forras_fajl, 'r', newline='') as fajl:
        next(fajl)
        for sor in fajl:
            oszlopok = sor.strip().split(',')
            adatok = {
                'title': oszlopok[0],
                'color': oszlopok[1],
                'full price': float(oszlopok[2]),
                'current price': float(oszlopok[3]),
                'publish date': oszlopok[4]
            }
            cipok.append(adatok)
    return cipok


def megjelenit_cipok(cipok, rendezesi_opcio):
    print("Cipők rendezése {} alapján:".format(rendezesi_opcio))
    rendezett_cipok = sorted(cipok, key=lambda x: x[rendezesi_opcio])
    pprint.pprint(rendezett_cipok)


def main():
    forras = "sneakers.csv"

    cipok = beolvas_cipok(forras)

    print("Válassz rendezési lehetőséget:")
    print("1 - Title")
    print("2 - Color")
    print("3 - Full Price")
    print("4 - Current Price")
    print("5 - Publish Date")

    dontes = input("Adjon meg egy számot a választott rendezési opcióhoz: ")

    if dontes == "1":
        megjelenit_cipok(cipok, "title")
    elif dontes == "2":
        megjelenit_cipok(cipok, "color")
    elif dontes == "3":
        megjelenit_cipok(cipok, "full price")
    elif dontes == "4":
        megjelenit_cipok(cipok, "current price")
    elif dontes == "5":
        megjelenit_cipok(cipok, "publish date")
    else:
        print("Hibás választás!")


main()
