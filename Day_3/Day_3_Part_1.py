data = """467..114.9
.k.*....e.
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


list_data = []

for row in data.split('\n'):
    list_prov = []
    for char in row:
        try:
            list_prov.append(int(char))
        except ValueError:
            list_prov.append(char)
    list_data.append(list_prov)

i_prec = None
i_actu = None
i_suiv = None

for i in list_data:
    if not i_prec and not i_actu:
        i_actu = i
        i_suiv = list_data[list_data.index(i)+1]
    else:
        i_prec = i_actu
        i_actu = i
        try:
            i_suiv = list_data[list_data.index(i) + 1]
        except IndexError:
            i_suiv = []

    # premiere suite de symboles -> OK detecter si symbole en peripherie
    if list_data[0] == i:
        for y in range(len(i)):
            # premier element de la suite
            if y == 0 and is_integer(i[y]):
                if not i[y+1] == ".":
                    try:
                        int(i[y + 1])
                    except ValueError:
                        print(f"prems faux c'est marque {i[y + 1]}")
                if not i_suiv[y] == ".":
                    try:
                        int(i_suiv[y])
                    except ValueError:
                        print(f"prems faux c'est marque {i_suiv[y]}")
                if not i_suiv[y+1] == ".":
                    try:
                        int(i_suiv[y + 1])
                    except ValueError:
                        print(f"prems faux c'est marque {i_suiv[y + 1]}")
            # dernier element de la suite
            elif y == len(i) - 1 and is_integer(i[y]):
                if not i[y - 1] == ".":
                    try:
                        int(i[y - 1])
                    except ValueError:
                        print(f"derns faux c'est marque {i[y - 1]}")
                if not i_suiv[y] == ".":
                    try:
                        int(i_suiv[y])
                    except ValueError:
                        print(f"derns faux c'est marque {i_suiv[y]}")
                if not i_suiv[y - 1] == ".":
                    try:
                        int(i_suiv[y - 1])
                    except ValueError:
                        print(f"derns faux c'est marque {i_suiv[y - 1]}")
            elif is_integer(i[y]):
                if not i[y + 1] == ".":
                    try:
                        int(i[y + 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i[y + 1]}")
                if not i[y - 1] == ".":
                    try:
                        int(i[y - 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i[y - 1]}")
                if not i_suiv[y] == ".":
                    try:
                        int(i_suiv[y])
                    except ValueError:
                        print(f"mids faux c'est marque {i_suiv[y]}")
                if not i_suiv[y + 1] == ".":
                    try:
                        int(i_suiv[y + 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i_suiv[y + 1]}")
                if not i_suiv[y - 1] == ".":
                    try:
                        int(i_suiv[y - 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i_suiv[y - 1]}")

    # derniere suite de symboles -> OK detecter si symbole en peripherie
    elif list_data[-1] == i:
        for y in range(len(i)):
            # premier element de la suite
            if y == 0 and is_integer(i[y]):
                if not i[y + 1] == ".":
                    try:
                        int(i[y + 1])
                    except ValueError:
                        print(f"prems faux c'est marque {i[y + 1]}")
                if not i_prec[y] == ".":
                    try:
                        int(i_prec[y])
                    except ValueError:
                        print(f"prems faux c'est marque {i_prec[y]}")
                if not i_prec[y + 1] == ".":
                    try:
                        int(i_prec[y + 1])
                    except ValueError:
                        print(f"prems faux c'est marque {i_prec[y + 1]}")
            # dernier element de la suite
            elif y == len(i) - 1 and is_integer(i[y]):
                if not i[y - 1] == ".":
                    try:
                        int(i[y - 1])
                    except ValueError:
                        print(f"derns faux c'est marque {i[y - 1]}")
                if not i_prec[y] == ".":
                    try:
                        int(i_prec[y])
                    except ValueError:
                        print(f"derns faux c'est marque {i_prec[y]}")
                if not i_prec[y - 1] == ".":
                    try:
                        int(i_prec[y - 1])
                    except ValueError:
                        print(f"derns faux c'est marque {i_prec[y - 1]}")
            # middle suite

            elif is_integer(i[y]):
                if not i[y + 1] == ".":
                    try:
                        int(i[y + 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i[y + 1]}")
                if not i[y - 1] == ".":
                    try:
                        int(i[y - 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i[y - 1]}")
                if not i_prec[y] == ".":
                    try:
                        int(i_prec[y])
                    except ValueError:
                        print(f"mids faux c'est marque {i_prec[y]}")
                if not i_prec[y + 1] == ".":
                    try:
                        int(i_prec[y + 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i_prec[y + 1]}")
                if not i_prec[y - 1] == ".":
                    try:
                        int(i_prec[y - 1])
                    except ValueError:
                        print(f"mids faux c'est marque {i_prec[y - 1]}")

    # suites de symboles entre la premiere et la derniere
    else:
        pass
