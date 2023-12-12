data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Le but est de relever les nombres qui sont adjacents a des symboles puis faire la somme -> 4361 ici

# direction(tableau_index, position_valeur)
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
list_data = []
suite = []


tableau = [x for x in data.split('\n')]

compar = []

for ligne in tableau:
    tab = []
    nb = ""
    for char in ligne:
        try:
            nb = nb + str(int(char))
        except ValueError:
            tab.append(nb)
            nb = ""

    compar.append(tab)

new_tab = []

for i in range(len(tableau)):
    nb_row = []
    chiffre = ""
    for y in range(len(tableau[i])):
        # chiffre = ""
        ok = True
        for direction in directions:
            try:
                if 0 <= i + direction[0] < len(tableau) and 0 <= y + direction[1] <= len(tableau[i + direction[0]]):
                    if (tableau[i + direction[0]][y + direction[1]].isdigit()
                            or tableau[i + direction[0]][y + direction[1]] == "."):
                        pass
                        # print(tableau[i][y])
                    else:
                        ok = False
                        chiffre = ''
                        break
            except IndexError:
                pass
        if ok and tableau[i][y] != '.':
            chiffre = chiffre + f"{(tableau[i][y])}"
        else:
            nb_row.append(chiffre)
            chiffre = ""

    new_tab.append(nb_row)

to_do_sum = []

for li in range(len(compar)):
    for nb in compar[li]:
        if nb != '':
            if nb not in new_tab[li]:
                to_do_sum.append(nb)

sum = 0
for to in to_do_sum:
    sum = sum + int(to)
print(sum)






